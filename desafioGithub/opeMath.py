# Solicita dois números como entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a subtração considerando o maior número primeiro
subtracao = abs(num2 - num1)

# Realiza as operações restantes
soma = num1 + num2
multiplicacao = num1 * num2

# Verifica se o segundo número é diferente de zero antes de realizar a divisão
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero."

# Imprime os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
