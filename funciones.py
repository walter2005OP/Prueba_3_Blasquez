import os
import msvcrt
import time
import csv



def opc_1 (evaluacion_Blasquez):
    input("nombre: ")
    input("RUT: ")
    input("Comuna: ")
    input("Direccicón: ")
while True: 
    
    print("""
    Cual es el cilindro que desea pedir? 
    (1). 5  kilogramos
    (2). 15 kilogramos      
""")
    
    opcc = int(input("Elija la que cilindro desea pedir: "))

    if opcc == 1:
        print
