""" Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes. """

gb = float(input('Qual tamanho do arquivo em Gigabytes? : '))

mb = gb * 1024
kb = gb * (1024 ** 2)

print(f"""
Em Megabytes : {mb}
Em Kilobytes: {kb}
""")