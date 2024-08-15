#  5) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#entradas
valor = int(input("Escreva uma valor: "))

#processamento
resposta = ""
if valor >= 0:
    resposta = "Positivo"
else:
    resposta = "Negativo"

#saidas
print ("O valor é ", resposta)