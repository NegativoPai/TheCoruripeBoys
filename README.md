# TheCoruripeBoys

Analisador léxico (scanner) para a mini-linguagem **Coruripe**, desenvolvido na
disciplina de Linguagens Formais e Autômatos Finitos — 6° Período.

O projeto reconhece seis classes de token — palavras-chave, identificadores,
inteiros, floats, operadores e delimitadores — cada uma modelada por um autômato
finito determinístico, e integra todas num analisador que tokeniza um programa
completo resolvendo ambiguidades por casamento mais longo.

As regras da linguagem estão em [docs/especificacao.md](docs/especificacao.md).

## Colaboradores

<div align="center">

Aluno|Matrícula|GitHub
|-----|-----|-----
João Manoel da Silva Santos|01695227|[NegativoPai](https://github.com/NegativoPai)
William Ângelo Ribeiro Santos|01689685|[williamalcai](https://github.com/williamalcai)
Ivan Pedro Batista Dos Santos|01754726|[IvanDev404](https://github.com/IvanDev404)
Thallys Deryck Azevedo da Silva|01717160|[Thallys013](https://github.com/Thallys013)
Edison Campos Cavalcante|01704611|[EdisonC-Dev](https://github.com/EdisonC-Dev)
José Gustavo Tenório Guimarães|01698878|[Gustavo9291](https://github.com/Gustavo9291)

</div>

## Funções

Quem coordena e integra cada área do trabalho.

<div align="center">

Função|Responsável
|-----|-----
Especificação da mini-linguagem|Todos
Definição formal e tabela de transições|[williamalcai](https://github.com/williamalcai)
Diagramas dos AFDs em TikZ|[IvanDev404](https://github.com/IvanDev404)
Minimização e seções teóricas|[Gustavo9291](https://github.com/Gustavo9291)
Simulador em Python e casos de teste|[NegativoPai](https://github.com/NegativoPai)
Montagem do relatório em LaTeX|[EdisonC-Dev](https://github.com/EdisonC-Dev)
Montagem dos slides em Beamer|[Thallys013](https://github.com/Thallys013)

</div>

## Seções do relatório

Cada integrante escreve pelo menos uma seção do relatório no Overleaf, de forma
que todos produzam texto em LaTeX. Cada seção tem um único autor, o que evita
conflito de edição no mesmo arquivo.

<div align="center">

Arquivo|Seção|Autor
|-----|-----|-----
`secoes/01-introducao.tex`|Introdução|[EdisonC-Dev](https://github.com/EdisonC-Dev)
`secoes/02-linguagem.tex`|A Mini-Linguagem|[Thallys013](https://github.com/Thallys013)
`secoes/03-definicao-formal.tex`|Definição Formal dos Autômatos|[williamalcai](https://github.com/williamalcai)
`secoes/04-diagramas.tex`|Diagramas de Transição|[IvanDev404](https://github.com/IvanDev404)
`secoes/05-minimizacao.tex`|Minimização|[Gustavo9291](https://github.com/Gustavo9291)
`secoes/06-implementacao.tex`|Implementação|[NegativoPai](https://github.com/NegativoPai)
`secoes/07-conclusao.tex`|Conclusão|[NegativoPai](https://github.com/NegativoPai)

</div>

O documento principal `relatorio.tex`, o preâmbulo e a integração das seções são
responsabilidade de [EdisonC-Dev](https://github.com/EdisonC-Dev).

## Estrutura

```text
docs/         regras da mini-linguagem
exemplos/     programas de exemplo em Coruripe
geradas/      saída de script, não editar à mão
simulador/    classe AFD, os seis autômatos e o scanner
testes/       suíte de testes
```

## Como executar

Todos os comandos rodam a partir da raiz do repositório.

Analisar um arquivo:

```bash
python -m simulador.main exemplos/programa.crp
```

Modo interativo, uma linha por vez:

```bash
python -m simulador.main
```

Rodar a suíte de testes completa:

```bash
python -m testes.rodar_todos
```

Rodar um teste isolado:

```bash
python -m testes.teste_scanner
```

## Ferramentas de apoio

Três scripts geram material para o relatório a partir dos próprios autômatos, de
modo que o texto não possa divergir da implementação.

Descrever os AFDs — conjuntos, significado de cada estado e tabela de transição:

```bash
python -m simulador.descrever
```

Aplicar o algoritmo de minimização e imprimir os passos:

```bash
python -m simulador.minimizar
```

Gerar as tabelas de transição em LaTeX em `geradas/tabelas.tex`:

```bash
python -m simulador.tabela_latex
```
