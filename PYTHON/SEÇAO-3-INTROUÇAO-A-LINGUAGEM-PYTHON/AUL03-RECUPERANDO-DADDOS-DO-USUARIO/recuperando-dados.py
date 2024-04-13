"""
RECEBENDO DADOS DO USUARIO

input -> todo dado recebido via input é do tipo string.
Em Python string é tudo que estiver entre
- Aspas simples  
- Aspas dupas
- Aspas simples  triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Tiago Soares'
- Aspas duplas -> "Tiago Soares"
- Aspas simples triplas -> '''Tiago Soares'''

"""
#- Aspas duplas triplas -> """Tiago Soares"""

#ENTRADA DE DADOS

#print("Qual o seu nome?")
#nome = input()
nome = input('Quaal o Seu nome?')

#print("Qual a sua idade?")
#idade = input()
idade = int(input('Qual sua idade?'))

#Exemplo de prinntt annttigo (versãao 2x)
#print("Seja bem-vindo(a) %s" %nome)

#Exemplo de print 'moderno' (versãao 3x)
#print('Seja bem-vindo(a) {0}' .format(nome))

#Exemplo de print mais atual (versãao 3.7)
print(f'Seja bem-vindo(a) {nome}')

#PROCESAMENTO

#SAIDA DE DADOS
#Exemplo de print annttigo (versãao 2x)
#print("A %s tem %s anos" %(nome, idade))

#Exemplo de print 'moderno' (versãao 3x)
#print('A {0} tem {1} anos' .format(nome, idade))
"""
int(idade) => cast
cast é 'A conversão de um tipo de dado para outro'
"""
print(f"A {nome} nasceu em {2024 - int(idade)}")