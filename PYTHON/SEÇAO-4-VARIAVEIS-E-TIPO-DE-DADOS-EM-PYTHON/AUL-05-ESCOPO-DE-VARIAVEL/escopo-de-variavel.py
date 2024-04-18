"""
ESCOPO DE VARIAVEL

Dois casos de escopo:

- Variaveis globais:
Seu escopo compreende todo o programa.
- Variaveis locais
São reconhecidas apenass onde foram declaradas, ou seja, seu escopo esta limitado
onde a variavel foi declarada.

Para declarar variaveis em Python fazemos:
Nome_da_variavel = Valor_da_variavel

Python é uma linguagem de tipagem dinâmica
ao declararmos uma variavel, não colocaamos o tipo de dado  dela.
Este tipo è inferido ao atribuirmos o valor a variavel 

Exemplo en c:
int numero = 42;
"""

numero = 42 # Variavel global
print(numero)
print(type(numero))

numero = 'Tiago' #  REATRIBUIÇÃO
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 23


if numero > 10:
    novo = numero + 10 # A Vriavel 'novo' é uma variavel local
    print(novo)

print(novo)