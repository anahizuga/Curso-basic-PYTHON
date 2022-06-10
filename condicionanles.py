#Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-900:")

calificacion = int(calificacion)

#Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("veeez, por no estudiar") #si es menor a 700 muestra esto

elif calificacion == 700 :
    print("PANZASOOOOO")

elif calificacion > 1000 :
    print("MIENTES, no se puede sacar más de mil")
    
else : #si no se cumple el if anterior, pasa a esta linea
    print("felicidades, pasa por tu certificado") #se ejecuta si ninguno d elos of se cumple

#verificacdor de mayoría de edad
edad = input ("introduce tu edad:")
edad = int(edad)

#aqui se usa un operador que son para hacer operaciones "and"
if edad >= 18 and edad <= 100 : 
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("ni que fueras viajero en el tiempo")
else :
    print("no puedes llevarte esos cigarros")

    #en python no hay switch case 