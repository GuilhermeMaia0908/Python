pizzas = 0
faturamento = 0 
maior_venda = 0 
menor_venda = 0 
acima_50 = 0

while True:
    valor = float(input("Valor da pizza vendida(0 para encerrrar)R$ "))
    if valor == 0:
        break
    if valor < 0:
        print ("Valor invalido. Digite um valor positivo.")
        continue
    pizzas += 1
    faturamento += valor 
    if valor > maior_venda: # Na primeira venda ele é maior (valor)
        maior_venda = valor
    if pizzas == 1 or valor < menor_venda:
        menor_venda = valor 
    if valor > 50: 
        acima_50 += 1




if pizzas == 0:
    print ("Nenhuma venda registrada hoje.")
else:
    ticket_medio = faturamento / pizzas
    print("=== FECHAMENTO DO CAIXA ===")
    print(f"Total de pizzas vendidas: {pizzas}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Maior venda: R$ {maior_venda:.2f}")
    print(f"Menor venda: R$ {menor_venda:.2f}")
    print(f"Pizzas vendidas acima de R$ 50,00: {acima_50}")

# print (f" Esse foi o ultimo valor da variavel pizzas no while: {pizzas}")
# print (f" Esse foi o ultimo valor da variavel faturamento no while: {faturamento}") 
# print (f" esse é p valor da variavel valor (existe somente while){valor}")


# Verificar se o valor é 0 (encerrar o sistema e não contar como valor de pizza)
# Verificar se o valor é positivo ou não (Valor correto)

