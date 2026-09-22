FRETE = 2
dia_semana = "Sabado"

print(f"""
        ========================================
        ========================================
       
        SEJA BEM VINDO A PIZZARIA PIPOCO RJ🍕😏

        ========================================
        ========================================

      """)
nome_cliente = input(f""" 
        🤤Digite o seu nome:
""")
pizza_sabor = input(f""" 

        🍕Escolha uma das opções abaixo😏:
            1- PARA Frango com requeijão
            2- PARA Calabresa
            3- PARA mussarela 
            4- PARA banana nevada
        
        """)
pizza_tamanho = input(f""" 
        😮Escolha o tamanho da PIZZA:
            1- Pequeno
            2- Medio
            3- Grande
""")
forma_entrega = input(f"""
            🛵
              ESCOLHA A FORMA DE ENTREGA:
            1- Consumo Local
            2- Entrega na Residêcia 
""")
if dia_semana == "Sabado":
    print(f" 🍕🤤 Pedido aceito com sucesso!" )
    print(f" O refri é por nossa conta chefe 😘")
elif dia_semana == "Domingo":
    print(f" 🍕🤤 Pedido aceito com sucesso!" )
    print(f" O FRETE e o Refri por nossa conta chefe 😘")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
    print(f" 🍕🤤 Pedido aceito com sucesso!" )
    print(f" O frete hoje é por conta nossa conta bb 😘")

# print(f"""
#      ============================================
#                 RESUMO DO PEDIDO
#             😎NOME DO BETA:{nome_cliente}
#             😮SABOR DA PIZZA: {pizza_sabor}
#             😏TAMANHO DA PEÇA: {pizza_tamanho}
#             🛵FORMA DE ENTREGA: {forma_entrega}
#      ============================================
# """)
#Estrutura condicional para promoção
#comprando qualquer pizza e qualquer tamanho no sabádo, o refir é gratuito
#Comprando uma pizza de calabresa no tamanho médio em qualquer dia, o frete é gratis 
#Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri é gratis 

