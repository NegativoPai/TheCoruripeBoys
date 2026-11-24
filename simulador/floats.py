
from simulador.automato import AFD
import string

digitos = string.digits

alfabeto = set(digitos + ".")

estados = {"q0", "q1", "q2", "q3", "q4", "qd"}

transicoes = {}

transicoes[("q0", "0")] = "q1"
transicoes[("q0", ".")] = "qd"
transicoes[("q1", ".")] = "q3"
transicoes[("q2", ".")] = "q3"
transicoes[("q3", ".")] = "qd"
transicoes[("q4", ".")] = "qd"
transicoes[("qd", ".")] = "qd"

for digito in digitos:
    if digito != "0":
        transicoes[("q0", digito)] = "q2"

    transicoes[("q1", digito)] = "qd"
    transicoes[("q2", digito)] = "q2"
    transicoes[("q3", digito)] = "q4"
    transicoes[("q4", digito)] = "q4"
    transicoes[("qd", digito)] = "qd"

afd_float = AFD(
    estados=estados,
    alfabeto=alfabeto,
    transicoes=transicoes,
    estado_inicial="q0",
    estados_finais={"q4"},
    token="FLOAT"
)

afd_float.rotulos = {
    "q0": "inicial",
    "q1": "parte inteira igual a zero",
    "q2": "parte inteira iniciada por 1 a 9",
    "q3": "ponto lido, aguarda digito",
    "qd": "erro",
    "q4": "float valido",
}
