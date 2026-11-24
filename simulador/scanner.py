
from simulador.palavras_chave import afd_palavra_chave
from simulador.identificadores import afd_identificador
from simulador.floats import afd_float
from simulador.inteiros import afd_inteiro
from simulador.operadores import afd_operador
from simulador.delimitadores import afd_delimitador

brancos = " \t\n\r"

# A ordem desta lista e a prioridade da regra R2 da especificacao.
automatos = [
    afd_palavra_chave,
    afd_identificador,
    afd_float,
    afd_inteiro,
    afd_operador,
    afd_delimitador,
]


class ErroLexico(Exception):
    pass


def tokenizar(texto):
    tokens = []
    posicao = 0
    linha = 1
    coluna = 1

    while posicao < len(texto):
        caractere = texto[posicao]

        if caractere in brancos:
            if caractere == "\n":
                linha += 1
                coluna = 1
            else:
                coluna += 1

            posicao += 1
            continue

        melhor_fim = -1
        melhor_automato = None

        for automato in automatos:
            fim = automato.prefixo_mais_longo(texto, posicao)

            if fim is not None and fim > melhor_fim:
                melhor_fim = fim
                melhor_automato = automato

        if melhor_automato is None:
            raise ErroLexico(
                f"caractere inesperado {caractere!r} "
                f"na linha {linha}, coluna {coluna}"
            )

        tokens.append(
            (melhor_automato.token, texto[posicao:melhor_fim], linha, coluna)
        )

        coluna += melhor_fim - posicao
        posicao = melhor_fim

    return tokens
