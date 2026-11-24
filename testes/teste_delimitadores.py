
from simulador.delimitadores import afd_delimitador
from testes.apoio import rodar, aceita

casos = [
    ("(", True), (")", True), (";", True), (",", True),
    ("", False), ("()", False), (";;", False),
    ("{", False), ("}", False),
]


def executar():
    return rodar("AFD de delimitadores", casos, aceita(afd_delimitador))


if __name__ == "__main__":
    executar()
