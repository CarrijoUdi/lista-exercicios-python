#Faça um programa que peça dois números e imprima a soma:

soma = 0
for i in range(2):
    num = int(input(f'Informe o {i+1}° número: '))
    soma += num
print(f'A soma dos números é:{soma}')