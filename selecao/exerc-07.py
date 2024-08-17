#  7) Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

# entrada
valor1 = float(input("Qual o primeiro valor? "))
valor2 = float(input("Qual o segundo valor? "))

# processamento
# resposta = 0
# if valor1 > valor2:
#     resposta = valor1
# else:
#     resposta = valor2

resposta = valor1 if valor1 > valor2 else valor2
# resposta = (valor1 > valor2) ? valor1 : valor2 // javascript

# saida
print("O maior deles: ", resposta)