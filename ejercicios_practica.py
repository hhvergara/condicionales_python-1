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
    
    print("  Rtas de ej (1)  ")
    
    # Comparadores
    # Ingrese dos números cualesquiera y realice las siguientes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print("El numero_1 =", numero_1, "es mayor al numero_2 =", numero_2)
    else:
        print("El numero_2 =", numero_2, "es mayor al numero_1 =", numero_1)


    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print("Numero_1 es positivo porque vale", numero_1)
    elif numero_1 < 0:
        print("Numero_1 es negativo porque vale", numero_1)
    else:
        print("Numero_1 es cero porque vale", numero_1)


    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 > 0 and numero_1 < 100):
        print("Se cumple la condición")
    else:
        print("No se cumple la condición")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10 or numero_2 > -2):
        print("Se cumple la condición")
    else:
        print("No se cumple la condición")

def ej2():
    # Ejemplos variables de texto

    print("  Rtas de ej (2)  ")
    
    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda


    if texto_1 > texto_2:
        print("{} es mayor que {}".format(texto_1, texto_2))
    else:
        print("{} es mayor que {}".format(texto_2, texto_1))

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    texto1_len = len(texto_1)
    texto2_len = len(texto_2)

    print("cantidad de caracteres de texto_1 ", texto_1, "es", texto1_len)
    print("cantidad de caracteres de texto_2 ", texto_2, "es", texto2_len)

    if texto1_len > texto2_len:
        print("{} tiene mayor cantidad de letras que {}".format(texto_1, 
                                                                texto_2))
    elif texto1_len < texto2_len:
        print("{} tiene menor cantidad de letras que {}".format(texto_1,
                                                                 texto_2))
    else:
        print("{} tiene la misma cantidad de letras que {}".format(texto_1,
                                                                 texto_2))


    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    letra1_texto1 = texto_1[0]
    print("la primera letra de texto_1 es ", letra1_texto1)

    letra1_texto2 = texto_2[0]
    print("la primera letra de texto_2 es ", letra1_texto2)

    if letra1_texto1 > letra1_texto2:
        print("1er letra de texto_1 es mayor a 1er letra de texto_2")
    else:
        print("1er letra de texto_1 es menor a 1er letra de texto_2")

    
    
    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    if texto_1 == copia_texto_1:
        print("copia_texto_1 = ", copia_texto_1, "es IGUAL a texto_1 =", texto_1)
    if texto_1 != copia_texto_1:
        print("copia_texto_1 = ", copia_texto_1, "es DISTINTO a texto_1 =", texto_1)

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if texto_2 != copia_texto_1:    
        print("copia_texto_1 = ", copia_texto_1, "es DISTINTO a texto_2 =", texto_2)
    else:
        print("copia_texto_1 = ", copia_texto_1, "es IGUAL a texto_2 =", texto_2)

def ej3():
    # Ejercicios de práctica numérica
    
    print("  Rtas de ej (3)  ")
    
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


    if numero_1 > numero_2:
        if numero_2 > 0:
            print("Resp=1")
        else:
            print("Resp_2")
    else:
        if numero_2 > 5:
            print("Resp=3")
        else:
            print("Resp_4")        


    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70
    
    if puntaje < 60:
        print("F, porque su puntaje es =", puntaje)
    else:
        print("El puntaje es mayor de 60")
    if (puntaje >= 60 and puntaje < 70):
        print("D, porque su puntaje es =", puntaje)
    if (puntaje >= 70 and puntaje < 80):
        print("C, porque su puntaje es =", puntaje)
    if (puntaje >= 80 and puntaje < 90):
        print("B, porque su puntaje es =", puntaje)
    if puntaje > 90:
        print("A, porque su puntaje es =", puntaje)
    
    # Inovetip: Qué pasa si el puntaje  es 90?? :D


    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
    # Ejemplos variables de texto

    print("  Rtas de ej (4)  ")

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    
    if texto_1 > texto_2:
        print("{} que es texto_1 es mayor que {} que es texto_2 ".format(texto_1, texto_2))
    else:
        print("{} que es texto_2 es mayor que {} que es texto_1 ".format(texto_2, texto_1))


    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)

    num_texto_1 = int(texto_1)
    num_texto_2 = int(texto_2)

    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    if num_texto_1 > num_texto_2:
        print("num_texto_1 =", num_texto_1, "es mayor a num_texto_2 =", num_texto_2)
    else:
        print("num_texto_2 =", num_texto_2, "es mayor a num_texto_1 =", num_texto_1)   

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    ej2()
    #ej3()
    #ej4()
