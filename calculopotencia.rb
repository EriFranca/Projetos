# Neste desafio de projeto, 
# você criará um array vazio para que o usuário insira até 3 números 
# e o final apareça o resultado desses 3 números elevados a 3ª potência.
potencia = []
3.times do |i|
  print "Informe o #{i+1}º número: "
  numero = gets.chomp.to_i
  potencia << numero
end

resultado = potencia.map { |num| num ** 3 }.sum
puts "O resultado é: #{resultado}"