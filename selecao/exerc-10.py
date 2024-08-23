# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# entrada
valor1 = int(input("Digite o primeiro valor?")) # 5
valor2 = int(input("Digite o segundo valor?")) # 2
valor3 = int(input("Digite o terceiro valor?")) # 7

# processamento
resposta = ""
if( valor1 < valor2 and valor2 < valor3 ):
    resposta = valor1 + " < "+ valor2 + " < " + valor3 
elif ( valor1 < valor3 and valor3 < valor2 ): 
    resposta = valor1 + " < " + valor3  + " < " + valor2
elif ( valor2 < valor3 and valor3 < valor1 ): 
    resposta = valor2 + " < " + valor3  + " < " + valor1
elif ( valor2 < valor1 and valor1 < valor3 ): 
    resposta = valor2 + " < " + valor1  + " < " + valor3
elif ( valor3 < valor1 and valor1 < valor2 ): 
    resposta = valor3 + " < " + valor3  + " < " + valor1
else: # valor3 < valor2 and valor2 < valor3 
    resposta = valor3 + " < " + valor2  + " < " + valor3

# saida
print(resposta)