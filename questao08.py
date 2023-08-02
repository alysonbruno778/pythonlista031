"""
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro
"""

a = float(input("Diga a distancia da viagem em km/h: "))
b = float(input("Quanto seu automóvel faz por litro: "))

c = a * b

print("Nessa viagem você gastará ", c,"em litros")