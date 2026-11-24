
from simulador.scanner import tokenizar, ErroLexico
from testes.apoio import verificar


def classificar(texto):
    return [(classe, lexema) for classe, lexema, _, _ in tokenizar(texto)]


def erro(texto):
    try:
        tokenizar(texto)
    except ErroLexico as excecao:
        return str(excecao)

    return "nenhum erro"


with open("exemplos/programa.crp", encoding="utf-8") as arquivo:
    programa = arquivo.read()


def montar():
    return [
        ("programa de exemplo: 32 tokens",
         len(tokenizar(programa)), 32),

        ("R2: 'se' e palavra-chave, nao identificador",
         classificar("se"), [("PALAVRA_CHAVE", "se")]),

        ("R1: 'sentinela' e identificador, nao 'se' + resto",
         classificar("sentinela"), [("IDENTIFICADOR", "sentinela")]),

        ("R1: 'variavel' e identificador, nao 'var' + resto",
         classificar("variavel"), [("IDENTIFICADOR", "variavel")]),

        ("R2: 'senao' e palavra-chave",
         classificar("senao"), [("PALAVRA_CHAVE", "senao")]),

        ("R1: '>=' e um operador so",
         classificar(">="), [("OPERADOR", ">=")]),

        ("R1: '> =' sao dois operadores",
         classificar("> ="), [("OPERADOR", ">"), ("OPERADOR", "=")]),

        ("R1: '1.5' e float, nao inteiro seguido de ponto",
         classificar("1.5"), [("FLOAT", "1.5")]),

        ("'10' e inteiro, nao float incompleto",
         classificar("10"), [("INTEIRO", "10")]),

        ("sinal fora do literal: 'a+1' sao tres tokens",
         classificar("a+1"),
         [("IDENTIFICADOR", "a"), ("OPERADOR", "+"), ("INTEIRO", "1")]),

        ("sinal fora do literal: '-5' sao dois tokens",
         classificar("-5"), [("OPERADOR", "-"), ("INTEIRO", "5")]),

        ("zero a esquerda: '007' vira tres inteiros",
         classificar("007"),
         [("INTEIRO", "0"), ("INTEIRO", "0"), ("INTEIRO", "7")]),

        ("'x<=y' sem espacos",
         classificar("x<=y"),
         [("IDENTIFICADOR", "x"), ("OPERADOR", "<="), ("IDENTIFICADOR", "y")]),

        ("so brancos nao gera token",
         classificar("   \n\t  "), []),

        ("R3: caractere fora do alfabeto",
         erro("@"), "caractere inesperado '@' na linha 1, coluna 1"),

        ("R3: erro na segunda linha",
         erro("var x\n  @"), "caractere inesperado '@' na linha 2, coluna 3"),

        ("R3: '!' sozinho nao e token",
         erro("!"), "caractere inesperado '!' na linha 1, coluna 1"),

        ("R3: chave nao pertence a linguagem",
         erro("{"), "caractere inesperado '{' na linha 1, coluna 1"),

        ("R3: '1.' tem ponto solto na coluna 2",
         erro("1."), "caractere inesperado '.' na linha 1, coluna 2"),
    ]


def executar():
    return verificar("Scanner", montar())


if __name__ == "__main__":
    executar()
