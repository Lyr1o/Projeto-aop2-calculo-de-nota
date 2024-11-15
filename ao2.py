#Lista para informaçoes dos alunos
alunos = []

#A quantidade de alunos (em porcentagem) que foram: Aprovado ou Reprovado;
num_aprovados = 0
num_reprovados = 0

# Loop para ler informações de 100 alunos
    #Para realizar o teste com 5 alunos favor colocar (1, 6)
for i in range(1, 101):
    print(f"Informações do aluno {i}:")
    nome = input("Digite o nome do aluno: ")

    aop1 = -1
    aop2 = -1
    aop3 = -1
    prova_regular = -1
    prova_de_recuperação = -1


          #LER DO USUÁRIO: Nota [0, 1] na AOP1: Atividade Online Pontuada 1;
    while aop1 < 0 or aop1 > 1:
        aop1 = float(input("\nDigite a nota da aop1: "))

        if aop1 < 0 or aop1 > 1:
            print("Digite um número válido entre 0-1.")

          #LER DO USUÁRIO: Nota [0, 2] na AOP2: Atividade Online Pontuada 2;
    while aop2 < 0 or aop2 > 2:
        aop2 = float(input("Digite a nota da aop2: "))

        if aop2 < 0 or aop2 > 2:
            print("Digite um número válido entre 0-2.")

          #LER DO USUÁRIO: Nota [0, 1] na AOP3: Atividade Online Pontuada 3;
    while aop3 < 0 or aop3 > 1:
        aop3 = float(input("Digite a nota da aop3: "))

        if aop3 < 0 or aop3 > 1:
            print("Digite um número válido entre 0-1.")

          #LER DO USUÁRIO: Nota [0, 6] da PROVA REGULAR;
    while prova_regular < 0 or prova_regular > 6:
        prova_regular = float(input("Digite a nota da prova: "))

        if prova_regular < 0 or prova_regular > 6:
            print("Digite um número válido entre 0-6.")


    soma_do_modulo = aop1 + aop2 + aop3 + prova_regular
    print(f"\nA soma do módulo (SM) é: {aop1} + {aop2} + {aop3} + {prova_regular} = {soma_do_modulo}")

    if soma_do_modulo >= 7.0:
        status = "Aprovado"
        num_aprovados += 1
        print(f"\nParabéns, {nome}! Você tirou {soma_do_modulo} e está aprovado.")

    else:
        print("\nVocê irá ter que realizar a prova de recuperação")


        while prova_de_recuperação < 0 or prova_de_recuperação > 10:
            prova_de_recuperação = float(input("Digite a nota da prova de recuperação: "))

            if prova_de_recuperação < 0 or prova_de_recuperação > 10:
                print("Digite um número válido entre 0-10.")
        media_do_modulo = (aop1 + aop2 + aop3 + prova_regular + prova_de_recuperação) / 2
        print(f"\nMédia do Módulo (MM) é: (({aop1} + {aop2} + {aop3} + {prova_regular} + {prova_de_recuperação}) / 2)= {media_do_modulo}")

        if media_do_modulo >= 5.0:
          status = "Aprovado"
          num_aprovados += 1

          print(f"\nParabéns, {nome}! Você tirou {media_do_modulo} e está aprovado.")

        else:
          status = "Reprovado"
          num_reprovados += 1
          print(f"\n{nome}, Você está reprovado com média {media_do_modulo}.")

    #informações do aluno
    aluno = {
             "nome": nome,
             "status": status
              }
    alunos.append(aluno)


print("\nInformações dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Status: {aluno['status']}")

total_alunos = len(alunos)
porcentagem_aprovados = (num_aprovados / total_alunos) * 100
porcentagem_reprovados = (num_reprovados / total_alunos) * 100

  #A quantidade de alunos (em porcentagem) que foram: Aprovado ou Reprovado;0
print(f"Quantidade de aprovados: {porcentagem_aprovados:.2f}%")
print(f"Quantidade de reprovados: {porcentagem_reprovados:.2f}%")
