# sabores = ["Mussarela", "Calabresa", "Pepperoni", "Quatro Queijos", "Frango com Catupiry"]

# print("Sabores disponíveis na Pizzaria Sabores:")
# for sabor in sabores:
#     print(f"- {sabor}")

# print("Preparando sua pizza...")
# for minuto in range (1,6):
#     print(f"🕛{minuto} minuto(s) se passou...")

# print ("Sua pizza está pronta! Bom apetite!")

# clientes = ["João", "Maria", "Carlos", "Ana", "Pedro"]

# print("Atendendo clientes: ")
# for i, cliente in enumerate (clientes):
#     if i == 3:
#         print ("Capacidade maxima atingida. Não podemos atender mais clientes no momento.")
#         break
#     print(f"atendendo {cliente}...") 

pedidos = ["Mussarela", "cancelado", "Calabresa", "cancelado", "Pepperoni"]

for pedido in pedidos:
    if pedido == "cancelado":
        continue  # pula este e vai para o próximo
    print(f"Preparando pizza de {pedido}...")