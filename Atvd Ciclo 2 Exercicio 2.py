def verifica_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def calcula_area_triangulo(a, b, c):
    s = (a + b + c) / 2  # Semi-perímetro
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    if verifica_triangulo(a, b, c):
        area = calcula_area_triangulo(a, b, c)
        print(f"Os valores {a}, {b} e {c} formam um triângulo.")
        print(f"A área do triângulo é {area:.2f}")
    else:
        print(f"Os valores {a}, {b} e {c} não formam um triângulo.")

if __name__ == "__main__":
    main()
