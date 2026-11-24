
from simulador.identificadores import afd_identificador
from simulador.inteiros import afd_inteiro
from simulador.floats import afd_float
from simulador.delimitadores import afd_delimitador
from simulador.operadores import afd_operador
from simulador.palavras_chave import afd_palavra_chave


def ordem(estado):
    if estado == "qd":
        return (1, 0)

    return (0, int(estado[1:]))


def assinatura(automato, estado, bloco_de):
    return tuple(
        bloco_de[automato.transicoes[(estado, simbolo)]]
        for simbolo in sorted(automato.alfabeto)
    )


def minimizar(automato, mostrar_passos=True):
    alcancaveis = automato.alcancaveis()
    removidos = automato.estados - alcancaveis

    if mostrar_passos and removidos:
        print(f"  passo 0: removidos {len(removidos)} estados inalcancaveis: "
              f"{sorted(removidos, key=ordem)}")

    finais = automato.estados_finais & alcancaveis
    nao_finais = alcancaveis - finais

    particao = [bloco for bloco in (finais, nao_finais) if bloco]

    if mostrar_passos:
        print(f"  passo 1: particao inicial {{F, Q-F}} com "
              f"{len(finais)} e {len(nao_finais)} estados")

    passo = 1

    while True:
        bloco_de = {}

        for indice, bloco in enumerate(particao):
            for estado in bloco:
                bloco_de[estado] = indice

        nova = []

        for bloco in particao:
            grupos = {}

            for estado in sorted(bloco, key=ordem):
                chave = assinatura(automato, estado, bloco_de)
                grupos.setdefault(chave, set()).add(estado)

            nova.extend(grupos.values())

        passo += 1

        if len(nova) == len(particao):
            break

        if mostrar_passos:
            print(f"  passo {passo}: {len(particao)} -> {len(nova)} classes")

        particao = nova

    if mostrar_passos:
        print(f"  passo {passo}: particao estavel com "
              f"{len(particao)} classes de equivalencia")

    return particao, removidos


def relatar(automato):
    print(f"--- {automato.token} ---")
    print(f"  original: {len(automato.estados)} estados")

    particao, removidos = minimizar(automato)

    fundidos = [bloco for bloco in particao if len(bloco) > 1]
    economia = len(automato.estados) - len(removidos) - len(particao)

    print(f"  minimizado: {len(particao)} estados "
          f"({len(automato.estados)} - {len(removidos)} inalcancaveis "
          f"- {economia} fundidos)")

    if not fundidos:
        print("  nenhuma fusao: o automato ja era minimo\n")
        return

    print(f"  classes com mais de um estado ({len(fundidos)}):")

    for bloco in sorted(fundidos, key=lambda b: sorted(b, key=ordem)):
        nomes = sorted(bloco, key=ordem)
        lidos = ", ".join(
            f"{n} [{automato.rotulos.get(n, '')}]" for n in nomes
        )
        print(f"    {{{lidos}}}")

    print()


automatos = [
    afd_identificador,
    afd_inteiro,
    afd_float,
    afd_delimitador,
    afd_operador,
    afd_palavra_chave,
]


if __name__ == "__main__":
    for automato in automatos:
        relatar(automato)
