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
    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el primer número:\n'))
    resta = numero_1 - numero_2

    if resta > 0:
        print("el número es positivo:", resta)
    else:
        if resta < 0:
            print("el número es negativo:", resta)
        else:
            print("el número es cero:", resta)


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el segundo número:\n'))
    numero_3 = int(input('Ingrese el tercer número:\n'))

    if numero_1 % 2 == 0:
        print("es par")
    else:
        print("es impar")
    
    if numero_2 % 2 == 0:
        print("es par")
    else:
        print("es impar")
    
    if numero_3 % 2 == 0:
        print("es par")
    else:
        print("es impar")
    


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
    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el segundo número:\n'))
    operacion = str(input('Ingrese la operacion:\n'))

    if operacion == "+":
        resultado_suma = numero_1 + numero_2
        print(resultado_suma)
    else:
        if operacion == "-":
            resultado_resta = numero_1 - numero_2
            print(resultado_resta)
        else: 
            if operacion == "*":
                resultado_multiplicacion = numero_1 * numero_2
                print(resultado_multiplicacion)
            else:
                if operacion == "/":
                    resultado_division = numero_1 / numero_2
                    print(resultado_division)
                else:
                    if operacion == "**":
                        resultado_exponente = numero_1**numero_2
                        print(resultado_exponente)


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
    texto_1 = str(input('Ingrese la primera palabra:\n'))
    texto_2 = str(input('Ingrese la segunda palabra:\n'))
    texto_3 = str(input('Ingrese la tercera palabra:\n'))
    ordenamiento = str(input('ingrese tipo de ordenamiento:\n'))

    if texto_1[0] > texto_2[0] and texto_2[0] > texto_3[0] and ordenamiento == "1":
        print(texto_1, texto_2, texto_3)
    else:
        if texto_2[0] > texto_1[0] and texto_1[0] > texto_3[0] and ordenamiento == "1":
            print(texto_2, texto_1, texto_3)
            
        else:
            if texto_1[0] > texto_2[0] and texto_3[0] > texto_2[0] and ordenamiento == "1":
                # Acá entra si texto_3 > texto_1 !!!
                print(texto_1, texto_3, texto_2)
            else:
                if texto_3[0] > texto_2[0] and texto_2[0] > texto_1[0] and ordenamiento == "1":
                    print(texto_3, texto_2, texto_1)
                else:
                    if texto_2[0] > texto_1[0] and texto_3[0] > texto_1[0] and ordenamiento == "1":
                        print(texto_2, texto_3, texto_1)
                    else:
                        if texto_3[0] > texto_2[0] and texto_1[0] > texto_2[0] and ordenamiento == "1":
                            print(texto_3, texto_1, texto_2)                
    
    
    if len(texto_1) > len(texto_2) and len(texto_2) > len(texto_3) and ordenamiento == "2":
        print(texto_1, texto_2, texto_3)
    else:
        if len(texto_2) > len(texto_1) and len(texto_1) > len(texto_3) and ordenamiento == "2":
            print(texto_2, texto_1, texto_3)
        else:
            if len(texto_1) > len(texto_2) and len(texto_3) > len(texto_2) and ordenamiento == "2":
                print(texto_1, texto_3, texto_2)
            else:
                if len(texto_3) > len(texto_2) and len(texto_2) > len(texto_1) and ordenamiento == "2":
                    print(texto_3, texto_2, texto_1)
                else:
                    if len(texto_2) > len(texto_1) and len(texto_3) > len(texto_1) and ordenamiento == "2":
                        print(texto_2, texto_3, texto_1)
                    else:
                        if len(texto_3) > len(texto_2) and len(texto_1) > len(texto_2) and ordenamiento == "2":
                            print(texto_3, texto_1, texto_2)    


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
    temperatura_1 = int(input('Ingrese la primera temperatura:\n'))
    temperatura_2 = int(input('Ingrese la segunda temperatura:\n'))
    temperatura_3 = int(input('Ingrese la tercera temperatura:\n'))
    promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3

    if temperatura_1 > temperatura_2 and temperatura_2 > temperatura_3:
        print("la maxima temperatura es:", temperatura_1,", la minima es:", temperatura_3, "y el promedio es:", promedio)
    else:
        if temperatura_2 > temperatura_1 and temperatura_1 > temperatura_3:
           print("la maxima temperatura es:", temperatura_2,", la minima es:", temperatura_3, "y el promedio es:", promedio) 
        else:
            if temperatura_3 > temperatura_2 and temperatura_2 > temperatura_1:
               print("la maxima temperatura es:", temperatura_3,", la minima es:", temperatura_1, "y el promedio es:", promedio)
            else:
                if temperatura_3 > temperatura_1 and temperatura_1 > temperatura_2:
                    print("la maxima temperatura es:", temperatura_3,", la minima es:", temperatura_2, "y el promedio es:", promedio)
                else:
                    if temperatura_1 > temperatura_3 and temperatura_3 > temperatura_2:
                        print("la maxima temperatura es:", temperatura_1,", la minima es:", temperatura_2, "y el promedio es:", promedio)
                    else:
                        if temperatura_2 > temperatura_3 and temperatura_3 > temperatura_1:
                            print("la maxima temperatura es:", temperatura_2,", la minima es:", temperatura_1, "y el promedio es:", promedio)



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()

