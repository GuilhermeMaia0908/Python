#estruturas condicionais permitem que o programa execute blocos de códigos diferentes dependendo de uma condição. A condição é sempre avaliada como true ( Verdadeiro ) False (FALSO)

# se o usuário tiver a idade maior que 18 ele poderá entrar. 
idade_usuario = 20 #Hardcode
# if idade_usuario > 18:
#     print("O usuario pode acessar o local.")

# if idade_usuario > 18:
#     print("O usuario Pode Acessar o Local.😏")
# else:
#     print("Entrada Proibida seu boboca🤤")

nota = int(input("Digite a nota do aluno: "))
# nota maior ou igual a 90, "Aprovado com nota excelente."
# nota for maior ou igual a 70, "Aprovado."
# Qualquer outra nota será exibido como "Reprovado". 

if nota >= 90:
    print("😎 Aprovado com beijos 😘BB.")
elif nota >= 70:
    print("👍Aprovado seu BETA")
else: 
    print("REPROVADO SEU BAITOLA😮")