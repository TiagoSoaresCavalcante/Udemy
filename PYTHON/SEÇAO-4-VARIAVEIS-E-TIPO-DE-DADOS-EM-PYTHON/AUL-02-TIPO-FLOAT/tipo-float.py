"""
tipo float
tipo reaal, decimal
casas decimais

obs: os separadores  de casas decimais na prrogramação é o ponto e não  virgula
"""

# Errado 
valor = 1, 44
print(valor) # É ENTENDIDO PELO PYTHON COMO TUPLA
print(type(valor))
valor = 1.44
print(valor)
print(type(valor))

# DUPLA ATRIBUIÇÃO
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#CONVERTER FLOAT PARA INT
"""
converendo valores float para inteiros perdemos precisâo
1.44 -> retorna 1
"""
res = int(valor)
print(type(res))

#NUMEROS COMPLEXOS
complexa = 5j
print(complexa)
print(type(complexa))
