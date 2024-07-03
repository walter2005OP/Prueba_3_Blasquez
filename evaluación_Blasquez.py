import os
from funciones import *
import time
import msvcrt

Rut = []
nombre = []
direccion = []
comuna = []
cil_5 = []
cil_15 = []

while True:

    

    print("""
    bienvenido a Gaxplosive.
    ¿que desea hacer?: 
         
    (1). Registrar pedido
    (2). Listar todos los pedidos
    (3). Buscar pedido por RUT
    (4). Imprimir hoja de ruta
    (5). salir
    """)
    
    msvcrt.getch
    opc = int(input("elija la opcion que desea ejecutar: "))

    if opc == 1:
            while True:
                input("nombre: ")
                input("RUT: ")
                input("Comuna: ")
                input("Direccicón: ")
             
        
                print("""
                Cual es el cilindro que desea pedir? 
                (1). 5  kilogramos
                (2). 15 kilogramos      
                """)

                opcc = int(input("Elija la que cilindro desea pedir: "))

                if opcc == 1:
                    cil_5.append(+1)
                    print ("se agrego con exito")
                elif opcc == 2:
                    cil_15.append(+1)
                    print("se agrego con exito")
                    break

    elif opc == 2:
            pass
    elif opc == 3:
            pass
    elif opc == 4:
            pass
    elif opc == 5:    
            print("Muchas gracias, vuelva pronto. ")
    else:
            print("!ERROR, esa opcion no existe.")


        
   
    
    
    


