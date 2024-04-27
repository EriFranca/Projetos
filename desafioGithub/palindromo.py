def eh_palindromo(palavra):
    # Converte a palavra para minúsculas para evitar diferenças de maiúsculas/minúsculas
    palavra = palavra.lower()
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    # Verifica se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Solicita uma palavra como entrada do usuário
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo e imprime o resultado
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
