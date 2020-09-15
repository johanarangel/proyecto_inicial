# Devolución 1
Fecha: 19-Septiembre-2020\
Autor: Hernán Contigiani

## Funcionamiento general del programa
El programa en general está muy bien realizado, como siempre los programas que nos has entregado son super prolijos lo cual permite a un tercero leerlos sin inconvenientes, es muy importante y valioso.

## Comentarios por archivo
#### principal.py
Al comienzo del programa entre la lnea 30 y 36 se está ejecutando código por fuera del bloque principal del programa (main). Sacaría esas líneas en donde se solicita que consulta se desea realizar y las colocaría tal cual está ahí dentro del "if main" abajo de todo (ĺinea 86).

#### funcion_validacion.py
Si por error uno comienza a crear un nuevo registro o entrada, el menu de ingreso de datos en cada caso da la posibilidad de "salir" ingresando 3 o FIN, pero de todas formas si ingreso esos valores el programa continua consultandome los registros de entrada y se termina generando el registro en el archivo. De esa manera sin desearlo conseguí ingresar esto en el archivo:\
123,3,FIN,FIN,FIN,FIN

#### validar_ingreso.py
Si por error la primera vez que se ejecuta el programa (sin ningún CSV creado) uno entra al menú "2" de validar ingreso, el sistema explota porque intenta abrir el archivo CSV que no existe aún (validacionempresas.csv). Faltaría comtemplar ese caso.

#### Comentarios
- El proyecto alcanza los conceptos vistos en la cursada, excelente el uso de funciones y archivos.
- Destaco el diseño del proyecto, muy bien resuelto y encarado lo cual se ve reflejado en la prolijidad y lectura del código.
- Muy pero muy bien realizado el readme, de los mejores realizados este año. En cuanto entre a ver el proyecto me dieron ganas de ver de que se trataba.
