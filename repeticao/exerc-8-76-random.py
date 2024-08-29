# 76) Construa um algoritmo que leia 50 valores inteiros e positivos e:
# · Encontre o maior valor
# · Encontre o menor valor
# · Calcule a média dos números lidos

#OBS1. Refaça o exercícios ussando lista para armazenaros valores digitados pelo usuario.
#OBS2. Faça com que o sistema sorteie 6 valores digitados pelo usuarios logo após o exibir as mensagens (random.randrange(1, 51))

import random

maior = 0
menor = 9999999
soma = 0
limite = 10
listValores = [] #[] respresta um Array ou Lista

for x in range(1, limite+1):
    #valor = int(input(f"Qual o {x}º valor?"))
    valor = random.randrange(1, 101)
    if(valor > maior):
        maior = valor
    if(valor < menor):
        menor = valor
    soma = soma + valor

    listValores.append(valor)

print("Soma: ", soma)
print("Media: ", soma/limite)
print("Maior: ", maior)
print("Menor: ", menor)
print("Valores: ", listValores)


# Sorteio de Valores
listSorteados = []
quantNumerosSorteio = 4

# Comando While (Enquanto): utilizado para repetir entonto a expressao for veraderia. Neste caso enquanto a lista de sorteador for menor que quantidade de numeros sorteados
# Comando Len (lenght = tamanho): retorna o valor do tamanho da lista, isto é quantidade de itens
while(len(listSorteados) < quantNumerosSorteio): 
    index = random.randrange(0, len(listValores))
    valorSorteado = listValores[index]
    contDuplicados = 0
    for s in listSorteados:
        if(s==valorSorteado):
            contDuplicados += 1
    if(contDuplicados == 0):
        listSorteados.append(valorSorteado)

print("Numero sorteado: ", listSorteados )