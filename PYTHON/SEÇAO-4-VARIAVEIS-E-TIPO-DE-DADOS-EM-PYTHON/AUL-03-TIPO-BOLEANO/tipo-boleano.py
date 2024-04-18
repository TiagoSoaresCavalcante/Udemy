""""
TIPO BOOLEANO
Algebra bolena criadaa por George Boolean

True - Verdadeiro
False - Falso
SEMPRE INICIADAS COM LETRAS MAIUSCULAS.
"""
ativo  = False
logado = False
print(ativo)

"""
OPERAÇÕES BASICAS
- NEGAÇÃO  (not) -> Se Falso o retorno sera Verdadeiro
             Se Verdadeiro o retorno sera Falso
"""

print(not ativo)

"""
- OU (or) -> Verdadeiro se um dos valores forem Verdadeiros
- True or True -> True
- True or False -> True
- False or true -> True
- False or false -> False
"""
print (ativo or logado)

"""
E (and) -> Verdadeiro se  todos forem Verdadeiros

- True and True -> True
- True and False -> False
- False and true -> False
- False and false -> False
"""