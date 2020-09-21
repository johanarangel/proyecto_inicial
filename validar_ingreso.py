#!/usr/bin/env python
'''
Página principal [Proyecto Inicial Python]
---------------------------
Autor: Johana Rangel
Version: 0.5

Descripcion:
Programa creado para validar permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "0.5"

import csv
import os
import re
import principal

def ingresa():

    '''Función creada para imprimir por pantalla si el código ingresado 
    tiene permiso para acceso provincial o no.
    '''
         
    try:
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))

    #Capturando error de excepción para los datos que ingresen diferente al formato indicado.

    except:
        print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
        codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n')) 

    if codigo != 3:
        
        '''Si el codigo en diferente a tres, se abre el archivo csv
        "validacionempresas.csv" cuya data se convierte en una lista. 
        Luego se crea una variable llamada "cantidad_filas" que es 
        igual a la longitud de la la data.
        '''
        persona_ingresada = [] #Variable que almacenará los datos de la persona que tenga permiso de ingreso provincial.

        file_exists = os.path.isfile('validacionempresas.csv') #Se verifica si existe el archivo
        
        if file_exists: #En caso exista procede a validar el codigo ingresado

            with open('validacionempresas.csv') as csvfile:
                data = list(csv.DictReader(csvfile))
                cantidad_filas = len(data)

            #Luego con el bucle for se recorre el range cantidad de filas
            # Para poder extraer la información de cada columna.                                    
                
                for i in range(cantidad_filas):
                    row = data[i]
                    codigos = int(row.get('Codigo'))
                    dni = int(row.get('DNI'))
                    nombre_empresa = str(row.get('Nombre empresa'))
                    actividad = str(row.get('Actividad'))
                    nombre_empleado = str(row.get('Nombre empleado'))
                    apellido_empleado = str(row.get('Apellido empleado'))

                    #Luego considerando el valor del código ingresado para validar, 
                    #se forma una condición para buscarlo en la lista contenida
                    #por la varible "codigos", en caso sean iguales, se van agregando
                    #los demás datos que le acompañan como el dni, nombre_empresa,
                    #actividad, nombre_empleado y apellido_empleado en una lista 
                    #llamada "persona_ingresada"
                    #Con la lista persona_ingresada se arma otra condición para
                    #imprimir por pantalla si tiene o no acceso provincial.

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

        elif not file_exists: #En caso no exista informa que no hay registro alguno y vuelve a consultar.
            
            print('No se puede validar los datos ingresados,porque no existe registro alguno')
            consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))
            
            principal.menu(consulta)

        '''
        En esta parte, el código que se muestra es para saber si existe un segundo archivo csv
        llamado "ingreso provincial", en donde quedará asentado los ingresos  provinciales.
        '''
        #Se verifica si el archivo "ingresoprovincial.csv" existe o no.

        file_exists = os.path.isfile('ingresoprovincial.csv')

        #En caso, no exista el archivo, crearlo desde cero, agregando el encabezado y las 
        #filas de acuerdo a su respectiva columna. 

        if not file_exists:
            
            with open('ingresoprovincial.csv', 'w', newline='') as fd:
                header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                writer = csv.DictWriter(fd, fieldnames=header)
                writer.writeheader()

                #Se arma una condición usando la lista "persona_ingresa", para buscar 
                #si el código que se valida está en ella y así dejar almacenado en el 
                #segundo archivo csv "ingresoprovincial" su ingreso.

                if codigo in persona_ingresada:
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Validar otro dato, ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))        
                        
            fd.close() 

        #En caso, exista el archivo, agregar filas.

        elif file_exists:
                        
            with open('ingresoprovincial.csv', 'a', newline='') as fd:
                header = ['Codigo', 'DNI', 'Nombre empresa', 'Actividad','Nombre empleado', 'Apellido empleado']
                writer = csv.DictWriter(fd, fieldnames=header)

                #sin agregar el encabezado, para esto se armó la condición, sino existe 
                # escribirlo y si ya existe no lo toma en cuenta. 

                if not file_exists:
                    writer.writeheader()

                #Se arma igualmente una condición usando la lista "persona_ingresa", para buscar 
                #si el código que se valida está en ella y así dejar almacenado en el 
                #segundo archivo csv "ingresoprovincial" su ingreso.

                if codigo in persona_ingresada:
                    writer.writerow({'Codigo': codigo, 'DNI': dni, 'Nombre empresa': nombre_empresa, 'Actividad': actividad, 'Nombre empleado': nombre_empleado, 'Apellido empleado': apellido_empleado})
                    codigo = int(input('Validar otro dato, ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))  
           
            fd.close()

    elif codigo == 3:
        print('Ha salido del programa') #Si el código es igual a tres sale del programa.
                           
    else:

        #Y si se ingresaotra opción que no sea numérica entera, indicar que no corresponde
        #y que lo vuelve a intentar nuevamente.

        print('El valor ingresado no corresponde, intente nuevamente.')
        
        try:
            codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n'))

            #Capturando error de excepción para los datos que ingresen diferente al formato indicado.

        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            codigo = int(input('Ingrese "CÓDIGO DE CIRCULACIÓN":\n Ingrese 3, para salir\n')) 

    
if __name__ == "__main__":
    
    ingresa()