# Questão 2
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

# Definir o número para verificação
numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

# Verificar se o número pertence à sequência de Fibonacci e exibir o resultado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
