valor_produto = f(input("digite o valor do produto: "))

print("""
1 - à vista
2 - à prazo
""")

forma_de_pagamento = int(input("digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
        # obtendo o valor do desconto de 10%
        desconto = valor_produto * 0.10
        valor_com_desconto = valor_produto - desconto

        print(f"\nvalor do produto: {valor_produto}")
        print("formade pagamento: à vista")
        print(f"valor do desconto: {desconto}")
        print(f"valor a pagar: { valor_com_desconto}")

    case 2:
            quantidade_de_parcelas = int(input("digite a quantidade de parcelas: "))
        
            if quantidade_de_parcelas >= 1 and quantidade_de_parcelas <=6:
                 valor_da_parcela = valor_produto / quantidade_de_parcelas 

