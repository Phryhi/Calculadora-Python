# Calculadora simples

print("CALCULADORA")

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
operacao = input("Digite a operação desejada (soma, subtração, multiplicação, divisão): ")
resultado = int(numero1) + int(numero2)

if operacao == "soma":
    resultado = int(numero1) + int(numero2)
elif operacao == "subtração":
    resultado = int(numero1) - int(numero2)
elif operacao == "multiplicação":
    resultado = int(numero1) * int(numero2)
elif operacao == "divisão":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "Operação não suportada!"

print("O resultado da operação é: " + str(resultado))
