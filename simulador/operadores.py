
from simulador.automato import afd_de_palavras

operadores = [
    "+", "-", "*", "/", "%",
    "=", "==", "!=",
    "<", "<=", ">", ">=",
]

afd_operador = afd_de_palavras(operadores, "OPERADOR")
