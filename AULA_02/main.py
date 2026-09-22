# Declaração de Variáveis
# NOME DO USUARIO
CPF = 123456  # Constante, boa prática.
nome_do_usuario = "Guilherme" # string
idade_do_usuario = 20 # number (int)
altura_do_usuario = 1.70 # number (float)
possui_cnh = True # boolean (True ou False)

# Exibição de dados 
# print(f"O usuário tem o nome {nome_do_usuario}")
print(f"""
        DADOS DO USUÁRIO
      ========================
        😎 NOME: {nome_do_usuario}
        👍 IDADE: {idade_do_usuario}
        😏 ALTURA: {altura_do_usuario}
      ========================
 """)
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")