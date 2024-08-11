import requests as rq
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Personaje import Personaje
from Mision import Mision
import csv

class App:
    peliculas_obj = []
    especies_obj = []
    planetas_obj  = []
    personajes_obj = []
    misiones_obj = []
    nombres_planetas = []
    nombres_naves = []
    nombres_armas = []
    nombres_integrantes = []

    def start(self):
        print('''BIENVENIDO
Iniciando carga de datos, por favor espere...''')
        # Carga de datos
        # self.cargar_datos_peliculas()
        print('Peliculas ha sido cargado exitosamente...')
        # self.cargar_datos_especies()
        print('Especies ha sido cargado exitosamente...')
        # self.cargar_datos_planetas()
        print('Planetas ha sido cargado exitosamente...')
        # self.cargar_datos_personajes()
        print(f'Personajes ha sido cargado exitosamente...')

        self.menu()

    def menu(self):
        
        while True:
            print('''----------------------------------------'
MENU
----------------------------------------
1. Lista de Peliculas de la saga
2. Lista de las especies de seres vivos de la saga
3. Lista de planetas
4. Buscar personaje
5. Grafico de cantidad de personajes nacidos en cada planeta
6. Informacion sobre naves
7. Misiones
0. Salir
----------------------------------------''')
            opcion_menu = (input('Seleccione una opcion: ')).strip()

            if opcion_menu == '1':
                self.peliculas_saga()
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
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue  

            elif opcion_menu == '6':
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue  

            
            elif opcion_menu == '7':
                self.submenu_misiones()

            elif opcion_menu == '0':
                print('Saliendo...')
                break
            else:
                print('Opcion invalida')
                continue


    def personajes_saga(self):
        nombre_input = ((input('Escriba el nombre del personaje que desea buscar: ')).strip()).lower()
        for personaje in self.personajes_obj: 
            if nombre_input in (personaje.name).lower():
                Personaje.show(personaje)
   
    def cargar_datos_personajes(self):
        # Se cargan los datos de la API y se guardan en una variable

        personajes = []

        url = 'https://swapi.dev/api/people/'
        while True:
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
        for pelicula in self.peliculas_obj:
            Pelicula.show(pelicula)

    def cargar_datos_peliculas(self):

        # Se cargan los datos de API y se guardan en una variable
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
        for especie in self.especies_obj:
            Especie.show(especie)

    def cargar_datos_especies(self):

        # Se cargan los datos de la API

        especies = []

        url = f'https://swapi.dev/api/species'
        while True:
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

            # Buscar los nombres de los episodios que aparece

            episodios_especie = []

            for pelicula in self.peliculas_obj:
                if nombre in pelicula.nombres_especies:
                    episodios_especie.append(pelicula)

            nombre_episodios = []

            for episodio in episodios_especie:
                nombre_episodios.append(episodio.title)

            self.especies_obj.append(Especie(nombre, altura, planeta, lengua_materna, clasificacion, nombres_personajes, nombre_episodios))

    def busqueda_binaria(self,lista,valor):
        low = 0
        high = len(lista) - 1
        while low <= high:
            mid = (low + high) // 2
            if lista[mid] == valor:
                return lista[mid]
            elif lista[mid] < valor:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def planetas_saga(self):
        for planeta in self.planetas_obj:
            Planeta.show(planeta)

    def cargar_datos_planetas(self):
        # Se cargan los datos de la API
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

    # Construir mision
    def agregar_mision(self):
        if len(self.misiones_obj) >= 5:
            print("No puedes definir más de 5 misiones.")
            return

        nombre = input("Ingrese el nombre de la misión: ")

        db = open('planets.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_planeta = fila[1]
            self.nombres_planetas.append(nombre_planeta)

        print('''----------------------------------------
PLANETAS:''')

        for planeta in self.nombres_planetas:
            print(f'-.{planeta}')

        while True:
            planeta_input = ((input("Ingrese el planeta destino: ")).strip()).lower()

            planeta_mision = None

            for planeta in self.nombres_planetas:
                if planeta_input in (planeta).lower():
                    planeta_mision = planeta
                    print(f'Se ha seleccionado el planeta: {planeta}')

            if planeta_mision == None:
                print('No se ha encontrado el planeta')
                continue
            else:
                break


        db = open('starships.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_nave = fila[1]
            self.nombres_naves.append(nombre_nave)

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
                print(f'Se ha seleccionado la nave: {nave}')
                break


        db = open('weapons.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_arma = fila[1]
            self.nombres_armas.append(nombre_arma)

        print('''----------------------------------------
ARMAS:''')

        for arma in self.nombres_armas:
            print(f'-.{arma}')

        armas_mision = []
        
        while True: 
            if len(armas_mision) >= 7:
                break
            else:
                while True:
                    arma_mision = None
                    arma_input = input("Ingrese arma a utilizar (o presione Enter para no seleccionar un arma): ")

                    if arma_input == '':
                        arma_mision = 'No seleccionado'
                        print('No se ha seleccionado ningun arma')
                        break

                    for arma in self.nombres_armas:
                        if arma_input in (arma).lower():
                            arma_mision = arma
                            print(f'Se ha seleccionado el arma {arma}')   
                            break

                    if arma_mision == None:
                        print('No se ha encontrado el arma')
                        continue
                    
                    break
                armas_mision.append(arma_mision)
   

        db = open('characters.csv')
        reader = csv.reader(db)
        next(reader)
        for fila in reader:
            nombre_integrante = fila[1]
            self.nombres_integrantes.append(nombre_integrante)

        print('''----------------------------------------
INTEGRANTES:''')

        for integrante in self.nombres_integrantes:
            print(f'-.{integrante}')

        integrantes_mision = []
        
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

                    if integrante_mision == None:
                        print('No se ha encontrado el integrante')
                        continue
                    
                    break
                integrantes_mision.append(integrante_mision)

        mision = Mision(nombre, planeta_mision, nave_mision, armas_mision, integrantes_mision)

        self.misiones_obj.append(mision)
        print("Misión agregada exitosamente.")

    # Requerimiento I: Modificar Mision
    def modificar_mision(self):
        if self.misiones_obj == []:
            print('No existen misiones creadas.')
            return

        for mision in self.misiones_obj:
            print('-. {mision.nombre}')

        nombre_mision_input = input("Ingrese el nombre de la misión a modificar: ")

        # Esta iteracion busca si existe alguna mision con el nombre que se acaba de ingresar

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

        if opcion == '1':

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

                while len(mision.armas) < 7:

                    for arma in self.nombres_armas:
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
                            print(f"Arma {arma_agregar} añadida.")
                            break
                
                if len(mision.armas) == 7:
                    print("Has alcanzado el máximo número de armas permitidas (7).")

            elif (decision.lower()).strip() == 'eliminar':
                arma_a_eliminar = (input("Ingrese el arma a eliminar: ").lower()).strip()
                arma_eliminada = None

                for arma in mision.armas:
                    if arma_a_eliminar in arma.lower():
                        arma_eliminada = arma
                        mision.armas.remove(arma_eliminada)
                        print(f"Arma {arma_eliminada} eliminada.")
                        break

                if arma_eliminada == None:
                    print("El arma no se encuentra en la lista.")

            else:
                print("Opción no válida.")

        elif opcion == '3':
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

    # Visualizar mision
    def visualizar_mision(self):

        for m in self.misiones_obj:
            print(f'-. {m.nombre}')
        nombre_mision_input = input("Ingrese el nombre de la misión a visualizar: ")

        # Esta iteracion busca si existe alguna mision con el nombre que se acaba de ingresar

        for m in self.misiones_obj:
            if m.nombre == nombre_mision_input:
                mision = m
                break

        if mision:
            mision.mostrar_detalle()
        else:
            print("Misión no encontrada.")

    # Guardar misiones
    def guardar_misiones(self):
        # Se abre el archivo en modo de escritura
        with open('misiones.txt', 'w') as file:
            for mision in self.misiones_obj:
                # Se agrega el separador '|' entre armas para que ',' sea solo para separar atributos principales
                armas = '|'.join(mision.armas)

                # Se agrega el separador ';' entre integrantes para que ',' sea solo para separar atributos principales
                integrantes = ';'.join(mision.integrantes)

                file.write(f"{mision.nombre},{mision.planeta_destino},{mision.nave},{armas},{integrantes}\n")
        print("Misiones guardadas exitosamente.")

    # Requerimiento L: Cargar misiones
    def cargar_misiones(self):
        try:
            # Intentar abrir el archivo en modo de lectura
            with open('misiones.txt', 'r') as file:
                self.misiones_obj = []  # Limpiar la lista actual de misiones para evitar duplicados
                for line in file:
                    nombre, planeta_destino, nave, armas_str, integrantes_str = line.strip().split(',')

                    # El separador '|' entre armas es para que ',' separe los atributos principales de la mision
                    armas = armas_str.split('|')

                    # El separador ';' entre integrantes es para que ',' separe los atributos principales de la mision
                    integrantes = integrantes_str.split(';')
                    mision = Mision(nombre, planeta_destino, nave, armas, integrantes)

                    self.misiones_obj.append(mision)
            print("Misiones cargadas exitosamente.")

        except FileNotFoundError:
            # Si el archivo no existe, se crea un archivo vacío
            open('misiones.txt', 'w').close()
            print("No se encontró el archivo de misiones, se ha creado un archivo nuevo.")

            self.misiones_obj = []  # Asegurarse de que la lista de misiones esté vacía

        except Exception as e:
            print(f"Error al cargar misiones: {str(e)}")
