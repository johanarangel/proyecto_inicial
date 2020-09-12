#!/usr/bin/env python
'''
Página principal [Proyecto Inicial Python]
---------------------------
Autor: Johana Rangel
Version: 0.1

Descripcion:
Programa creado para validar permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "0.3"

import csv
import os
import re


def validacion():
    
    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))
                    
    while codigo != 3:
        
        try:
            dni = int(input('Ingrese número de "DNI": \n Ingrese 3, para salir\n'))
        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            dni = int(input('Ingrese número de "DNI": \n Ingrese 3, para salir\n'))

        try:
            nombre_empresa =  str(input('Ingrese "NOMBRE DE LA EMPRESA": \n Ingrese "FIN", para salir\n'))
        except:    
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            nombre_empresa =  str(input('Ingrese "NOMBRE DE LA EMPRESA": \n Ingrese "FIN", para salir\n'))

        try:
            actividad = str(input('Ingrese "ACTIVIDAD": \n Ingese "FIN", para salir\n'))
        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            actividad = str(input('Ingrese "ACTIVIDAD": \n Ingese "FIN", para salir\n'))
            
        try:
            nombre_empleado = str(input('Ingrese "NOMBRE DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))
        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            nombre_empleado = str(input('Ingrese "NOMBRE DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))
        
        try:    
            apellido_empleado = str(input('Ingrese "APELLIDO DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))
        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            apellido_empleado = str(input('Ingrese "APELLIDO DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))

        
        if codigo != 3: 
            file_exists = os.path.isfile('validacionempresas.csv')

            if not file_exists:
                with open('validacionempresas.csv', 'w', newline='') as fd:
                
                    header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                    writer = csv.DictWriter(fd, fieldnames=header)
                    writer.writeheader()         
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))        
            
                fd.close() 
                    
            elif file_exists:
                        
                with open('validacionempresas.csv', 'a', newline='') as fd:
                            
                    header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                    writer = csv.DictWriter(fd, fieldnames=header)
                                        
                    if not file_exists:
                        writer.writeheader()

                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN" para validar a otra persona:\n Ingrese 3, para salir\n'))  
                                                
                fd.close()  

        elif codigo == 3:
            print('Ha salido del programa.') 
            break

if __name__ == '__main__':
    
    validacion()