contador = 0
respuesta = 10
a = 0

while a!=10:
    a = int(input("Ingrese la respuesta correcta"))
    if a == 10:
        contador +=1

if(contador == 1):
    print("ganaste")