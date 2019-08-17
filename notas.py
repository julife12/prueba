s1=float(input("ingrese la nota de seguimiento 1: "))
p1=float(input("ingrese la nota del parcial 1: "))
s2=float(input("ingrese la nota de seguimiento 2: "))
p2=float(input("ingrese la nota del parcial 2: "))
l=float(input("ingrese la nota del laboratorio: "))
ns1= s1*0.1
np1= p1*0.25
ns2= s2*0.1
np2= p2*0.3
nl= l*0.25
nf= ns1+ns2+np1+np2+nl
print("la nota final es", nf)
if nf>=3.0:
    if nf>=4.5:
        print("alumno excelente")
    else:
        print("paso")
else:
    if nf<2.0:
        print("perdio la asignatura")
    else:
        print("puede habilitar")

