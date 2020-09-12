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

def ingresa():
    
    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n')) 

    if codigo != 3:
        
        persona_ingresada = []
        
        with open('validacionempresas.csv') as csvfile:
            data = list(csv.DictReader(csvfile))
            cantidad_filas = len(data)
                                            
            for i in range(cantidad_filas):
                row = data[i]
                codigos = int(row.get('Codigo'))
                dni = int(row.get('DNI'))
                nombre_empresa = str(row.get('Nombre empresa'))
                actividad = str(row.get('Actividad'))
                nombre_empleado = str(row.get('Nombre empleado'))
                apellido_empleado = str(row.get('Apellido empleado'))
                            
                if codigos == codigo:
                    persona_ingresada.append(codigo)
                    persona_ingresada.append(dni)    
                    persona_ingresada.append(nombre_empresa)
                    persona_ingresada.append(actividad)
                    persona_ingresada.append(nombre_empleado)
                    persona_ingresada.append(apellido_empleado)
                                
                if codigo in persona_ingresada:
                    print('Código está registrado, está validado el ingreso provincial')
                    print('Los datos encontrados de acuerdo al código:', codigo, '\n DNI:', dni, '\n Nombre empresa:', nombre_empresa, '\n Actividad:', actividad, '\n Nombre empleado:', nombre_empleado, '\n Apellido empleado:', apellido_empleado)
                    
                else:
                    print('El código ingresado no se encuenta registrado, acceso denegado')
            
        csvfile.close()
    
        file_exists = os.path.isfile('ingresoprovincial.csv')

        if not file_exists:
            
            with open('ingresoprovincial.csv', 'w', newline='') as fd:
                header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                writer = csv.DictWriter(fd, fieldnames=header)
                writer.writeheader()
                    
                if codigo in persona_ingresada:
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))        
                        
                fd.close() 
            
        elif file_exists:
                        
            with open('ingresoprovincial.csv', 'a', newline='') as fd:
                header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                writer = csv.DictWriter(fd, fieldnames=header)
                                
                if not file_exists:
                    writer.writeheader()
                        
                if codigo in persona_ingresada:
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))  
                                            
            fd.close()
               
    elif codigo == 3:
            print('Ha salido del programa')
                           
    else:
        print('El valor ingresado no corresponde, intente nuevamente.')
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n')) 

    
if __name__ == "__main__":
    
    ingresa()