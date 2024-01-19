def horas_reloj(t, h):
    return (t +h) % 12 or 12
t = int(input("Hora actual: "))
h = int(input("Cantidad de horas: "))

hora_marcada = horas_reloj(t, h)

print("En", h, "horas: ","el reloj marcara las: ", hora_marcada) 
    