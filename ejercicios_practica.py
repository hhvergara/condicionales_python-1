#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las siguientes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    
    print("")
    print("Los números ingresados son:",numero_1,"y",numero_2)

    if numero_1 < numero_2:
        print("El número mayor es:",numero_2)
    else:
        print("El número mayor es:",numero_1)

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    
    print("")
    if numero_1 > 0:
        print("El número",numero_1,"es positivo")
    elif numero_1 == 0:
        print("El numero es:",numero_1)#esto devuelve un 0 si es true
    else:
        print("El número",numero_1,"es negativo")
    
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    print("")
    if numero_1 > 0 and numero_1 < 100:
        print("El número",numero_1,"es mayor a 0 y menor a 100")
    else:
        print("El número",numero_1,"no cumple las condiciones solicitadas")
    
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2

    # Imprima en pantalla si se cumple o no la condición
    print("")
    if numero_1 < 10 | numero_2 > -2:
        print("Esta condición si se cumple:",numero_1,"y",numero_2)
    else:
        print("La condición no se cumple")
    #realizado



def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las siguientes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))
    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("La palabra mayor es:",texto_1)
    else:
        print("La palabra mayor es:",texto_2)
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    
    if len(texto_1) > len(texto_2):
        print("La palabra",texto_1,"tiene más cantidad de letras que",texto_2)
    elif len(texto_1) == len(texto_2):
        print("La palabra",texto_1,"tiene la misma cantidad de letras que",texto_2)
    else:
        print("La palabra",texto_2,"tiene más cantidad de letras que",texto_1)
    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if texto_1[0] > texto_2[0]:
        print("La primera letra de",texto_1,"es mayor a la primera letra de",texto_2)
    elif texto_1[0] == texto_2[0]:
        print("La primera letra de",texto_2,"es igual a la primera letra de",texto_1)
    else:
        print("La primera letra de",texto_2,"es mayor a la primera letra de",texto_1)

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    if copia_texto_1 == texto_1:
        print(copia_texto_1,"es igual a ",texto_1)
    else:
        print(copia_texto_1,"no es igual a",texto_1)
    
    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if copia_texto_1 == texto_2:
        print(copia_texto_1,"es igual a ",texto_2)
    else:
        print(copia_texto_1,"no es igual a",texto_2)
    #realizado



def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print(numero_2,"es positivo")
        elif numero_2 == 0:
            print(numero_2,"es cero")
        else:
            print(numero_2,"es negativo")
    elif numero_2 > 5:
        print(numero_1,"no es mayor a 5")
        print(numero_2,"es mayor a 5")
    else:
        print(numero_2,"y",numero_1,"no son mayores a 5")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es mayor a 60       --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 90:
        print("Felicidades! su puntaje es",puntaje)
    elif puntaje >= 80:
        print("Felicidades! su puntaje es",puntaje)
    elif puntaje >= 70:
        print("Felicidades! su puntaje es",puntaje)
    elif puntaje >= 60:
        print("Felicidades! su puntaje es",puntaje)
    elif puntaje > 60:
        print("Felicidades! su puntaje es",puntaje)
    else:
        print("Lo siento, no has aprobado :(",puntaje)
    #realizado



def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print(texto_1,"es mayor que",texto_2)
    else:
        print(texto_2,"es mayor que",texto_1)

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    texto_1 = int(texto_1)
    texto_2 = int(texto_2)
    
    if texto_1 > texto_2:
        print(texto_1,"es mayor que",texto_2)
    else:
        print(texto_2,"es mayor que",texto_1)
    
    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
    #realizado

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()