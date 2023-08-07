valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

print(f"Valor 1: {valor1:f}")

print("valor 1: {valor1:.2f}")
print("valor 2: {valor2:.2f}")
print("valor 3: {valor3:.2f}")

print("valor 2: {valor2:.2f}")

print("valor 1: {valor1:10.2f}")
print("valor 2: {valor2:10.2f}")
print("valor 3: {valor3:10.2f}")

print("valor 1: {valor1:010.2f}")
print("valor 2: {valor2:010.2f}")
print("valor 3: {valor3:010.2f}")

valor4 = 0.7536

print(f"Valor 4: {valor4:.1%}")

texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto valor 2: {texto_valor2}")

texto_valor_br = texto_valor2.replace(".",",").replace("_",".")
print(f"Texto valor BR: {texto_valor_br}")