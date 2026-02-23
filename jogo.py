import random

print("Bem-vindo(a) ao jogo de adivinhação!")

melhor_recorde = None

while True:

    print("\nEscolhe a dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)")

    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == "1":
        limite = 10
    elif escolha == "2":
        limite = 50
    elif escolha == "3":
        limite = 100
    else:
        print("Opção inválida, vou colocar no fácil 😅")
        limite = 10

    numero_secreto = random.randint(1, limite)
    tentativas = 0 
    vidas = 5

    print(f"\nEu pensei em um número de 1 a {limite}...")
    print("Tu tem 5 vidas❤️")


    while vidas > 0:
        try:
         chute = int(input("Qual é teu chute? "))
        except:
         print("Digita um número válido😅")
         continue
       

        tentativas += 1
        vidas -= 1

        if chute < numero_secreto:
            print("Muito baixo! Tenta de novo!")

        elif chute > numero_secreto:
            print("Muito alto! Tenta de novo!")

        else:
            print(f"ACERTOU!!! em {tentativas} tentativas!")

            if melhor_recorde is None or tentativas < melhor_recorde:
                melhor_recorde = tentativas
                print("Novo recorde!")
        
            break
    
        print(f"Vidas restantes: {vidas} ❤️")

    else:
        print(f"💀 Suas vidas acabaram! o número era {numero_secreto}")

    if melhor_recorde:
        print(f"Melhor recorde até agora: {melhor_recorde} tentativas")
    
    jogar_de_novo = input("Quer jogar de novo? (s/n)").lower()

    if jogar_de_novo != "s":
        print("Valeu por jogar!")
        break