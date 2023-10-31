def calcular_idade_em_anos_meses_dias(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30
    return anos, meses, dias_finais


def ler_idade_em_dias():
    dias = int(input("Digite a idade em dias: "))
    return dias


def exibir_idade_em_anos_meses_dias(anos, meses, dias):
    print(f"Idade: {anos} anos, {meses} meses e {dias} dias")


idade_em_dias = ler_idade_em_dias()
anos, meses, dias = calcular_idade_em_anos_meses_dias(idade_em_dias)
exibir_idade_em_anos_meses_dias(anos, meses, dias)