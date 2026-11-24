
from simulador.inteiros import afd_inteiro
from testes.apoio import rodar, aceita

casos = [
    ("0", True), ("7", True), ("10", True), ("123", True), ("1000000", True),
    ("", False), ("00", False), ("007", False), ("01", False),
    ("-45", False), ("+89", False), ("12.5", False), ("abc", False),
    ("12a", False),
]


def executar():
    return rodar("AFD de inteiros", casos, aceita(afd_inteiro))


if __name__ == "__main__":
    executar()
