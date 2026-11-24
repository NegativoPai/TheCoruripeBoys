# Mini-linguagem Coruripe

Especificação das regras léxicas. O código e o relatório seguem este arquivo.
Mudança aqui precisa ser combinada no grupo antes de ser commitada.

## Palavras-chave

    se  senao  var  fim

Quatro palavras, todas minúsculas e sem acento. `SE` e `Se` são identificadores.

A quantidade foi escolhida de propósito. O AFD de palavras-chave é uma trie, onde
cada prefixo distinto vira um estado: estas quatro dão **13 estados**, que cabem
num diagrama legível e numa tabela que não estoura a margem da página.

`se` e `senao` compartilham prefixo de propósito — é isso que dá passos reais ao
algoritmo de minimização.

## Identificadores

Começa com letra ou `_`, seguido de zero ou mais letras, dígitos ou `_`:

    (letra | _) (letra | dígito | _)*

Sem acento e sem cedilha. A restrição mantém o alfabeto em 63 símbolos, o que
permite agrupar a tabela de transição em duas colunas em vez de 63.

## Números

**Inteiro:** `0`, ou um dígito de 1 a 9 seguido de zero ou mais dígitos.

    0 | [1-9][0-9]*

**Float:** um inteiro, um ponto, e pelo menos um dígito depois.

    INTEIRO . [0-9]+

Três decisões e os motivos:

- **Zero à esquerda não vale.** `007` é inválido. Custa um estado a mais no AFD.
- **O sinal não faz parte do número.** `-5` é o operador `-` seguido do inteiro
  `5`. Se `+1` fosse um inteiro válido, `a+1` teria duas leituras e a tokenização
  deixaria de ser única — que é a propriedade que um analisador léxico existe para
  garantir. Compiladores reais resolvem igual: o sinal é tratado na sintaxe.
- **O ponto exige dígito dos dois lados.** `.5` e `5.` são inválidos.

## Operadores

    +  -  *  /  %  =  ==  !=  <  <=  >  >=

Doze operadores, quatro deles com dois caracteres. Isso é intencional: `<=` e `<`
só podem ser distinguidos pela regra de casamento mais longo, o que torna a regra
necessária em vez de decorativa.

O símbolo `!` só existe dentro de `!=`. Sozinho é erro.

## Delimitadores

    (  )  ;  ,

Não há chaves. O bloco do `se` é fechado por `fim`.

## Regras de desambiguação

Mais de uma classe pode casar na mesma posição. A ordem abaixo resolve, e é o que
garante que a tokenização seja única.

**R1 — Casamento mais longo.** Vence o token de maior comprimento a partir da
posição atual. Por isso `>=` é um operador só e não `>` seguido de `=`; `1.5` é um
FLOAT e não o inteiro `1` seguido de `.` e `5`; e `sentinela` é um identificador e
não a palavra-chave `se` seguida de `ntinela`.

**R2 — Prioridade no empate.** Quando duas classes casam com o mesmo comprimento,
vale esta ordem:

    PALAVRA_CHAVE  IDENTIFICADOR  FLOAT  INTEIRO  OPERADOR  DELIMITADOR

É o que faz `se` ser palavra-chave, já que casa com as duas primeiras classes com
dois caracteres em ambas.

**R3 — Falha.** Quando nenhuma classe casa, é erro léxico, reportado com linha e
coluna.

## O que a linguagem não aceita

| Entrada | Motivo |
|---|---|
| identificador com acento | acentos e cedilha estão fora do alfabeto |
| `007` | zero à esquerda não é permitido |
| `-5` como token único | o sinal é operador, não faz parte do literal |
| `.5` e `5.` | float exige dígito dos dois lados do ponto |
| `!` isolado | `!` só existe dentro de `!=` |
| `"texto"` | literais de string estão fora do escopo |
| comentários | fora do escopo |
| `{` e `}` | não há chaves; o bloco fecha com `fim` |

## Alfabeto

União dos alfabetos de todos os AFDs: 52 letras, 10 dígitos, `_`, `.`, os nove
símbolos de operador (`+ - * / % = ! < >`) e os quatro delimitadores. São 77
símbolos, mais os brancos (espaço, tabulação, quebra de linha), que separam tokens
sem gerar token.

Cada AFD usa apenas o subconjunto que lhe interessa.

## Convenção de nomes dos estados

`q0` é o estado inicial, `q1`, `q2`, ... os demais, e `qd` o estado de erro.

Esta convenção permite que a definição formal e os diagramas sejam escritos em
paralelo sem divergir.

## Tamanho de cada autômato

| Classe | Estados | Símbolos | Transições |
|---|---|---|---|
| PALAVRA_CHAVE | 13 | 10 | 130 |
| IDENTIFICADOR | 3 | 63 | 189 |
| INTEIRO | 4 | 10 | 40 |
| FLOAT | 6 | 11 | 66 |
| OPERADOR | 15 | 9 | 135 |
| DELIMITADOR | 6 | 4 | 24 |

A coluna de transições é `estados × símbolos`, porque δ é **função total**: existe
transição definida para todo par (estado, símbolo), sem exceção. É isso que o
estado `qd` garante.

Estes números são conferidos automaticamente por `testes/teste_validacao.py`. Se
um AFD mudar e esta tabela não for atualizada, o teste falha.

## Programa de exemplo

O arquivo `exemplos/programa.crp` contém:

    var sentinela = 0;
    var taxa = 1.5;
    se sentinela >= 10
      var limite = (sentinela + 1) * 2;
    senao
      var limite = 0;
    fim

Produz 32 tokens. Foi montado para exercitar as três regras de desambiguação de
uma vez: `sentinela` contra `se` (R1 derrubando a prioridade), `se` sozinho (R2
aplicando a prioridade), `>=` contra `>` (R1 no operador) e `1.5` contra `1` (R1
no literal).
