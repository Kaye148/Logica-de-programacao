print("""
    codigo \t prato \t\t\t valor
      1 \t picanha \t\t R$ 25
      2 \t lasanha \t\t R$ 20
      3 \t strgonoff \t\t R$ 18
      4 \t Bife Acebolado \t R$ 15
      5 \tPão com ovo \t\t R$ 5
""")

codigo = int(input("digite o codigo do prato desajedo: "))

match codigo:
     
    case 1:
        prato = "picanha"
        preco = 25
    case 2:
        prato = "lasanha"
        preco = 20
    case 3:
        prato = "Strogonoff"
        preco = 18
    case 4:
        prato = "Bife Acebolado"
        preco = 15
    case 5:
        preco = "Pão com ovo"
        preco = 5
  