
from simulador.operadores import afd_operador
from testes.apoio import rodar, aceita

casos = [
    ("+", True), ("-", True), ("*", True), ("/", True), ("%", True),
    ("=", True), ("==", True), ("!=", True),
    ("<", True), ("<=", True), (">", True), (">=", True),
    ("", False), ("!", False), ("===", False), ("<>", False), ("=<", False),
]


def executar():
    return rodar("AFD de operadores", casos, aceita(afd_operador))


if __name__ == "__main__":
    executar()
