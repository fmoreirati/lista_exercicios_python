# 1) Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio))

#entrada
raio = int(input("Qual o raio?"))

#processamento
#area = PI * (raio * raio)
def calculoArea(valorRaio):
    PI = 3.14 #constante
    return PI * (valorRaio * valorRaio)

#saida
print("Area do circulo ", calculoArea(raio))

