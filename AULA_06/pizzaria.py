dia = input("Dia da semana: ").lower()
valor = float(input("Valor do pedido: R$ "))
valor_final = valor 
frete_gratis = False 

if dia == "terça" and valor > 40:
    print(f"Você ganhou uma sobremesa de graça🍧")
elif dia == "quinta":
    valor_final = valor_final - (valor_final * 0.15)
    print(f"Você ganhou 15% de desconto na pizza")
elif (dia == "sabado" or dia == "domingo") and valor > 100 :
    frete_gratis = True
    print(f"Você ganhou frete gratis!")

elif frete_gratis == False :
    valor_final = valor_final + 6
else:
    print ("Sem Promoção!")
if frete_gratis == False :
    valor_final = valor_final + 6 
    print (f"Total a Pagar será 💵R$:{valor_final:.2f}")