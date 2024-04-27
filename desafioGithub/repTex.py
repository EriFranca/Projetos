# Recebe a string e o número inteiro do usuário
entrada_string = input("Digite uma string: ")
entrada_numero = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = entrada_string * entrada_numero

# Imprime o resultado
print("A string repetida {} vezes é: {}".format(entrada_numero, resultado))
