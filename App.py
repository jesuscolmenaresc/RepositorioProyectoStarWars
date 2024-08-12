import requests as rq
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Personaje import Personaje
from Mision import Mision
import csv
import matplotlib.pyplot as plt
import pandas as pd

class App:
    # Clase principal de la aplicacion que gestion la interacción del usuario y la carga de datos asi como los menús

    peliculas_obj = [] # Type: list
    especies_obj = [] # Type: list
    planetas_obj  = [] # Type: list
    personajes_obj = [] # Type: list
    misiones_obj = [] # Type: list
    nombres_planetas = [] # Type: list
    nombres_naves = [] # Type: list
    nombres_armas = [] # Type: list
    nombres_integrantes = [] # Type: list

    def start(self):
        # Este modulo llama la carga de datos del programa utilizando la api swapi.dev y posteriormente inicia la aplicacion

        print('''BIENVENIDO
Iniciando carga de datos, por favor espere...''')
        # Carga de datos
        self.cargar_datos_peliculas()
        print('Peliculas ha sido cargado exitosamente...')
        self.cargar_datos_especies()
        print('Especies ha sido cargado exitosamente...')
        self.cargar_datos_planetas()
        print('Planetas ha sido cargado exitosamente...')
        self.cargar_datos_personajes()
        print(f'Personajes ha sido cargado exitosamente...')

        self.menu()

    def menu(self):
        # Menú de la aplicación, para que el usuario pueda acceder a cada caracteristica
        
        while True:
            print('''----------------------------------------'
MENU
----------------------------------------
1. Lista de Peliculas de la saga
2. Lista de las especies de seres vivos de la saga
3. Lista de planetas
4. Buscar personaje
5. Grafico de cantidad de personajes nacidos en cada planeta
6. Grafico de caracteristicas de naves
7. Tabla de estadisticas sobre naves
8. Misiones
0. Salir
----------------------------------------''')
            opcion_menu = (input('Seleccione una opcion: ')).strip()

            if opcion_menu == '1':
                self.peliculas_saga()

                # Este while True se realizó con el objetivo de que el usuario pueda regresar al menú anterior cuando termine la acción
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue

            elif opcion_menu == '2':
                self.especies_saga()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue

            elif opcion_menu == '3':
                self.planetas_saga()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue                
                
            elif opcion_menu == '4':
                self.personajes_saga()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue  

            elif opcion_menu == '5':
                self.grafico_cantidad_personas()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue  

            elif opcion_menu == '6':
                self.graficos_caracteristicas()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue  
            
            elif opcion_menu == '7':
                self.tablas_naves()
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')

            elif opcion_menu == '8':
                self.submenu_misiones()

            elif opcion_menu == '0':
                print('Saliendo...')
                break
            else:
                print('Opcion invalida')
                continue


    def personajes_saga(self):
        # Se ejecuta la opcion 4 del menu principal, utilizando un algoritmo de busqueda lineal
        nombre_input = ((input('Escriba el nombre del personaje que desea buscar: ')).strip()).lower()
        for personaje in self.personajes_obj: 
            if nombre_input in (personaje.name).lower():
                Personaje.show(personaje)
   
    def cargar_datos_personajes(self):
        # Se cargan los datos de la API swapi.dev y se guardan en variable self.personajes_obj

        personajes = []

        url = 'https://swapi.dev/api/people/'
        while True: # Dado que los datos se encuentran en distinas paginas, se utiliza la key 'next' para obtener la siguiente pagina
                db = rq.get(url).json()
                personajes.extend(db['results'])
                url = db['next']
                if url is None:
                    break
                else:
                    continue   
        
        for personaje in personajes:
            nombre = personaje['name']
            genero = personaje['gender']

            nombre_especie = 'Desconocido'
            for especie in self.especies_obj:
                if nombre in especie.nombre_personajes_especie:
                    nombre_especie = especie.name

            nombre_planeta_origen = 'Desconocido'
            for planeta in self.planetas_obj:
                if nombre in planeta.nombre_personajes_planeta:
                    nombre_planeta_origen = planeta.name
            
            nombre_episodios_aparece = []

            for pelicula in self.peliculas_obj:
                if nombre in pelicula.nombres_personajes:
                    nombre_episodios_aparece.append(pelicula.title)

            nombre_naves_utiliza = []

            urls_naves_utiliza = personaje['starships']

            for url_nave_utiliza in urls_naves_utiliza:
                db_aux = rq.get(url_nave_utiliza).json()
                nombre_naves_utiliza.append(db_aux['name'])

            nombre_vehiculos_utiliza = []

            urls_vehiculos_utiliza = personaje['vehicles']

            for url_vehiculo_utiliza in urls_vehiculos_utiliza:
                db_aux = rq.get(url_vehiculo_utiliza).json()
                nombre_vehiculos_utiliza.append(db_aux['name'])

            self.personajes_obj.append(Personaje(nombre, nombre_planeta_origen, nombre_episodios_aparece, genero, nombre_especie, nombre_naves_utiliza, nombre_vehiculos_utiliza))

    def peliculas_saga(self):
        # Se ejecuta la opcion 1 del menu, se recorre toda la lista de objetos y se muestran los datos de la pelicula
        for pelicula in self.peliculas_obj:
            Pelicula.show(pelicula)

    def cargar_datos_peliculas(self):

        # Se cargan los datos de API swapi.dev y se guardan en una variable

        url = 'https://swapi.dev/api/films/'
        db = rq.get(url).json()

        # Se crea una lista de peliculas a partir de la base de datos
        peliculas = db['results']

        for pelicula in peliculas:
            titulo = pelicula['title']
            numero_episodio = pelicula['episode_id']
            fecha_lanzamiento = pelicula['release_date']
            opening_crawl = pelicula['opening_crawl']
            director = pelicula['director']
            url_especies_lista = pelicula['species']
            nombres_especies = []
            for url_especie in url_especies_lista:
                db_aux = rq.get(url_especie).json()
                nombre_especie = db_aux['name']
                nombres_especies.append(nombre_especie)
                
            url_planetas_lista = pelicula['planets']
            nombres_planetas = []
            for url_planeta in url_planetas_lista:
                db_aux = rq.get(url_planeta).json()
                nombre_planeta = db_aux['name']
                nombres_planetas.append(nombre_planeta)

            url_personajes_lista = pelicula['characters']
            nombres_personajes = []
            for url_personaje in url_personajes_lista:
                db_aux = rq.get(url_personaje).json()
                nombre_personaje = db_aux['name']
                nombres_personajes.append(nombre_personaje)

            self.peliculas_obj.append(Pelicula(titulo,numero_episodio,fecha_lanzamiento,opening_crawl,director,nombres_especies,nombres_planetas, nombres_personajes))

    def especies_saga(self):
        # Se ejecuta la opcion 3 del menu principal recorriendo la lista de especies e imprimiendo
        for especie in self.especies_obj:
            Especie.show(especie)

    def cargar_datos_especies(self):

        # Se cargan los datos de la API swapi.dev

        especies = []

        url = f'https://swapi.dev/api/species'
        while True: # Dado que los datos se encuentran en distinas paginas, se utiliza la key 'next' para obtener la siguiente pagina
                db = rq.get(url).json()
                especies.extend(db['results'])
                url = db['next']
                if url is None:
                    break
                else:
                    continue   

        for especie in especies:
            nombre = especie['name']
            clasificacion = especie['classification']
            altura = especie['average_height']
            url_planeta = especie['homeworld']
            if url_planeta is None:
                planeta = 'Unknown'
            else:
                db_aux = rq.get(url_planeta).json()
                planeta = db_aux['name']
            
            lengua_materna = especie['language']

            # Nombre de personajes donde aparece

            url_personajes_lista = especie['people']
            nombres_personajes = []

            for url_personaje in url_personajes_lista:
                db_aux = rq.get(url_personaje).json()
                nombre_personaje = db_aux['name']
                nombres_personajes.append(nombre_personaje)

            # Nombres de los episodios que aparece

            episodios_especie = []

            for pelicula in self.peliculas_obj:
                if nombre in pelicula.nombres_especies:
                    episodios_especie.append(pelicula)

            nombre_episodios = []

            for episodio in episodios_especie:
                nombre_episodios.append(episodio.title)

            self.especies_obj.append(Especie(nombre, altura, planeta, lengua_materna, clasificacion, nombres_personajes, nombre_episodios))

    def planetas_saga(self):
        # Se ejecuta la opcion 2 del menu principal
        for planeta in self.planetas_obj:
            Planeta.show(planeta)

    def cargar_datos_planetas(self):
        # Se cargan los datos de la API swapi.dev
        planetas = []

        url = 'https://swapi.dev/api/planets'
        while True:
                db = rq.get(url).json()
                planetas.extend(db['results'])
                url = db['next']
                if url is None:
                    break
                else:
                    continue   

        for planeta in planetas:
            nombre = planeta['name']
            periodo_orbita = planeta['orbital_period']
            periodo_rotacion = planeta['rotation_period'] 
            poblacion = planeta['population']
            clima = planeta['climate']
            urls_personajes_planeta = planeta['residents']
            
            # Buscar los nombres de los episodios que aparece el planeta

            nombre_episodios = []

            for pelicula in self.peliculas_obj:
                if nombre in pelicula.nombres_planetas:
                    nombre_episodios.append(pelicula.title)

            # Buscar los nombres de los personajes cuyo origen es el planeta
            
            nombre_personajes_planeta = []

            for url_personaje_planeta in urls_personajes_planeta:
                db = rq.get(url_personaje_planeta).json()
                nombre_personajes_planeta.append(db['name'])

            self.planetas_obj.append(Planeta(nombre, periodo_rotacion, periodo_orbita, clima, poblacion, nombre_episodios, nombre_personajes_planeta))

    def submenu_misiones(self):
        # Se ejecuta la opcion 8 del menu principal
        # Se crea un nuevo submenu para acceder a cada una de las opciones dentro de las misiones
        while True:
            print('''----------------------------------------
SUBMENÚ MISIONES
----------------------------------------
1. Agregar misión
2. Modificar misión
3. Visualizar misión
4. Guardar misiones
5. Cargar misiones
0. Volver al menú principal
----------------------------------------''')
            opcion = input('Seleccione una opción del submenú misiones: ').strip()

            if opcion == '1':
                self.agregar_mision()
            elif opcion == '2':
                self.modificar_mision()
            elif opcion == '3':
                self.visualizar_mision()
            elif opcion == '4':
                self.guardar_misiones()
            elif opcion == '5':
                self.cargar_misiones()
            elif opcion == '0':
                break
            else:
                print("Opción inválida.")
                continue

    def agregar_mision(self):
        # Agregar Mision
        # Se ejecuta la opción 1 del submenu misiones
        if len(self.misiones_obj) >= 5: # Se establece un limite de misiones para sobrecargar el programa
            print("No puedes definir más de 5 misiones.")
            return

        nombre = input("Ingrese el nombre de la misión: ")

        # Se lee la base de datos a partir de los archivos en formato csv
        db = open('planets.csv')
        reader = csv.reader(db)
        next(reader) # Se pasa a la siguiente fila dentro del archivo para saltarse el encabezado
        for fila in reader:
            nombre_planeta = fila[1]
            self.nombres_planetas.append(nombre_planeta)

        print('''----------------------------------------
PLANETAS:''')

        for planeta in self.nombres_planetas: # Se muestran todos los planetas
            print(f'-.{planeta}')

        while True:
            planeta_input = ((input("Ingrese el planeta destino: ")).strip()).lower()

            planeta_mision = None

            # Busqueda lineal para encontrar el planeta que coincide con la busqueda y guardarlo
            for planeta in self.nombres_planetas: 
                if planeta_input in (planeta).lower():
                    planeta_mision = planeta

            if planeta_mision == None:
                print('No se ha encontrado el planeta')
                continue
            else:
                print(f'Se ha seleccionado el planeta: {planeta_mision}')
                break

        # Se lee la base de datos a partir de los archivos en formato csv
        db = open('starships.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_nave = fila[1]
            self.nombres_naves.append(nombre_nave)

        print('''----------------------------------------
NAVES:''')

        for nave in self.nombres_naves: # Se muestran todas las naves
            print(f'-.{nave}')

        while True:
            nave_input = input("Ingrese la nave a utilizar: ")

            nave_mision = None

            # Se utiliza algoritmo de busqueda lineal y se guarda aquel que coincide con la busqueda del usuario
            for nave in self.nombres_naves:
                if nave_input in (nave).lower():
                    nave_mision = nave

            if nave_mision == None:
                print('No se ha encontrado la nave')
                continue
            else:
                print(f'Se ha seleccionado la nave: {nave_mision}')
                break

        # Se lee la base de datos a partir de los archivos en formato csv
        db = open('weapons.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_arma = fila[1]
            self.nombres_armas.append(nombre_arma)

        print('''----------------------------------------
ARMAS:''')

        # Se muestran todas las armas posibles
        for arma in self.nombres_armas:
            print(f'-.{arma}')

        armas_mision = []
        
        while True: 
            if len(armas_mision) >= 7: # Se verifica que se guarden un maximo de 7 armas
                break
            else:
                while True:
                    arma_mision = None
                    arma_input = input("Ingrese arma a utilizar (o presione Enter para no seleccionar un arma): ")

                    if arma_input == '': # Si se presiona Enter, quedara vacio este slot del arma
                        arma_mision = 'No seleccionado'
                        print('No se ha seleccionado ningun arma')
                        break

                    for arma in self.nombres_armas: # Si se escribe un nombre, lo buscara para posteriormente guardar el arma que coincida
                        if arma_input in (arma).lower():
                            arma_mision = arma
                            print(f'Se ha seleccionado el arma {arma}')   
                            break

                    if arma_mision == None: # Si no se encuentra ninguna coincidencia volvera al while True
                        print('No se ha encontrado el arma')
                        continue
                    
                    break
                armas_mision.append(arma_mision)
   
        # Se lee la base de datos a partir de los archivos en formato csv
        db = open('characters.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_integrante = fila[1]
            self.nombres_integrantes.append(nombre_integrante)

        print('''----------------------------------------
INTEGRANTES:''')

        for integrante in self.nombres_integrantes: # Se muestran los integrantes
            print(f'-.{integrante}')

        integrantes_mision = []
        
        # Se repite el algoritmo utilizado en la parte de seleccion de armas
        while True: 
            if len(integrantes_mision) >= 7:
                break
            else:
                while True:
                    integrante_mision = None
                    integrante_input = input("Ingrese integrante (o presione Enter para no seleccionar ningun integrante): ")

                    if integrante_input == '':
                        integrante_mision = 'No seleccionado'
                        print('No se ha seleccionado ningun integrante')
                        break

                    for integrante in self.nombres_integrantes:
                        if integrante_input in (integrante).lower():
                            integrante_mision = integrante
                            print(f'Se ha seleccionado el integrante {integrante}')   
                            break

                    if integrante_mision in integrantes_mision:
                        print('El integrante ya se encuentra en la mision')
                        continue
                    
                    if integrante_mision == None:
                        print('No se ha encontrado el integrante')
                        continue
                    
                    break
                integrantes_mision.append(integrante_mision)

        # Se guarda la mision como un objeto 
        mision = Mision(nombre, planeta_mision, nave_mision, armas_mision, integrantes_mision)

        self.misiones_obj.append(mision)
        print("Misión agregada exitosamente.")


    def modificar_mision(self):
        # Modificar Mision
        # Se ejecuta la opcion 2 del submenu de misiones
        if self.misiones_obj == []: # Si la lista de misiones esta vacia no se ejecuta el codigo
            print('No existen misiones creadas.') 
            return

        # Se muestran los nombres de las misiones
        for mision in self.misiones_obj:
            print('-. {mision.nombre}')

        nombre_mision_input = input("Ingrese el nombre de la misión a modificar: ")

        # Se busca si existe alguna mision con el nombre que se acaba de ingresar

        for m in self.misiones_obj:
            if m.nombre == nombre_mision_input:
                mision = m
                break

        if not mision:
            print("Misión no encontrada.")
            return

        print("Selecciona el atributo de la misión que deseas modificar:")
        print("1. Nave")
        print("2. Armas")
        print("3. Integrantes")
        opcion = input("Escribe el número de la opción que deseas modificar: ")

        if opcion == '1': # Se modifica la nave, mostrando las naves existentes y sobreescribiendola en la anterior

            print('''----------------------------------------
NAVES:''')

            for nave in self.nombres_naves:
                print(f'-.{nave}')

            while True:
                nave_input = input("Ingrese la nave a utilizar: ")
                nave_mision = None
                for nave in self.nombres_naves:
                    if nave_input in (nave).lower():
                        nave_mision = nave

                if nave_mision == None:
                    print('No se ha encontrado la nave')
                    continue
                else:
                    mision.nave = nave_mision
                    print(f'Se ha actualiza la nave: {nave}')
                    break

            print("Nave actualizada exitosamente.")

        elif opcion == '2': 
            print("Actualmente las armas de la misión son: ")
            for arma in mision.armas:
                print(f'-. {arma}')

            decision = input("¿Deseas agregar o eliminar armas? (agregar/eliminar): ")

            if (decision.lower()).strip() == 'agregar':

                while len(mision.armas) < 7: # Verifica que hayan menos de 7 armas guardadas

                    for arma in self.nombres_armas: # Muestra las armas disponibles
                        print(f'-.{arma}')

                    nueva_arma = ((input("Ingrese la nueva arma a añadir o escriba 'salir' para terminar: ")).lower()).strip()
                    if nueva_arma.lower() == 'salir':
                        break
                    else:
                        arma_agregar = None
                        for arma in self.nombres_armas:
                            if nueva_arma in (arma).lower():  
                                arma_agregar = arma

                        if arma_agregar == None:
                            print('No se ha encontrado el arma')
                            continue
                        else:
                            mision.armas.append(arma_agregar)
                            print(f"Arma {arma_agregar} añadida.") # Si el arma se encontro, se agrega a la lista de armas de la mision
                            break
                
                if len(mision.armas) == 7:
                    print("Has alcanzado el máximo número de armas permitidas (7).")

            elif (decision.lower()).strip() == 'eliminar':
                arma_a_eliminar = (input("Ingrese el arma a eliminar: ").lower()).strip()
                arma_eliminada = None

                for arma in mision.armas:
                    if arma_a_eliminar in arma.lower():
                        arma_eliminada = arma
                        mision.armas.remove(arma_eliminada) # Cuando tiene identificado el nombre del arma la busca y la elimimna
                        print(f"Arma {arma_eliminada} eliminada.")
                        break

                if arma_eliminada == None:
                    print("El arma no se encuentra en la lista.")

            else:
                print("Opción no válida.")

        elif opcion == '3': # La modificacion de integrantes se da igual que la modificacion de armas del apartado anterior
            print("Actualmente los integrantes de la misión son: ")
            for integrante in mision.integrantes:
                print(f'-. {integrante}')

            decision = input("¿Deseas agregar o eliminar integrantes? (agregar/eliminar): ")

            if (decision.lower()).strip() == 'agregar':

                while len(mision.integrantes) < 7:

                    for integrante in self.nombres_integrantes:
                        print(f'-.{integrante}')

                    nuevo_integrante = ((input("Ingrese el nuevo integrante a añadir o escriba 'salir' para terminar: ")).lower()).strip()
                    if nuevo_integrante == 'salir':
                        break
                    else:
                        integrante_agregar = None
                        for integrante in self.nombres_integrantes:
                            if nuevo_integrante in (integrante).lower():  
                                integrante_agregar = integrante
                                break

                        if integrante_agregar == None:
                            print('No se ha encontrado el integrante')
                            continue
                        else:
                            mision.integrantes.append(integrante_agregar)
                            print(f"Integrante {integrante_agregar} añadido.")
                            break

                if len(mision.integrantes) == 7:
                    print("Has alcanzado el máximo número de integrantes permitidos (7).")

            elif (decision.lower()).strip() == 'eliminar':
                integrante_a_eliminar = (input("Ingrese el integrante a eliminar: ").lower()).strip()
                integrante_eliminado = None

                for integrante in mision.integrantes:
                    if integrante_a_eliminar in integrante.lower():
                        integrante_eliminado = integrante
                        mision.integrantes.remove(integrante_eliminado)
                        print(f"Integrante {integrante_eliminado} eliminado.")

                if integrante_eliminado == None:
                    print("El integrante no se encuentra en la lista.")

            else:
                print("Opción no válida.")

        else:
            print("Opción no válida.")


    def visualizar_mision(self):
        # Visualizar mision
        # Se ejecuta la opcion 3 del submenu misiones
        for m in self.misiones_obj: # Se muestran los nombres de las misiones
            print(f'-. {m.nombre}')
        nombre_mision_input = input("Ingrese el nombre de la misión a visualizar: ")

        # Se busca si existe alguna mision con el nombre que se acaba de ingresar

        for m in self.misiones_obj:
            if m.nombre == nombre_mision_input:
                mision = m
                break

        if mision:
            mision.mostrar_detalle() # Se muestra los detalles de la mision
        else:
            print("Misión no encontrada.")


    def guardar_misiones(self):
        # Guardar misiones
        # Se ejecuta la opcion 4 del submenu misiones 
        # Se abre el archivo en modo de escritura
        with open('misiones.txt', 'w') as file:
            for mision in self.misiones_obj:
                # Se agrega el separador '|' entre armas para que ',' sea solo para separar atributos principales
                armas = '|'.join(mision.armas)

                # Se agrega el separador ';' entre integrantes para que ',' sea solo para separar atributos principales
                integrantes = ';'.join(mision.integrantes)

                file.write(f"{mision.nombre},{mision.planeta_destino},{mision.nave},{armas},{integrantes}\n")
        print("Misiones guardadas exitosamente.")

    def cargar_misiones(self):
        # Cargar misiones
        # Se ejecuta la opcion 5 del submenu de misiones

        # Se utiliza el comando try porque si el archivo no existe y se obtiene un error no se detenga el programa
        try:
            # Intentar abrir el archivo en modo de lectura
            with open('misiones.txt', 'r') as archivo:
                self.misiones_obj = []  # Limpiar la lista actual de misiones para evitar duplicados, guardandose los datos que existan en el archivo misiones
                for linea in archivo:
                    nombre, planeta_destino, nave, armas_str, integrantes_str = linea.strip().split(',')

                    # El separador '|' entre armas es para que ',' separe los atributos principales de la mision
                    armas = armas_str.split('|')

                    # El separador ';' entre integrantes es para que ',' separe los atributos principales de la mision
                    integrantes = integrantes_str.split(';')
                    mision = Mision(nombre, planeta_destino, nave, armas, integrantes) # Se guarda la mision como objeto

                    self.misiones_obj.append(mision) # Se anexa a la lista misiones
            print("Misiones cargadas exitosamente.")

        except FileNotFoundError:
            # Si el archivo no existe, se crea un archivo vacío
            open('misiones.txt', 'w').close()
            print("No se encontró el archivo de misiones, se ha creado un archivo nuevo.")

            self.misiones_obj = [] 

        except Exception as e: # Si existe cualquier otro error en la lectura del archivo, puede ser por formato
            print(f"Error al cargar misiones: {str(e)}")

    def personajes_en_cada_planeta(self):
        # Se crean las listas para los graficos del apartado 5 del menu principal

        # Se lee la base de datos a partir del csv
        info =open('characters.csv', 'r')
        planetas={}
        caracteres= csv.DictReader(info)
        for elementos in caracteres: # Se recorre cada diccionario
            planeta=elementos['homeworld']

            # Si la llave no existe, se crea, si existe, se suma un elemento
            if planeta in planetas:
                planetas[planeta]+=1
            else:
                planetas[planeta]=1

        personajes_planeta=list(planetas.keys()) # Se crea una lista con las llaves del diccionario
        cantidad_personajes_planeta=list(planetas.values()) # Se crea una lista con los valores del diccionario
        info.close() # Se cierra el archivo
        return personajes_planeta, cantidad_personajes_planeta

    def grafico_cantidad_personas(self):
        # Se ejecuta la opcion 5 del menu principal
        # Se crea grafico con la herramienta matplotlib

        personaje_planeta, cantidad_personajes_planeta = self.personajes_en_cada_planeta()
        fig, ax= plt.subplots()
        plt.bar(personaje_planeta,cantidad_personajes_planeta)
        plt.xlabel('personaje por planeta')
        plt.ylabel('Numero de personajes nacidos en un planeta')
        plt.title('Planeta de nacimiento de los personajes')
        plt.xticks(rotation=45,ha='right')
        plt.show()

    def longitud_naves(self):
        # Se crea un diccionario con las llaves de las naves y su longitud  
        info=open('starships.csv','r')
        longitud_naves={}
        caracteres=csv.DictReader(info)  
        for elementos in caracteres:
            longitud_naves[elementos['name']]=(float((elementos['length'])))/100 # es del tipo: float y se escalan los datos para tener mejor lectura
        info.close()
        return longitud_naves

    def capacidad_carga(self):
        # Se crea un diccionario con las llaves de las naves y su capacidad de carga  
        info=open('starships.csv','r')
        capacidad_carga={}
        caracteres=csv.DictReader(info) 
        for elementos in caracteres:
            if elementos['cargo_capacity'] == '': # Dado que existen elementos vacios se le asigna un valor de 0
                elementos['cargo_capacity'] = 0
            capacidad_carga[elementos['name']]=float((elementos['cargo_capacity']))/1000000 # es del tipo: float y se escalan los datos para tener mejor lectura
        info.close()
        return capacidad_carga

    def clasificacion_hiperimpulsor(self):
        # Se crea un diccionario con las llaves de las naves y su calificacion del hiperimpulsor  
        info=open('starships.csv', 'r')
        clasificacion_hiperimpulsor = {}
        caracteres=csv.DictReader(info)
        for elementos in caracteres:
            if elementos['hyperdrive_rating'] == '': # Dado que existen elementos vacios se le asigna un valor de 0
                elementos['hyperdrive_rating'] = 0
            clasificacion_hiperimpulsor[elementos['name']] = (float((elementos['hyperdrive_rating'])))*10  # es del tipo: float y se escalan los datos para tener mejor lectura
        info.close()
        return clasificacion_hiperimpulsor

    def MGLT_naves(self):
        # Se crea un diccionario con las llaves de las naves y sus "megaluz por hora" MGLT
        info=open('starships.csv', 'r')
        MGLT_naves={}
        caracteres = csv.DictReader(info)
        for elementos in caracteres:
            if elementos['MGLT'] == '': # Dado que existen elementos vacios se le asigna un valor de 0
                elementos['MGLT'] = 0
            MGLT_naves[elementos['name']] = float((elementos['MGLT']))  # es del tipo: float y se escalan los datos para tener mejor lectura
        info.close()
        return MGLT_naves

    def graficos_caracteristicas(self):
        # Se ejecuta la opcion 6 del menu principal

        # Se leen los datos de los diccionarios
        naves_longitud = self.longitud_naves()
        naves_capacidad_carga = self.capacidad_carga()
        naves_calificacion_hiperimpulsor = self.clasificacion_hiperimpulsor()
        naves_mglt = self.MGLT_naves()

        # Se obtiene una lista de llaves y una lista de cada valor
        naves = list(naves_longitud.keys()) # Se obtienen una lista de llaves ordenadas
        longitudes = list(naves_longitud.values())
        capacidades_carga = list(naves_capacidad_carga.values())
        calificaciones_hiperimpulsor = list(naves_calificacion_hiperimpulsor.values())
        mglts = list(naves_mglt.values())

        # Se crea el gráfico
        fig, ax = plt.subplots()

        # Se agregan las barras para cada característica
        ax.bar(naves, longitudes, label=('Longitud (x10^2)'))
        ax.bar(naves, capacidades_carga, bottom=longitudes, label=('Capacidad de carga (x10^6)'))
        ax.bar(naves, calificaciones_hiperimpulsor, bottom=[x + y for x, y in zip(longitudes, capacidades_carga)], label=('Clasificación de hiperimpulsor (x10^-1)'))
        ax.bar(naves, mglts, bottom=[x + y + z for x, y, z in zip(longitudes, capacidades_carga, calificaciones_hiperimpulsor)], label='MGLT (x10^1)')

        # Se agrega el titulo, la leyenda, lectura del eje y, se muestra el grafico
        ax.set_title('Características de naves')
        ax.legend()
        plt.xticks(rotation=45,ha='right')
        plt.ylabel('Cantidad de atributos')

        plt.show()

    def tablas_naves(self):
        # Se ejecuta la parte 7 del menu principal

        ruta = 'starships.csv' 
        df = pd.read_csv(ruta) # Se lee el archivo con la libreria pandas

        # Se seleccionan las columnas que se necesitan como un dataframe
        estadisticas_df = df[['starship_class', 'hyperdrive_rating', 'MGLT', 'max_atmosphering_speed', 'cost_in_credits']]

        # Se calculan las estadísticas para "Calificación de hiperimpulsor"
        hyperdrive_estadisticas = estadisticas_df.groupby('starship_class').agg(
            hyperdrive_media=('hyperdrive_rating', 'mean'),
            hyperdrive_moda=('hyperdrive_rating', lambda x: x.mode()[0] if not x.mode().empty else None),
            hyperdrive_minimo=('hyperdrive_rating', 'min'),
            hyperdrive_maximo=('hyperdrive_rating', 'max')
        ).reset_index()

        # Se redondean los decimales y los valores que tengan NaN se modifican por un guion
        hyperdrive_estadisticas = hyperdrive_estadisticas.round(2).fillna("-")

        # Se renombran las columnas de hyperdrive_estadisticas para que tenga nombre en español
        hyperdrive_estadisticas.columns = ['Clase de Nave', 'Media', 'Moda', 'Mínimo', 'Máximo']

        # Se calculan las estadísticas para "MGLT"
        MGLT_estadisticas = estadisticas_df.groupby('starship_class').agg(
            MGLT_media=('MGLT', 'mean'),
            MGLT_moda=('MGLT', lambda x: x.mode()[0] if not x.mode().empty else None),
            MGLT_minimo=('MGLT', 'min'),
            MGLT_maximo=('MGLT', 'max')
        ).reset_index()

        # Se redondean los decimales y los valores que tengan NaN se modifican por un guion
        MGLT_estadisticas = MGLT_estadisticas.round(2).fillna("-")

        # Se renombran las columnas de MGLT_estadisticas para que tenga nombre en español
        MGLT_estadisticas.columns = ['Clase de Nave', 'Media', 'Moda', 'Mínimo', 'Máximo']

        # Se calculan las estadísticas para "Velocidad máxima en atmósfera"
        max_speed_estadisticas = estadisticas_df.groupby('starship_class').agg(
            max_speed_media=('max_atmosphering_speed', 'mean'),
            max_speed_moda=('max_atmosphering_speed', lambda x: x.mode()[0] if not x.mode().empty else None),
            max_speed_minimo=('max_atmosphering_speed', 'min'),
            max_speed_maximo=('max_atmosphering_speed', 'max')
        ).reset_index()

        # Se redondean los decimales y los valores que tengan NaN se modifican por un guion
        max_speed_estadisticas = max_speed_estadisticas.round(2).fillna("-")

        # Se renombran las columnas de max_speed__estadisticas para que tenga nombre en español
        max_speed_estadisticas.columns = ['Clase de Nave', 'Media', 'Moda', 'Mínimo', 'Máximo']

        # Se calculan las estadísticas para "Costo (en créditos)"
        cost_estadisticas = estadisticas_df.groupby('starship_class').agg(
            cost_media=('cost_in_credits', 'mean'),
            cost_moda=('cost_in_credits', lambda x: x.mode()[0] if not x.mode().empty else None),
            cost_minimo=('cost_in_credits', 'min'),
            cost_maximo=('cost_in_credits', 'max')
        ).reset_index()

        # Se redondean los decimales y los valores que tengan NaN se modifican por un guion
        cost_estadisticas = cost_estadisticas.round(2).fillna("-")

        # Se renombran las columnas de costs__estadisticas para que tenga nombre en español
        cost_estadisticas.columns = ['Clase de Nave', 'Media', 'Moda', 'Mínimo', 'Máximo']

        # Se muestran todas las tablas
        print("---------------------------------------------------------------------")
        print("Estadísticas para 'Clasificación de hiperimpulsor':")
        print(hyperdrive_estadisticas, "\n")

        print("---------------------------------------------------------------------")
        print("Estadísticas para 'MGLT':")
        print(MGLT_estadisticas, "\n")

        print("---------------------------------------------------------------------")
        print("Estadísticas para 'Velocidad máxima en atmósfera':")
        print(max_speed_estadisticas, "\n")

        print("---------------------------------------------------------------------")
        print("Estadísticas para 'Costo (en créditos)':")
        print(cost_estadisticas, "\n")
        print("---------------------------------------------------------------------")