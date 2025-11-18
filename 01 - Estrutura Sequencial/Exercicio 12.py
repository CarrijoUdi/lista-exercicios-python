#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: Gigabytes * 1024

gb = float(input('Informe o tamanho em GB: '))

mb = gb * 1020

print(f'Seu arquivo tem {mb} Megabytes')