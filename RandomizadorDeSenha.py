from random import choice
characters = ("abcdfghijklmnopqrstuvwxyz0123456789")
quantidade = int(input("Digite a quantidade de characteres : "))
senha = ''

for i in range(quantidade):
    senha += choice(characters)

print(f'Senha gerada "{senha}" ')
