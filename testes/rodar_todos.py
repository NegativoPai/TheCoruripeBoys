
import sys

from testes import (
    teste_validacao,
    teste_identificadores,
    teste_inteiros,
    teste_floats,
    teste_palavras_chave,
    teste_operadores,
    teste_delimitadores,
    teste_scanner,
)

modulos = [
    teste_validacao,
    teste_identificadores,
    teste_inteiros,
    teste_floats,
    teste_palavras_chave,
    teste_operadores,
    teste_delimitadores,
    teste_scanner,
]

aprovados = 0
total = 0

for modulo in modulos:
    passou, executados = modulo.executar()
    aprovados += passou
    total += executados

print(f"TOTAL GERAL: {aprovados}/{total}")

if aprovados != total:
    print(f"{total - aprovados} teste(s) falharam")
    sys.exit(1)

sys.exit(0)
