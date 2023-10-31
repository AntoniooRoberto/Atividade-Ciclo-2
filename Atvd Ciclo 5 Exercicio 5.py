def inverter_letras_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = []

    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        palavras_invertidas.append(palavra_invertida)

    frase_invertida = " ".join(palavras_invertidas)
    return frase_invertida

frase_original = "Esta é uma frase de exemplo"
frase_invertida = inverter_letras_palavras(frase_original)
print(f"Frase original: {frase_original}")
print(f"Frase com palavras invertidas: {frase_invertida}")