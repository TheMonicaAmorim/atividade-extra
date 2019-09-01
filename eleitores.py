import random

totalEleitores = input("informe o total de eleitores:\n")
brancos = input("informe o total de votos brancos:\n")
nulos = input("informe o total de votos nulos:\n")
v = (float(brancos) + float(nulos))
validos = (float(totalEleitores) - float(v))
print("dos", (totalEleitores), "somente", (validos), "serao validos")