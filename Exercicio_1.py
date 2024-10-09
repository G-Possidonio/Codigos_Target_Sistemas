#Exercicio 1: Resolvido

def sequencia_fibonacci(n):
    seq = []
    a, b = 0, 1
    while a <= n:
        seq.append(a)
        a, b = b, a + b
    return seq

def pertence_a_fibonacci(n):
    if n < 0:
        return False
    seq = sequencia_fibonacci(n)
    return n in seq

# Exemplo de uso
numero = int(input("Digite um número: "))
if pertence_a_fibonacci(numero):
    print()
    print(f"O número {numero} pertence à sequência de Fibonacci.")
    print(sequencia_fibonacci(numero))
else:
    print()
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    print(sequencia_fibonacci(numero))