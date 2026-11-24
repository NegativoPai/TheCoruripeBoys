
from simulador.identificadores import afd_identificador
from simulador.inteiros import afd_inteiro
from simulador.floats import afd_float
from simulador.delimitadores import afd_delimitador
from simulador.operadores import afd_operador
from simulador.palavras_chave import afd_palavra_chave

especiais = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "_": r"\_",
    "%": r"\%",
    "$": r"\$",
    "&": r"\&",
    "#": r"\#",
    "^": r"\^{}",
    "~": r"\~{}",
    "<": r"\textless{}",
    ">": r"\textgreater{}",
}


def ordem(estado):
    if estado == "qd":
        return (1, 0)

    return (0, int(estado[1:]))


def escapar(texto):
    return "".join(especiais.get(caractere, caractere) for caractere in texto)


def estado_latex(estado):
    return f"$q_{{{escapar(estado[1:])}}}$"


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
                partes.append(f"{simbolos[inicio]}--{simbolos[i - 1]}")
            else:
                partes.extend(simbolos[inicio:i])

            inicio = i

    return escapar(", ".join(partes))


def tabela(automato):
    colunas = classes_de_simbolos(automato)

    linhas = [
        r"\begin{table}[htb]",
        r"\centering",
        rf"\caption{{Funcao de transicao do AFD de "
        rf"{escapar(automato.token.replace('_', ' ').lower())}}}",
        rf"\label{{tab:afd-{automato.token.lower().replace('_', '-')}}}",
        r"\begin{tabular}{l|" + "c" * len(colunas) + "}",
        r"\hline",
    ]

    cabecalho = [r"$\delta$"]

    for simbolos in colunas:
        cabecalho.append(rf"\texttt{{{rotulo(simbolos)}}}")

    linhas.append(" & ".join(cabecalho) + r" \\")
    linhas.append(r"\hline")

    for estado in sorted(automato.estados, key=ordem):
        marca = ""

        if estado == automato.estado_inicial:
            marca += r"$\rightarrow$ "

        if estado in automato.estados_finais:
            marca += r"$*$ "

        celulas = [marca + estado_latex(estado)]

        for simbolos in colunas:
            celulas.append(estado_latex(automato.transicoes[(estado, simbolos[0])]))

        linhas.append(" & ".join(celulas) + r" \\")

    linhas.append(r"\hline")
    linhas.append(r"\end{tabular}")
    linhas.append(r"\end{table}")

    return "\n".join(linhas)


automatos = [
    afd_identificador,
    afd_inteiro,
    afd_float,
    afd_delimitador,
    afd_operador,
    afd_palavra_chave,
]


def gerar(caminho="geradas/tabelas.tex"):
    blocos = [
        "% Arquivo gerado por simulador/tabela_latex.py",
        "% Nao editar a mao: rode o script de novo depois de mudar algum AFD.",
        "",
    ]

    for automato in automatos:
        blocos.append(tabela(automato))
        blocos.append("")

    with open(caminho, "w", encoding="utf-8", newline="\n") as arquivo:
        arquivo.write("\n".join(blocos))

    for automato in automatos:
        colunas = classes_de_simbolos(automato)
        print(f"{automato.token:15} {len(automato.estados):3} estados x "
              f"{len(colunas)} colunas "
              f"(alfabeto de {len(automato.alfabeto)} simbolos)")

    print(f"\n{caminho} gerado")


if __name__ == "__main__":
    gerar()
