print("hola bienvenido")
a= int(input("por favor ingrese el primer digito "))
residuo= a % 2
if a==0:
    print("El numero es cero")
elif (residuo==0):
    print("el numero es par")
    if (a>1):
        print("y positivo")
    else:
        print("y negativo")
else:
    print("el numero es impar")
    if (a>0):
        print("y positivo")
    else:
        print("y negativo")


    