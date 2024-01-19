nota1 = int(input("ingrese la nota certamen:\n"))
nota2 = int(input("ingrese la nota certamen:\n"))
notaL = int(input("ingrese la nota laboratorio:\n"))
Nc = (59.5 - 0.3 * notaL)/0.7
Nf = 3 * Nc - (nota1 + nota2) + 1
print("Necesita nota ", int(round(Nf)), "en el certamen 3")