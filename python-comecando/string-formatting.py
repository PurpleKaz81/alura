print("R${:f}".format(1.59))

print("R${:.2f}".format(1.59))

print("R${:.2f}".format(1.5))

print("R${:.2f}".format(1234.5))

print("R${:7.2f}".format(1234.5))

print("R${:7.2f}".format(4.5))

print("R${:07.2f}".format(4.5))

print("R${:07d}".format(4))

print("R${:7d}".format(46))

print("Date {:02d}/{:02d}".format(9, 4))

print("Date {:02d}/{:02d}".format(19, 11))

name = "Leonardo"
last_name = "Cordeiro"
sign = "peixes"
condition = "homão da porra"

print("Olá, Sr. {1}, {0}, de {2}, {3}".format(name, last_name, sign, condition))

name = "Rodrigo"
last_name = "Mattos"
sign = "câncer"
condition = "delícia viva e Sazon\u00ae dos meus olhos \U0001F60D"

print(f"Olá, Sr. {last_name}, {name}, de {sign}, {condition} ")
