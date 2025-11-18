#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#A fórmula de conversão é: C = (5/9) * (F - 32)
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (5/9) * (fahrenheit - 32)
print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")