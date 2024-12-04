#interface que vai adaptar nosso jogo

from sistema import gerar_numero_secreto, verificar_tentativa

def jogar():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = gerar_numero_secreto()
    tentativas = 10

    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes.")
        tentativa = int(input("Digite um número entre 1 e 50: "))

        mensagem = verificar_tentativa(numero_secreto, tentativa)
        print(mensagem)

        if mensagem == "Parabéns! Você acertou!":
            break
        
        tentativas -= 1

    if tentativas == 0:
        print(f"Que pena! O número secreto era {numero_secreto}.")

jogar()
