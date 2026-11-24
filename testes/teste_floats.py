
from simulador.floats import afd_float
from testes.apoio import rodar, aceita

casos = [
    ("1.5", True), ("0.5", True), ("0.0", True), ("10.25", True),
    ("1.50", True), ("123.456", True),
    ("", False), ("1", False), (".5", False), ("5.", False),
    ("007.5", False), ("01.5", False), ("1..5", False), ("1.5.5", False),
    ("1.a", False),
]


def executar():
    return rodar("AFD de floats", casos, aceita(afd_float))


if __name__ == "__main__":
    executar()
