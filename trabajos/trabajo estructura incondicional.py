#Taller
#punto4
#Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta
#lo siguiente
# toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
# cada minuto adicional a partir de los tres primeros es un paso de contador y
#cuesta 100 pesos.
duracion = int(input("ingrese la duracion de la llamada en minutos:"))
if duracion <=3:
    costo_total= 200
else:
    costo_total= 200 + (duracion - 3) * 100
#imprima el resultado
print("El costo total de la llamada es de ", costo_total, " pesos.")


#punto5
#En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros
#y Y conejos blancos. Hacer un algoritmo que:
# Imprima la cantidad de conejos vendida
#Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de
#los conejos negros, imprima el monto total de la venta.
# Imprima el color de los conejos que se vendieron más

(print("el numero de conejos que se vendieron"))
C1=int(input(cuantos conejos blancos se vendieron))
C2=int(input(cuantos conejos negros se vendieron))
P1=int(input(precio de venta de  los conejos blancos))
P2=int(input(precio de venta de los conejos negros))
C1*P1=(precio de los conejos blancos)
C2*P2=(precio de los conejos negros)
C1+C2=(cantidad de los conejos vendidos)
# Imprima la cantidad de conejos vendida
C3=C1+C2
print("el total de conejos vendidos es",C3)


#imprima el monto total de la venta
P3=(C1*P1)+(C2*P2)
print("el total de la venta de los conejos es",P3,"pesos")