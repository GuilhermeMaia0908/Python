sabores_pizza = ["Mussarela", "Calabresa", "Peperoni", "Quatro Queijos", "Frango com Catupiry",
"Portuguesa"]

print("Faça seu pedido(digite 'sair' para encerrar):")

pizza = ""

while pizza.capitalize() != "Sair":
    pizza = input("Escolha um sabor: ").capitalize()

    if pizza in sabores_pizza:
        print(f'{pizza} foi adicionado a sua compra 😊')

    elif pizza.capitalize() != "Sair":
        print("Esse sabor não está no cardápio, escolha outro:")
    else:
        print("Pedido encerrado!")