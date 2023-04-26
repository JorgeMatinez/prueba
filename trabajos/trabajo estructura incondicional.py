""" Taller
punto4
Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta
lo siguiente
 toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
 cada minuto adicional a partir de los tres primeros es un paso de contador y
cuesta 100 pesos. """ """

duracion = int(input("ingrese la duracion de la llamada en minutos:"))
if duracion <=3:
    costo_total= 200
else:
    costo_total= 200 + (duracion - 3) * 100

print("El costo total de la llamada es de ", costo_total, " pesos.")


""" """ punto5
En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros
y Y conejos blancos. Hacer un algoritmo que:
 Imprima la cantidad de conejos vendida
Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de
los conejos negros, imprima el monto total de la venta.
 Imprima el color de los conejos que se vendieron más
 """
""" (print("ingresa el numero de conejos blancos y negros que has vendido"))
C1=int(input("cuantos conejos blancos vendiste?"))
C2=int(input("cuantos conejos negros vendiste?"))
P1=float(input("precio de venta de cada conejo blanco?"))
P2=float(input("precio de venta de cada conejo negro?")) """

# Imprima la cantidad de conejos vendida """

#C3=C1+C2
#print("el total de conejos vendidos es",C3,)
#imprima el monto total de la venta
#P3=(C1*P1)+(C2*P2)
#print("el total de la venta de los conejos es",P3,"pesos")
#if C1>C2:
    #print("se vendieron conejos blancos",C1)
#elif C1==C2:
    #print("se vendieron la misma cantidad de conejos negros y blancos",C1,C2)    
#else:
    #print("se vendieron mas conejos negros",C2)

    #punto6
#     Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes,
# determinadas sobre las siguientes condiciones:
# • NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante
# tendrá 3 evaluaciones.
# • NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante
# presentara 2 trabajos.
# • NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
# • Nota mínima 1,0 nota máxima: 5,0


nota1=float(input("digite el primer numero: "))
if nota1 < 1 or nota1 > 5 :
    print("nota invalida")
else :
    nota2=float(input("digite el segundo numero: "))
    if nota2 < 1 or nota2 > 5 :
     print("nota invalida")
    else:
        nota3=float(input("digite el tercer numero: "))
        if nota3 < 1 or nota3 > 5 :
            print("nota invalida")
        else:
            notaprevios= ((nota1 + nota2 +nota3)/3) *0.6
            nota4=float(input("digite el cuarto numero: "))
            if nota4 < 1 or nota4 > 5:
                print("nota invalida")
            else:
                nota5=float(input("digite el quinto numero: "))
                if nota5 < 1 or nota5 > 5:
                    print("nota invalida")
                else:
                    notatrabajos=((nota4+nota5)/2)*0.4
                    notafinal=notaprevios+notatrabajos
                    print("Su nota final es",notafinal)

#punto7
""" Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,
cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo existen dos claves) """

""" Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,
cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo existen dos claves) """



#punto8
# En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología. El
# presupuesto anual del hospital se reparte a estas tres (3) áreas; usted debe realizar
# un algoritmo que permita ingresar el valor del presupuesto anual, ingresar el
# porcentaje correspondiente a cada área, realizar el cálculo del presupuesto que
# corresponde a cada área,si la suma de los porcentajes no corresponde al 100% debe
# mostrar un mensaje de error.
# Mostrar el porcentaje asignado a cada área y el presupuesto obtenido.

presupuesto_anual=float(input("digite el presupuesto anual:"))
pediatria=float(input("cuanto porcentaje (%) pediatria:"))
psiquiatria=float(input("cuanto porcentaje(%) psiquiatria:"))
traumologia=float(input("cuanto porcentaje(%) traumologia:"))
if pediatria + psiquiatria + traumologia== 100:
    p1=((presupuesto_anual *pediatria)/100)
    p2=((presupuesto_anual * psiquiatria)/100)
    p3=((presupuesto_anual * traumologia)/100)
    print("Al area pediatria le corresponde :",p1 ,"psiquiatria" ,p2, "traumologia:",p3,)
    print("para un total de : ", p1+p2+p3)
else:
    print("error,LA SUMA DE LOS PORCENTAJES DA MAS DEL 100%")

#punto9



    
