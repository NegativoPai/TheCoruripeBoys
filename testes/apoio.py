
def rodar(titulo, casos, funcao):
    aprovados = 0

    print(f"=== {titulo} ===")

    for entrada, esperado in casos:
        obtido = funcao(entrada)
        passou = obtido == esperado

        if passou:
            aprovados += 1

        print(
            f"  {entrada!r:<24} "
            f"esperado: {esperado!s:<6} "
            f"obtido: {obtido!s:<6} "
            f"{'OK' if passou else 'FALHOU'}"
        )

    print(f"  {aprovados}/{len(casos)} aprovados\n")

    return aprovados, len(casos)


def aceita(automato):
    return lambda cadeia: automato.reconhecer(cadeia) is not None


def verificar(titulo, checagens):
    aprovados = 0

    print(f"=== {titulo} ===")

    for rotulo, obtido, esperado in checagens:
        if obtido == esperado:
            aprovados += 1
            print(f"  {rotulo:<48} OK")
        else:
            print(f"  {rotulo:<48} FALHOU")
            print(f"      esperado: {esperado!r}")
            print(f"      obtido:   {obtido!r}")

    print(f"  {aprovados}/{len(checagens)} aprovados\n")

    return aprovados, len(checagens)
