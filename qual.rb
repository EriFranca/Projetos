def verificar_whatsapp(numero)
    if /\(\d{2}\) \d \d{4}-\d{4}/.match(numero)
      puts "Meu Whatsapp é #{numero}"
    else
      puts "O número de Whatsapp fornecido não está no formato correto."
    end
  end
  
  # Exemplo de uso
  verificar_whatsapp("(99) 9 1234-5678")
  verificar_whatsapp("(99) 9 9876-5432")
  