# João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

kg = 0
multa = 4
excesso = 0

kg = float(input('Qual o peso pescado? : '))
if kg < 0:
    kg *= -1
if kg > 50:
    excesso = kg - 50
    multa = excesso * 4
    print(f"""
          Quantidade pescado: {kg} kilos.
          Quantidade excesso: {excesso} kilos.
          Multa : {multa}
          
          """)
else:
    print(f"""
          Quantidade pescado: {kg} kilos.
          Não tem excesso e nem multa.
                   
          """)
    