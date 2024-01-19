def decimal_parte(n):
    numero_decimal = n - int(n)
    return numero_decimal
n = float(input("Ingrese un numero: "))

numero_decimal = decimal_parte(n)
print("La parte decimal es: ", numero_decimal)

