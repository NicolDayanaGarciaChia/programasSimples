nombre = input("Ingrese numero:\n")
array = []
for i in range(len(nombre)):
    array.append(nombre[-i-1])
print("".join(array))    