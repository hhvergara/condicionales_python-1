#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    num_1 = int(input("Ingrese un número: "))
    num_2 = int(input("Ingrese otro número: "))

    r = num_1 % num_2

    if r > 0:
        print("Su resultado es positivo!",r)
    elif r < 0:
        print("Su resultado es negativo!",r)
    else:
        print("Su resultado es:",r)
    #realizado



def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    num_1 = int(input("Ingrese un número: "))
    num_2 = int(input("Ingrese otro número: "))
    num_3 = int(input("Ingrese un tercer número: "))

    if num_1 % 2 == 0:
        print(num_1,"es par!")
    else:
        print(num_1,"no es par!")

    if num_2 % 2 == 0:
        print(num_2,"es par!")  
    else:
        print(num_2,"no es par!")

    if num_3 % 2 == 0:
        print(num_3,"es par!")
    else:
        print(num_3,"no es par")  
    #realizado



def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print("Ingrese un número")
    num1 = float(input(": "))
    print("")
    print("Ingrese otro número")
    num2 = float(input(": "))
    #operations

    print("Qué operación deseas realizar?")
    print("Ingresa '+' para suma")
    print("Ingresa '-' para resta")
    print("Ingresa '*' para multiplicación")
    print("Ingresa '/' para división")
    print("Ingresa '**' para potencia")

    operator = str(input(": "))
    
    if operator == "+":
        suma = num1 + num2
        print("El resultado de su suma es:",suma)
    elif operator == "-":
        resta = num1 - num2
        print("El resultado de su resta es:",resta)
    elif operator == "*":
        multiplicacion = num1 * num2
        print("El resultado de su multiplicación es:",multiplicacion)
    elif operator == "/":
        division = num1 - num2
        print("El resultado de su división es:",division)
    elif operator == "**":
        potencia = num1 ** num2
        print("El resultado de su potencia es:",potencia)
    else:
        print("Ninguna de las opciones es correcta, elige otra operación:")
        print("Ingresa '+' para suma")
        print("Ingresa '-' para resta")
        print("Ingresa '*' para multiplicación")
        print("Ingresa '/' para división")
        print("Ingresa '**' para potencia")
    #realizado



def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    word_1 = str(input("Ingrese una palabra: ")).capitalize()
    word_2 = str(input("Ingrese otra palabra: ")).capitalize()
    word_3 = str(input("Ingrese una tercer palabra: ")).capitalize()

    print("Presiona '1' para ordenar alfabéticamente las palabras")
    print("Presiona '2' para ordenar de mayor a menor cantidad de letras")

    operator = int(input(": "))

    if operator == 1:
        if word_1 > word_2 and word_1 > word_3:
            print("1:",word_1)
            if word_2 > word_3:
                print("2:",word_2)
                print("3:",word_3)
            else:
                print("2:",word_3)
                print("3:",word_2)
        elif word_2 > word_1 and word_2 > word_3:
            print("1:",word_2)
            if word_1 > word_3:
                print("2:",word_1)
                print("3:",word_3)
            else:
                print("2:",word_3)
                print("3:",word_1)
        elif word_3 > word_1 and word_3 > word_2:
            print("1:",word_3)
            if word_1 > word_2:
                print("2:",word_1)
                print("3:",word_2)
            else:
                print("2:",word_2)
                print("3:",word_1)
    elif operator == 2:
        if len(word_1) > len(word_2) and len(word_1) > len(word_3):
            print("1:",word_1)
            if len(word_2) > len(word_3):
                print("2:",word_2)
                print("3:",word_3)
            else:
                print("2:",word_3)
                print("3:",word_2)
        elif len(word_2) > len(word_1) and len(word_2) > len(word_3):
            print("1:",word_2)
            if len(word_1) > len(word_3):
                print("2:",word_1)
                print("3:",word_3)
            else:
                print("2:",word_3)
                print("3:",word_1)
        elif len(word_3) > len(word_1) and len(word_3) > len(word_2):
            print("1:",word_3)
            if len(word_1) > len(word_2):
                print("2:",word_1)
                print("3:",word_2)
            else:
                print("2:",word_2)
                print("3:",word_1)
    else:
        print("Ingresa una opción válida")
    #realizado



def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    temp_1 = float(input("Ingrese su temperatura: "))
    temp_2 = float(input("Ingrese otra temperatura: "))
    temp_3 = float(input("Ingrese una tercer temperatura: "))

    if temp_1 > temp_2 and temp_1 > temp_3:
        print("La temperatura máxima es:",temp_1,"º")
        if temp_2 > temp_3:
            print("La temperatura mínima es:",temp_3,"º")
        else:
            print("La temperatura mínima es:",temp_2,"º")
    elif temp_2 > temp_1 and temp_2 > temp_3:
        print("La temperatura máxima es:",temp_2)
        if temp_1 > temp_3:
            print("La temperatura mínima es:",temp_3,"º")
        else:
            print("La temperatura mínima es:",temp_1,"º")
    elif temp_3 > temp_1 and temp_3 > temp_2:
        print("La temperatura máxima es",temp_3,"º")
        if temp_1 > temp_2:
            print("La temperatura mínima es",temp_2,"º")
        else:
            print("La temperatura mínima es",temp_1,"º")
    else:
        print("Las temperaturas son todas iguales")

    promedio = (temp_1+temp_2+temp_3)/3

    print("El promedio de temperaturas es de",promedio,"º")
    #realizado


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()