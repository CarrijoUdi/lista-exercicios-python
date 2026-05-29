#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Quanto você ganha por hora? : '))

horas_trabalhadas = float(input('Quantas horas trabalhou? : '))

salario_mes = ganho_hora * horas_trabalhadas

print(f'Seu sálario é de R$ {salario_mes}')
