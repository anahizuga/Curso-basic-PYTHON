#declaramos una variable
calificación = input("Introduce tu calificación de la AZ-900:")

calificación = int(calificación)
#preguntamos si la calñificación es menor a 700
if calificación <700 : 
    print("vez, por no estudiar") #si es menor a 700 muestra esto
elif calificación > 1000 :
    print("no se puede, mientes")
else : #sino se cumple el int anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado") #se ejecuta si ninguno de los if se cumple

#verificador de mayoria de edad
edad = input("introduce tu edad:")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print(" Bienvenid@ al mamitas")
elif edad > 100 :
    print("si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero en el tiempo")
else :
    print("Noi puedes llevarte esos cigarros")
