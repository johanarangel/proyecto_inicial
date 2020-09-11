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
__version__ = "0.1"

import csv
import os


def menu():
    
    consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))
        
    if consulta == 1:
        print('Bienvenido a la validación de trabajadores por empresa para ingreso provincial.')
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n'))
                    
        while codigo != 2:
            if codigo != 2:
                dni = int(input('Ingrese número de "DNI": \n Ingrese 2, para salir\n'))
                nombre_empresa =  str(input('Ingrese "NOMBRE DE LA EMPRESA": \n Ingrese "FIN", para salir\n'))
                actividad = str(input('Ingrese "ACTIVIDAD": \n Ingese "FIN", para salir\n'))
                nombre_empleado = str(input('Ingrese "NOMBRE DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))
                apellido_empleado = str(input('Ingrese "APELLIDO DEL EMPLEADO": \n Ingrese "FIN", para salir\n'))
                
                file_exists = os.path.isfile('validacionempresas.csv')

                if not file_exists:
                    with open('validacionempresas.csv', 'w', newline='') as fd:
                        header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                        writer = csv.DictWriter(fd, fieldnames=header)
                        writer.writeheader()
                        writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n'))        
                    fd.close() 
                
                if file_exists:
                    with open('validacionempresas.csv', 'a', newline='') as fd:
                        header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                        writer = csv.DictWriter(fd, fieldnames=header)
                        
                        if not file_exists:
                            writer.writeheader()

                        writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n'))  
                                
                    fd.close()  

            elif codigo == 2:
                print('Bienvenido a la validación de trabajadores por empresa.') 

    elif consulta == 2:
        print('Bienvenido a la validación de datos en puntos de control para ingreso provincial.')
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n'))  
        
        with open('validacionempresas.csv') as csvfile:
            data = list(csv.DictReader(csvfile))

        persona_ingresada = []
        cantidad_filas = len(data)
        contador = 0
                        
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
                print('Los datos encontrados de acuerdo al código:', codigo, 'son', persona_ingresada)
                print('Código está registrado, está validado el ingreso provincial')

            elif codigos != codigo:
                print('El código ingresado no se encuenta registrado, acceso denegado')

            else:
                print('El valor ingresado no corresponde, intente nuevamente.')
                codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 2, para salir\n'))  

    elif consulta == 3:
        pass
        
    else:
        print('El valor ingresado no corresponde con los indicados, intente nuevamente')

if __name__ == '__main__':
    
    print('Bienvenido al programa de verificación de permiso provincial')
    menu()
    

