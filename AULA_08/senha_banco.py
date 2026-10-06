"""
Crie um sistema que peça ao usuario para digitar uma senha para acessar sua conta bancária.Ele tem *APENAS 3 TENTATIVAS* Para acertar a senha. Se ele errar as 3 tentativas, o sistema bloqueia a conta.
- A senha correta será : 40028922;
- O usuario tem 3 tentativas Input();
- Errou 3 vezes conta bloqueada 
"""


SENHA_CORRETA = "40028922" #constante, boa prática em python
tentativas = 3 #Uma variavel contadora, pode ser i ou j

while tentativas > 0:
    senha = input("Digite a sua senha: ") # Variavel Local
    if senha ==  SENHA_CORRETA:
        print("🔓 ACESSO PERMITIDO! ")
        break # Comando onde finaliza o Loop
    else:
        tentativas -= 1  # tentativas = tentativas - 1
        print(f'Senha Incorreta😮. Tentativas Restantes: {tentativas} ')

    if tentativas == 0: 
        print("🔒Conta Bloqueada! ")        