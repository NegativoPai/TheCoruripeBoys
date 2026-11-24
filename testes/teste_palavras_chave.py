
from simulador.palavras_chave import afd_palavra_chave
from testes.apoio import rodar, aceita

casos = [
    ("se", True), ("senao", True), ("var", True), ("fim", True),
    ("", False), ("s", False), ("sen", False), ("sena", False),
    ("fi", False), ("va", False), ("ser", False), ("SE", False),
    ("variavel", False), ("senaoo", False),
]


def executar():
    return rodar("AFD de palavras-chave", casos, aceita(afd_palavra_chave))


if __name__ == "__main__":
    executar()
