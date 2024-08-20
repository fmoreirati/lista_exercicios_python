#  8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
from datetime import date
#entrada
anoNasc = int(input("Qual o ano de seu nascimento?"))
# ANOATUAL = date.today().year

#processamento
def verficarOpcaoVoto(idadeUser):
    #resposta=""
    #idade = ANOATUAL - anoNasc
    if (idadeUser > 16):
        #resposta="sim"
        return "sim"
    else:
        #resposta="não"
        return "não"
    
def idade(nascimento):
    ANOATUAL = date.today().year
    return ANOATUAL - nascimento

idadeAtualUser = idade(anoNasc)
#saida
print("Você poderá votar este ano: ", verficarOpcaoVoto(idadeAtualUser))
print("Porque voce tem ", idadeAtualUser , " anos")