#!/usr/bin/env python
'''
Página principal [Proyecto Inicial Python]
---------------------------
Autor: Johana Rangel
Version: 0.4

Descripcion:
Programa creado para validar permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "0.4"

import csv
import os
import re


def validacion():
    '''
    Función creada para que la empresa pueda agregar los datos 
    solicitados en las siguientes variables: codigo, dni, nombre de la empresa, 
    actividad, nombre empleado y apellido empleado, agregándose en un archivo csv 
    llamado "validacionempresas.csv".
    '''
    
    try:
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))

    #Capturando error de excepción para los datos que ingresen diferente al formato indicado.

    except:
        print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))
                    
    while codigo != 3:
        '''
        Bucle que funciona en base al código, mientras sea diferente de tres, porque 
        al ser igual entra en salir del programa. Luego, atrapando errores de excepción
        para la entrada de datos en las variables, en caso sea diferente al formato de entrada
        '''

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
            #Código para saber la existencia del archivo "validacionempresas" 

            if not file_exists:
                #En caso de no existir el archivo crearlo desde cero, agreando el header e incorpar
                #los datos indicados.

                with open('validacionempresas.csv', 'w', newline='') as fd:
                
                    header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                    writer = csv.DictWriter(fd, fieldnames=header)
                    writer.writeheader()         
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))        
            
                fd.close() 
                    
            elif file_exists: 
                #En caso de existir el archivo "validacionempresas.csv", agregar más registrados
                # a las filas.         
                with open('validacionempresas.csv', 'a', newline='') as fd:
                            
                    header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                    writer = csv.DictWriter(fd, fieldnames=header)
                                        
                    if not file_exists: # Esta opción permite reconocer si no existe el encabezado (el header)
                        writer.writeheader() # En caso no exista, escribirlo y si ya existe, no escribirlo.

                    #permite agegar más datos a las filas.
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    
                    try:
                        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN" para validar a otra persona:\n Ingrese 3, para salir\n'))  
                    
                    except:
                        print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
                        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN" para validar a otra persona:\n Ingrese 3, para salir\n'))                              
                
                
                fd.close()  

        elif codigo == 3:
            
                print('Ha salido del programa.') #Condición para permitir salir del programa
                break
            
            

if __name__ == '__main__':
    
    validacion()