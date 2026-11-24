
from simulador.automato import afd_de_palavras

delimitadores = ["(", ")", ";", ","]

afd_delimitador = afd_de_palavras(delimitadores, "DELIMITADOR")
