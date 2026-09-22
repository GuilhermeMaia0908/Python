# distancia = float(input("Digite a distância em km: "))
# if distancia <= 5:
#     print("Frete: R$: 5,00")
# elif distancia <= 10:
#     print("Frete: R$: 10,00")
# else:
#     print("Não entregamos nesses guetos" )

distancia = float(input("Digite a distância em km: "))
taxa_fixa = 5.00

if distancia <= 6:
     valor_km = 1.00
elif distancia <= 10:
    valor_km = 2.00
else: 
    print ("Não entregamos nesses guetos feios ")
exit()

frete = taxa_fixa + distancia * valor_km
print(f"Valor do frete : R$ {frete}")