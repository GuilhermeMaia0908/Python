def calcular_preco_pizza(sabor, tamanho, borda_recheada=False):
    "Calcula o preço final de uma pizza com opções."
    tabela = {
        "P": 25.0,
        "M": 35.0,
        "G": 45.0,
    }


    preco = tabela[tamanho]

    if borda_recheada:
        preco = preco + 8
        preco += 8.0
        print(f"""A pizza de {sabor} 
        e o tamanho é {tamanho}
        a borda é recheada ?{borda_recheada}
        O preço final é R${preco}
""")
    return preco, sabor


calcular_preco_pizza("Frango","G", )
    # sabores = {
    #     "Pepperoni": 50,
    #     "Maravilha": 25,
    #     "Galeto": 10,
    # }
    # sabor_pizza = sabores[sabor]

   