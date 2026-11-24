
import sys

from simulador.scanner import tokenizar, ErroLexico


def imprimir(tokens):
    print(f"{'#':>3}  {'LEXEMA':<12} {'CLASSE':<14} LINHA:COLUNA")

    for numero, (classe, lexema, linha, coluna) in enumerate(tokens, 1):
        print(f"{numero:>3}  {lexema:<12} {classe:<14} {linha}:{coluna}")

    print(f"\n{len(tokens)} tokens")


def analisar(texto):
    try:
        imprimir(tokenizar(texto))
    except ErroLexico as erro:
        print(f"ERRO LEXICO: {erro}")


def interativo():
    print("=== ANALISADOR LEXICO DA LINGUAGEM CORURIPE ===")
    print("Digite uma linha de codigo, ou 'sair' para encerrar.\n")

    while True:
        linha = input("> ")

        if linha.lower() == "sair":
            break

        analisar(linha)
        print()


if len(sys.argv) > 1:
    with open(sys.argv[1], encoding="utf-8") as arquivo:
        analisar(arquivo.read())
else:
    interativo()
