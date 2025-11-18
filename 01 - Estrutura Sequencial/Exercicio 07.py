#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

area = 0

lado = float(input('Informe o valor lado do quadrado: '))

area = lado ** lado
dobro = 2 * area
print(f'O dobro da áre desse quadrado é {dobro}.')