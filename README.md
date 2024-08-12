## RepositorioProyectoStarWars
Proyecto Algoritmos y Programacion // Colmenares Jesus // Izquierdo Grecia // Marrufo Jose

## Requisitos

Se deben instalar las librerias requests, matplotlib y pandas.

- Requests: `pip install requests`
- Matplotlib: `pip install matplotlib`
- Pandas: `pip install pandas`

## Ejecucion

Para ejecutar el proyecto, se debe correr el archivo `main.py`:

## Funcionalidad

El programa puede realizar las siguientes acciones:

- Lista de Películas: Muestra la lista de películas de la saga.
- Especies: Muestra las especies de la saga.
- Planetas: Muestra los planetas de la saga.
- Personajes: Permite buscar y mostrar información sobre los personajes.
- Misiones: Gestiona la creación y modificación de misiones.
- Gráficos: Muestra gráficos sobre datos de personajes y naves.

## Instrucciones

En el menu principal tiene 8 opciones diferentes del menu para navegar.

- La opcion 1 muestra las peliculas de la saga.
- La opcion 2 muestra los seres vivos de la saga.
- La opcion 3 muestra los planetas de la saga.
- La opcion 4 permite buscar los personajes de la saga
  - No es necesario escribir el nombre completo del personaje, el sistema mostrara todas las coincidencias de lo que escriba el usuario.
- La opcion 5 permite visualizar un grafico con la cantidad de personajes nacidos en cada planeta.
- La opcion 6 permite visualizar un grafico apilado de barras con diferentes caracteristicas (las caracteristicas se escalaron para poder tener una mejor visualizacion).
- La opcion 7 permite visualizar 4 tablas en la consola de comandos con diferentes caracteristicas estadisticas para la clase de las naves.
- La opcion 8 permite acceder al menu misiones
  - La opcion 1 del submenu misiones le permite agregar una mision: El programa le preguntara:
    - Nombre de la mision
    - Planeta
    - Nave
    - Armas (7 slots disponibles) (En caso de que quiera dejar el slot vacio presionar Enter)
    - Personajes (7 slots disponibles) (En caso de que quiera dejar el slot vacio presionar Enter)
  - La opcion 2 del submenu permite modificar las misiones, permitiendole seleccionar la mision a modificar
    - La opcion 1 de este submenu permite cambiar la nave de la mision
    - La opcion 2 de este submenu permite eliminar/agregar arma
    - La opcion 3 de este submenu permite eliminar/agregar personaje
  - La opcion 3 del submenu permite visualizar los datos de las misiones existentes
  - La opcion 4 del submenu permite guardar los datos de las misiones en un archivo en formato .txt
  - La opcion 5 del submenu permite cargar los datos de las misiones desde un archivo en formato .txt sobreescribiendola sobre los datos que tenga cargado el programa