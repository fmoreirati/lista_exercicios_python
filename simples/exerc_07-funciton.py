''' 7) A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
abastecimentos é o mesmo.'''

#entrada
comprimento = float(input("Comprimento da pista (em metros)? ")) #1000 -> 1km
voltas = int(input("Número total devoltas? ")) #10
abastecimento = int(input("Número de abastecimentos desejados? ")) #2
consumo = float(input("Consumo de combustível do carro (em Km/L)? ")) #10 

#processamento
# kmTotal = (comprimento / 1000) * voltas
# consumoTotal = kmTotal / consumo
# litros = consumoTotal / abastecimento

def calculoListros():
    kmTotal = (comprimento / 1000) * voltas
    consumoTotal = kmTotal / consumo
    return consumoTotal / abastecimento

#saida
print("O número mínimo de litros necessários até o primeiro reabastecimento: ", calculoListros())


def calculoListros(comprimento, voltas, consumo, abastecimento):
    kmTotal = (comprimento / 1000) * voltas
    consumoTotal = kmTotal / consumo
    return consumoTotal / abastecimento


print ("Carro 1:", calculoListros(2000, 10, 14, 3))
print ("Carro 2:", calculoListros(6000, 30, 5, 10))