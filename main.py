import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")

    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10  # Número máximo de tentativas

    while tentativas < max_tentativas:
        try:
            # Receber o palpite do jogador
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            # Verificar o palpite
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break

        except ValueError:
            print("Por favor, digite um número válido.")
    
    else:
        print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")

# Iniciar o jogo
if __name__ == "__main__":
    jogo_adivinhacao()
