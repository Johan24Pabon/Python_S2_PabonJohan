# ##########################
# #### Clase Dia 2 ######
# ##########################

#verificar si un numero es promo
#entrada: verificar 
#salida: verificacion realizada

#proceso

print('Bienvenido al portal para verificar si un numero es primo')

print('Ingrese un numero que desee verificar si es primo')
numVerificar=int(input())

divisores= 1
cantidadDivisores=0
for i in range(1,numVerificar,1):

    divisores= divisores +1

    resultado = numVerificar % divisores

    if resultado == 0:
        cantidadDivisores = cantidadDivisores+1


if cantidadDivisores> 2:
    print('el numero no es primo')

else:
        print('el numero es primo')

#Desarrollado por Johan Eduardo Pabon Ortega C.C 1.097.495.280
 