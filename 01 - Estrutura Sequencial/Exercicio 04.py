#Faça um programa que peça as 4 notas bimestrais e mostre a média.

media = 0
soma_notas = 0
for x in range(1,5):
    nota = float(input(f'Informe a {x}º nota: '))
    soma_notas += nota
    media = soma_notas / x
print(f'Sua mádia é de {media:.2f} pontos.')    
