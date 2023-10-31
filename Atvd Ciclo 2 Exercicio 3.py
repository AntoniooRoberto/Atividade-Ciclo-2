def encontrar_menor_numero(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor
def main():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    menor = encontrar_menor_numero(a, b, c)
    print(f"O menor número entre {a}, {b} e {c} é {menor}.")

if __name__ == "__main__":
    main()