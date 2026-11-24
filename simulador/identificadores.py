
from simulador.automato import AFD
import string

letras = string.ascii_letters
digitos = string.digits

alfabeto = set(letras + digitos + "_")

estados = {"q0", "q1", "qd"}

transicoes = {}

for caractere in alfabeto:
    if caractere in letras + "_":
        transicoes[("q0", caractere)] = "q1"
    else:
        transicoes[("q0", caractere)] = "qd"

    transicoes[("q1", caractere)] = "q1"
    transicoes[("qd", caractere)] = "qd"

afd_identificador = AFD(
    estados=estados,
    alfabeto=alfabeto,
    transicoes=transicoes,
    estado_inicial="q0",
    estados_finais={"q1"},
    token="IDENTIFICADOR"
)

afd_identificador.rotulos = {
    "q0": "inicial",
    "q1": "identificador valido",
    "qd": "erro",
}
