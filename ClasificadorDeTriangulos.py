# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:25:34 2019

@author: Alfonso
"""

def leer(pos):
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = input("Ingrese el " + pos + " número entero: ")
        try:
            valor = int(valor)
            if valor >= 1:
                if valor <= 200:
                    return valor
                else:
                    print("Error: Debe ingresar un numero menor o igual a 200")
            else:
                print("Error: Debe ingresar un numero mayor o igual a 1")
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def definirTriangulo(a, b, c):
    """Dado 3 numero determina si es un triangulo y que tipo de triangulo es"""
    if a+b>c and a+c>b and c+b>a:
        if a==b and b==c:
            return "El triangulo es un triangulo EQUILATERO"
        elif a!=b and b!=c and a!=c:
            return "El triangulo es un triangulo ESCALENO"
        else:
            return "El triangulo es un triangulo ISOSCELES"
    else:
        return "Las medidas dadas no forman un triangulo"


print("Ingrese 3 numeros para determinar que tipo de triangulo es.")

a = leer("primer")
b = leer("segundo")
c = leer("tercer")


print(definirTriangulo(a,b,c))
