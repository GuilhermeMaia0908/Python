"""
Crie um Programa que simule um caixa eletronico. O usuario pode sacar valores até o saldo disponivel ou até ele digitar "sair"
- Comece com um saldo inicial de 500 reais 
- peça ao usuario digitar o valor para SAQUE
- se o valor for maior que o saldo, avise que não a saldo suficiente 
- se o usuario digitar "sair", encerre o programa
"""

saldo = 500

while saldo > 0: #Ira continuar até ser false  (ACABAR O SALDO ) ou digitar 'sair'
    print(f' \n 💴 Saldo disponivel: R$:{saldo:.2f}') #\n quebra a linha
    saque = input("💵Digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair":  # Metodo lower() transforma a string em minuscula 
        print("🏧 Operação encerrada!")
        break
    saque = float(saque)
    if saque > saldo:
        print(" ❌ saldo insuficiente!")
    else:
        # saldo = saldo - saque
        saldo -= saque 
        print(f"Saque de R${saque:.2f}realizado com sucesso!")