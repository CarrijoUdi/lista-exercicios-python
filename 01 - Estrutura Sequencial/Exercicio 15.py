'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

'''
import time

print('===========================')
vl_horas = float(input('Quanto você ganha por hora? : '))
horas_trabalhadas = float(input('Quantas horas trabalhou? : '))
print('===========================')

salario_bruto = vl_horas * horas_trabalhadas
irrf = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
descontos = irrf + inss + sindicato
salario_liquido = salario_bruto - (descontos)

print('Aguarde calculando seu salário')
for i in range(1,5):
    print('%' * i,end='')
    time.sleep(0.5)
print('Seu sálario está na tabela abaixo:')

print('===========================')
print(f"""
IR (11%) : R$ {irrf}
INSS (8%) : R$ {inss}
Sindicato ( 5%) : R$ {sindicato}
Total descontos : R$ {descontos}
Salário Bruto : R$ {salario_bruto}
Salário Liquido : R$ {salario_liquido}
""")
print('===========================')

