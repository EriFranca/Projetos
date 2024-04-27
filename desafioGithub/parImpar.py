def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita um número inteiro como entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar e imprime o resultado
print(f"O número {numero} é {verificar_par_ou_impar(numero)}.")
