import random

print("Bem-vindo(a) ao jogo de adivinhação!")

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

    print(f"\nEu pensei em um número de 1 a {limite}...")

    while True:
        chute = int(input("Qual é teu chute? "))
        tentativas +=1

        if chute < numero_secreto:
            print("Muito baixo! Tenta de novo!")

        elif chute > numero_secreto:
            print("Muito alto! Tenta de novo!")

        else:
            print(f"ACERTOU!!! em {tentativas} tentativas!")
            break
    
    jogar_de_novo = input("Quer jogar de novo? (s/n)").lower()

    if jogar_de_novo != "s":
        print("Valeu por jogar!")
        break