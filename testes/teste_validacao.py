
from simulador.palavras_chave import afd_palavra_chave
from simulador.identificadores import afd_identificador
from simulador.floats import afd_float
from simulador.inteiros import afd_inteiro
from simulador.operadores import afd_operador
from simulador.delimitadores import afd_delimitador
from testes.apoio import verificar

# Valores declarados na tabela de docs/especificacao.md
esperado = {
    "PALAVRA_CHAVE": (13, 10),
    "IDENTIFICADOR": (3, 63),
    "INTEIRO": (4, 10),
    "FLOAT": (6, 11),
    "OPERADOR": (15, 9),
    "DELIMITADOR": (6, 4),
}

automatos = [
    afd_palavra_chave,
    afd_identificador,
    afd_float,
    afd_inteiro,
    afd_operador,
    afd_delimitador,
]


def montar():
    checagens = []

    for automato in automatos:
        nome = automato.token
        estados, simbolos = esperado[nome]

        checagens.append(
            (f"{nome}: tupla bem formada", automato.validar(), [])
        )
        checagens.append(
            (f"{nome}: |Q| e |S| conforme a especificacao",
             (len(automato.estados), len(automato.alfabeto)),
             (estados, simbolos))
        )
        checagens.append(
            (f"{nome}: delta e total",
             len(automato.transicoes), estados * simbolos)
        )
        checagens.append(
            (f"{nome}: todo estado e alcancavel",
             automato.estados - automato.alcancaveis(), set())
        )

    return checagens


def executar():
    return verificar("Validacao das tuplas", montar())


if __name__ == "__main__":
    executar()
