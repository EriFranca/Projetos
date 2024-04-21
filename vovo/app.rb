
require_relative 'produto'
require_relative 'loja'
 
produto = Produto.new
    produto.nome = 'Tomate'
    produto.preco = 2.50

produto1 = Produto.new
    produto1.nome = 'Bolo de cenoura'
    produto1.preco = 50.00
 
Mercado.new(produto.nome, produto.preco).comprar
Mercado.new(produto1.nome, produto1.preco).comprar