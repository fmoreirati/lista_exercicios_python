#  6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for digitado o valor zero, escrever a palavra zero 
 
#entradas
valor = int(input("Escreva uma valor: "))

#processamento
resposta = ""
if valor == 0:
    resposta = "Zero"
elif valor > 0:
    resposta = "Positivo"
else:
    resposta = "Negativo"

#saidas
print ("O valor é ", resposta)