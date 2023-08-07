nome = input("Digite seu primeiro nome: ")
idade = int(input("Digite sua idade "))

#print("Olá, ", nome, "!")
#print("Tudo bem com você?")
#print("caramba", nome, "! você tem", idade, "anos? mem parece.")

print("Olá, {}".format(nome))
print("Tudo bem com você?")
print("caramba {}! você tem {} anos? nem parece.".format(nome, idade))

print(f"caramba {nome}! você tem {idade} anos? nem parece.")