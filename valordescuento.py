print("hola, bienvenido ")
p1=int(input("por favor indique el peso del paquete "))
d1=int(input("por favor digite la distancia a la que se va a enviar el paquete en kilometros "))
if p1<10:
    print("el paquete ha sido rechazado porque el peso esta por debajo del minimo ")


precio=(p1*1500)+(d1*4000)
if p1>100:
    if d1>100:
        porcentaje=precio*0.15
        precioT=precio-porcentaje
        if d1>2000:
            porcentajePro=precioT*0.1
            precioPro=precioT-porcentajePro
            print("el precio total es: ", precioPro)
        else:
            print("el precio total es ", precioT)
else:
    if d1>2000:
        porcentaje=precio*0.1
        precioT= precio-porcentaje
        print("el precio total es: ", precioT)
    else:
        print("el precio total es: ", precio)


