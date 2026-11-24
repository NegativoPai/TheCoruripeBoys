
from simulador.automato import AFD
import string

digitos = string.digits

alfabeto = set(digitos)

estados = {"q0", "q1", "q2", "qd"}

transicoes = {}

transicoes[("q0", "0")] = "q1"

for digito in digitos:
    if digito != "0":
        transicoes[("q0", digito)] = "q2"

    transicoes[("q1", digito)] = "qd"
    transicoes[("q2", digito)] = "q2"
    transicoes[("qd", digito)] = "qd"

afd_inteiro = AFD(
    estados=estados,
    alfabeto=alfabeto,
    transicoes=transicoes,
    estado_inicial="q0",
    estados_finais={"q1", "q2"},
    token="INTEIRO"
)

afd_inteiro.rotulos = {
    "q0": "inicial",
    "q1": "zero isolado",
    "q2": "inteiro positivo sem zero a esquerda",
    "qd": "erro",
}
