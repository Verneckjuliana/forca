import random

def desenhar_forca(erros):
    partes_forca = [
        "   ____\n  |    |\n      |\n      |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n      |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n  |    |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|    |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n /     |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n / \\   |\n      |\n"
    ]
    return partes_forca[erros]

def escolher_palavra_e_dica():
    frutas = ["MAÇA", "BANANA", "MORANGO", "ABACAXI", "UVA", "PERA", "LARANJA", "PITAYA", "MANGA", "KIWI", "MELANCIA", "AMORA", "ABACATE"]
    indice = random.randint(0, len(frutas) - 1)
    palavra_secreta = frutas[indice]
    dica = dicas_frutas[palavra_secreta]
    return palavra_secreta, dica

def ocultar_letras(palavra, letras_corretas):
    oculto = ""
    for letra in palavra:
        if letra in letras_corretas:
            oculto += letra
        else:
            oculto += "_"
    return oculto

dicas_frutas = {
    "MAÇA": "É uma fruta vermelha e pode ser verde também.",
    "BANANA": "É uma fruta amarela e alongada.",
    "MORANGO": "É uma fruta pequena e vermelha.",
    "ABACAXI": "É uma fruta tropical com casca espinhosa.",
    "UVA": "É uma fruta pequena e redonda, pode ser roxa ou verde.",
    "PERA": "É uma fruta de forma arredondada, geralmente amarela ou verde.",
    "LARANJA": "É uma fruta cítrica e tem casca alaranjada.",
    "PITAYA": "É uma fruta que dá no cacto.",
    "MANGA": "É uma fruta que esta presente na sua camiseta.",
    "KIWI": "É uma fruta com pelinhos na casca.",
    "MELANCIA": "É uma fruta pesada",
    "AMORA": "Vou contar pro seu pai que você namora.",
    "ABACATE": "É uma fruta que faz a melhor vitamina do mundo."
}

letras_corretas = []
letras_erradas = []
tentativas = 6
acertou = False

print("Bem-vindo ao Jogo da Forca!")

palavra_secreta, dica = escolher_palavra_e_dica()
print("Dica:", dica)

while tentativas > 0:
    print(desenhar_forca(6 - tentativas))

    palavra_oculta = ocultar_letras(palavra_secreta, letras_corretas)
    print("Palavra: ", palavra_oculta)

    letra = input("Digite uma letra: ").upper()

    if letra in letras_corretas:
        print("Você já escolheu essa letra.")
        continue

    if letra in letras_erradas:
        print("Você já tentou esta letra e errou.")
        continue

    if letra in palavra_secreta:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print(f"Letra {letra} não encontrada. Você tem {tentativas} tentativas restantes.")
        print("Letras erradas:", letras_erradas)

    if set(letras_corretas) == set(palavra_secreta):
        acertou = True
        break

if acertou:
    print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
else:
    print("Você perdeu. A palavra era:", palavra_secreta)
    print(desenhar_forca(6 - tentativas))

