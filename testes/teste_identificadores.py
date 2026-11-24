
from simulador.identificadores import afd_identificador
from testes.apoio import rodar, aceita

casos = [
    ("idade", True), ("_total", True), ("valor123", True), ("A", True),
    ("_", True), ("nome_completo", True), ("abc123_xyz", True),
    ("sentinela", True),
    ("", False), ("123valor", False), ("9abc", False),
    ("nome@", False), ("valor 123", False),
]


def executar():
    return rodar("AFD de identificadores", casos, aceita(afd_identificador))


if __name__ == "__main__":
    executar()
