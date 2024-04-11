"""
PEP8- Python Enhancement Proposal
São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia do pep8 é que  podemos escrever python de forma pythonica
[1] - utilize camel case para nomes de classes.

    class Calculadora:
      pass

    class CalculadoraCientifica:
      pass

[2] - Utilize nomes em minusculos separados por underline em funções. 
      
      def soma():
        pass

      def soma_dois():
        pass
        
[3] - Uttilize 4 espaços para identação!!!

if 'a' in 'laranja':
    print('tem')

[4]- Linhas em branco (2)

    class Classe:
      pass


    class Outra:
      pass
      

[5]  - Imports

Imports devem ser feitos sempre em linhas separadas.
# ERRADO: import sys,os

# CERTO: import sys
         import os
NÃO HÁ PROBLEMAS EM UTILIZAR
from types import, Stringtypes, ListType.

CASO TENHA MUITOS IMPORTS DE UMAA MESMO PACOTE, RECOMENDA-SE FAZER:

from type import{
    StringType
    ListType
    OutroType..
}

IMPORTS DEVEM SER  COLOCADOS NNO TOPO DO ARQUIVO, LOGO DEPOIS DE QQUISQUER COMENTARIO OU DOCSTRINGS
E ANTES DE CONSTANTES OU VARIAVEIS GLOBAIS. 


[6]- ESPAÇOS  EM EXPREÇÕES E INSTRUÇÕES

NÃO FAÇA

funcao( algo[ 1 ] { outro: 2 })

 FAÇA

funcao(algo[1], {outro:2})

""" 


