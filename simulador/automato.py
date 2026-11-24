class AFD:
    def __init__(self, estados, alfabeto, transicoes,
                 estado_inicial, estados_finais, token):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)
        self.token = token
        self.rotulos = {}
        self.mortos = self.calcular_mortos()

    def reconhecer(self, cadeia):
        estado = self.estado_inicial

        for caractere in cadeia:
            if caractere not in self.alfabeto:
                return None

            estado = self.transicoes.get((estado, caractere))

            if estado is None:
                return None

        if estado in self.estados_finais:
            return self.token

        return None

    def validar(self):
        problemas = []

        if self.estado_inicial not in self.estados:
            problemas.append(
                f"estado inicial {self.estado_inicial} nao pertence a Q"
            )

        for estado in sorted(self.estados_finais):
            if estado not in self.estados:
                problemas.append(f"estado final {estado} nao pertence a Q")

        for origem, simbolo in sorted(self.transicoes):
            destino = self.transicoes[(origem, simbolo)]

            if origem not in self.estados:
                problemas.append(f"transicao parte de {origem}, fora de Q")

            if simbolo not in self.alfabeto:
                problemas.append(f"transicao le {simbolo!r}, fora do alfabeto")

            if destino not in self.estados:
                problemas.append(f"transicao chega em {destino}, fora de Q")

        for estado in sorted(self.estados):
            for simbolo in sorted(self.alfabeto):
                if (estado, simbolo) not in self.transicoes:
                    problemas.append(f"falta delta({estado}, {simbolo!r})")

        return problemas

    def alcancaveis(self):
        atingidos = {self.estado_inicial}

        while True:
            novos = set(atingidos)

            for origem, simbolo in self.transicoes:
                if origem in atingidos:
                    novos.add(self.transicoes[(origem, simbolo)])

            if novos == atingidos:
                return atingidos

            atingidos = novos

    def calcular_mortos(self):
        vivos = set(self.estados_finais)

        while True:
            novos = set(vivos)

            for origem, simbolo in self.transicoes:
                if self.transicoes[(origem, simbolo)] in vivos:
                    novos.add(origem)

            if novos == vivos:
                return self.estados - vivos

            vivos = novos

    def prefixo_mais_longo(self, texto, inicio=0):
        estado = self.estado_inicial
        posicao = inicio
        fim = -1

        if estado in self.estados_finais:
            fim = inicio

        while posicao < len(texto):
            caractere = texto[posicao]

            if caractere not in self.alfabeto:
                break

            proximo = self.transicoes.get((estado, caractere))

            if proximo is None or proximo in self.mortos:
                break

            estado = proximo
            posicao += 1

            if estado in self.estados_finais:
                fim = posicao

        if fim == -1:
            return None

        return fim


def afd_de_palavras(palavras, token):
    alfabeto = set()

    for palavra in palavras:
        alfabeto.update(palavra)

    estados = {"q0", "qd"}
    transicoes = {}
    finais = set()
    nomes = {"": "q0"}
    contador = 0

    for palavra in sorted(palavras):
        for tamanho in range(1, len(palavra) + 1):
            prefixo = palavra[:tamanho]

            if prefixo not in nomes:
                contador += 1
                nomes[prefixo] = f"q{contador}"
                estados.add(nomes[prefixo])

            origem = nomes[prefixo[:-1]]
            transicoes[(origem, prefixo[-1])] = nomes[prefixo]

        finais.add(nomes[palavra])

    for estado in estados:
        for simbolo in alfabeto:
            if (estado, simbolo) not in transicoes:
                transicoes[(estado, simbolo)] = "qd"

    automato = AFD(estados, alfabeto, transicoes, "q0", finais, token)

    automato.rotulos = {
        nome: f"leu {prefixo!r}" for prefixo, nome in nomes.items()
    }
    automato.rotulos["q0"] = "inicial"
    automato.rotulos["qd"] = "erro"

    return automato
