# Neste desafio de projeto, você desenvolverá um programa de consulta de CPF do usuário. 
# Seu código precisa utilizar uma biblioteca especial para saber se os números 
# que o usuário digitou são de um CPF verdadeiro.

require 'cpf_cnpj'

def consulta_cpf
    print "Digite o CPF para consulta: "
    cpf = gets.chomp.gsub(/\D/, '') # Remove caracteres não numéricos
  
    if CPF.valid?(cpf)
      puts "CPF válido."
    else
      puts "CPF inválido."
    end
  end
  
  consulta_cpf