# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# entrada
valor1 = int(input("Digite o primeiro valor?")) # 5
valor2 = int(input("Digite o segundo valor?")) # 2
valor3 = int(input("Digite o terceiro valor?")) # 7

# processamento
resposta = ""
valorTemp = 0

if( valor1 > valor2 ):
    valorTemp = valor2
    valor2 = valor1
    valor1 = valorTemp
    
if( valor1 > valor3 ):
    valorTemp = valor3
    valor3 = valor1
    valor1 = valorTemp

if( valor2 > valor3 ): 
    valorTemp = valor3
    valor3 = valor2
    valor2 = valorTemp

# saida
print(valor1, valor2, valor3)