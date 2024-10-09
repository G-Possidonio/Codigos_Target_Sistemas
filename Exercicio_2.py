#Exercíco 2: Resolvido

palavra = input("Digite uma palavra: ")
letraMinuscula = 0
letraMaiuscula = 0

if 'a' in palavra or 'A' in palavra:
    print('\nExiste a letra a ou A na palavra digitada pelo usuário \n')
    
for letra in palavra:
    if letra == 'a':
        letraMinuscula += 1
    elif letra == 'A':
        letraMaiuscula += 1

print(f'A palavra: {palavra}, possuí: ')
print(f'{letraMinuscula} letra(s) (a) mínuscula(s) e {letraMaiuscula} letra(s) maiscula(s)')