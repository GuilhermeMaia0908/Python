# Primeira função, calcular_preco_pizza()
def calcular_preco_pizza(tamanho):
  tabela = {"P": 25.0, "M": 35.0, "G": 45.0,}
  "Para receber o value você acessa o key"
  return tabela.get(tamanho,0)
  "tabela.get() é um forma segura de acessar valores no dict"
  ".get(tamanho,0) evita retorno None se a chave não existir"

# Segunda função, calcular_taxa_entrega()
def calcular_taxa_entrega(distancia_km):
  if distancia_km <= 3:
    return 5.0
  elif distancia_km <= 7:
    return 10.0
  else:
    return 15.0
 
# Terceira função, aplicar_desconto_fidelidade()
def aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel):
  if eh_cliente_fiel:
    return subtotal * 0.90 
  return subtotal  

def fechar_pedido(tamanho, distancia_km, eh_cliente_fiel): 
  "Essa função REUTILIZA todas as funções anteriores"
  preco_pizza = calcular_preco_pizza(tamanho)
  taxa = calcular_taxa_entrega(distancia_km)
  subtotal = preco_pizza + taxa
  total = aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel)
  
  print(f"Pizza ({tamanho}): R$ {preco_pizza:.2f}")
  print(f"Taxa de entrega: R$ {taxa:.2f}")
  print(f"Total: R$ {total:.2f}")
  print("-" * 30)
  

fechar_pedido("G", 5, True)