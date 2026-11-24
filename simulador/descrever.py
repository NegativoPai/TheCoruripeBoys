
from simulador.palavras_chave import afd_palavra_chave
from simulador.identificadores import afd_identificador
from simulador.floats import afd_float
from simulador.inteiros import afd_inteiro
from simulador.operadores import afd_operador
from simulador.delimitadores import afd_delimitador


def ordem(estado):
    if estado == "qd":
        return (1, 0)

    return (0, int(estado[1:]))


def classes_de_simbolos(automato):
    grupos = {}

    for simbolo in sorted(automato.alfabeto):
        chave = tuple(
            automato.transicoes[(estado, simbolo)]
            for estado in sorted(automato.estados, key=ordem)
        )
        grupos.setdefault(chave, []).append(simbolo)

    return sorted(grupos.values())


def rotulo(simbolos):
    partes = []
    inicio = 0

    for i in range(1, len(simbolos) + 1):
        fim_do_bloco = (
            i == len(simbolos)
            or ord(simbolos[i]) != ord(simbolos[i - 1]) + 1
        )

        if fim_do_bloco:
            if i - inicio >= 3:
                partes.append(f"{simbolos[inicio]}-{simbolos[i - 1]}")
            else:
                partes.extend(simbolos[inicio:i])

            inicio = i

    return ",".join(partes)


def descrever(automato):
    estados = sorted(automato.estados, key=ordem)
    colunas = classes_de_simbolos(automato)

    print(f"===== {automato.token} =====")
    print(f"Q  = {{{', '.join(estados)}}}")
    print(f"S  = {len(automato.alfabeto)} simbolos")
    print(f"q0 = {automato.estado_inicial}")
    print(f"F  = {{{', '.join(sorted(automato.estados_finais, key=ordem))}}}")
    print(f"|Q| x |S| = {len(estados)} x {len(automato.alfabeto)} "
          f"= {len(automato.transicoes)} transicoes")

    print("\nestados:")

    for estado in estados:
        marca = ""

        if estado == automato.estado_inicial:
            marca += ">"

        if estado in automato.estados_finais:
            marca += "*"

        print(f"  {marca:>2} {estado:<4} {automato.rotulos.get(estado, '')}")

    largura = max(len(rotulo(c)) for c in colunas)
    largura = max(largura, 6)

    print("\ntabela de transicao:")
    print("     " + "  ".join(f"{rotulo(c):>{largura}}" for c in colunas))

    for estado in estados:
        celulas = [
            f"{automato.transicoes[(estado, c[0])]:>{largura}}"
            for c in colunas
        ]
        print(f"  {estado:<3}" + "  ".join(celulas))

    print("\n(> estado inicial, * estado final)\n")


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
        descrever(automato)
