""""
TIPO  STRING
Em Python um daado é considerado do tipo string sempre que:

- Estiver entre aspas simples
 'uma string', '234', 'a', 'True', '42.3'

 - Entre aspas duplas
 "uma string"," 234"," a", "True", "42.3"

- Entre aspas  simples triplas
'''uma string''',  '''234''', '''a''', '''True''',  ''' 42.3'''
"""
# - Entre aspas  duplas triplas
# """uma string""", """234""", """a""", """True""", """ 42.3"""

nome = 'Tiago Soares' 
print(nome)
print(type(nome))

nome = "Tiago Soares"
print(nome)
print(type(nome))

nome = '''Tiago Soares'''
print(nome)
print(type(nome))

nome = """Tiago Soares"""
print(nome)
print(type(nome))

"""
proxima linha
"""

nome = 'Tiago \nSoares'
print(nome)
print(type(nome))


nome = """Tiago 
Soares"""
print(nome)
print(type(nome))

"""
cractere de escape
"""
nome = "Tiago \" Soares"
print(nome)
print(type(nome))

"""
Todas as letras maiusculas
"""
nome = 'Tiago Soares' 
print(nome.upper())

"""
Todas as letras minusculas
"""
nome = 'Tiago Soares' 
print(nome.lower())


"""
Lista
"""
nome = 'Tiago Soares' 
print(nome.split())

"""
- Slice de string
[ 0,   1,   2,   3,    4,  5,  6,   7,    8,    9,  10,  11]
['T' ,'i', 'a', 'g',  'o, ' ', S', 'o',  'a',  'r' 'e', 's']
"""
nome = 'Tiago Soares' 
print(nome[0:5])
print(nome[6:11])


#[ 0,        1]
#[Tiago', 'soares']
print(nome.split()[0])
print(nome.split()[1])

"""
[::-1] -> COMECE DO 1º elmento, vá até o ultimo elemento e inverta 
"""
print(nome[::-1])

"""
Substituir uma letra por outra
"""
print(nome.replace('T', 'H'))
print(type(nome))

texto = "socorram me subino onibus em marrocos"
print(texto)
print(texto[::-1]) #texto palindromo