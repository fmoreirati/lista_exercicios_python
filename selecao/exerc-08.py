#  8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
from datetime import date

#entrada
anoNasc = int(input("Qual o ano de seu nascimento?"))
ANOATUAL = date.today().year

#processamento
resposta=""
idade = ANOATUAL - anoNasc
if (idade > 16):
    resposta="sim"
else:
    resposta="não"

#saida
print("Você poderá votar este ano: ", resposta)
print("Porque voce tem ", idade, " anos")