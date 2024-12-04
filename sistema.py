#sistema principal do jogo

import random

def gerar_numero_secreto():
    return random.randint(1, 50)

def verificar_tentativa(numero_secreto, tentativa):
    if tentativa < numero_secreto:
        return "O número secreto é maior!"
    elif tentativa > numero_secreto:
        return "O número secreto é menor!"
    else:
        return "Parabéns! Você acertou!"
