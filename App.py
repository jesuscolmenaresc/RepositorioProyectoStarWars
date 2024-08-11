import requests as rq
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Personaje import Personaje
from Mision import Mision

class App:
    peliculas_obj = []
    especies_obj = []
    planetas_obj  = []
    personajes_obj = []

    def start(self):
        print('''BIENVENIDO
Iniciando carga de datos, por favor espere...''')
        # Carga de datos
        #self.cargar_datos_peliculas()
        print('Peliculas ha sido cargado exitosamente...')
        #self.cargar_datos_especies()
        print('Especies ha sido cargado exitosamente...')
        #self.cargar_datos_planetas()
        print('Planetas ha sido cargado exitosamente...')
        #self.cargar_datos_personajes()
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
8. Salir
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
                while True:
                    opcion_0 = (input('Escriba \'0\' para volver al menu anterior: ')).strip()
                    if opcion_0 == '0':
                        print('Regresando...')
                        break
                    else:
                        print('Opcion invalida')
                        continue

            elif opcion_menu == '8':
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

    def __init__(self):
        self.misiones = []

    # Requerimiento H: Construir mision
    def agregar_mision(self):
        if len(self.misiones) >= 5:
            print("No puedes definir más de 5 misiones.")
            return

        nombre = input("Ingrese el nombre de la misión: ")
        planeta_destino = input("Ingrese el planeta destino: ")
        nave = input("Ingrese la nave a utilizar: ")

        armas = [input("Ingrese arma (o presione Enter para omitir): ") for _ in range(7)]

        integrantes = [input("Ingrese integrante (o presione Enter para omitir): ") for _ in range(7)]

        mision = Mision(nombre, planeta_destino, nave, armas, integrantes)

        self.misiones.append(mision)
        print("Misión agregada exitosamente.")

    # Requerimiento I: Modificar Mision
    def modificar_mision(self):
        nombre_mision = input("Ingrese el nombre de la misión a modificar: ")

        # Esta iteracion busca si existe alguna mision con el nombre que se acaba de ingresar
        mision = next((m for m in self.misiones if m.nombre == nombre_mision), None)

        if not mision:
            print("Misión no encontrada.")
            return

        print("Selecciona el atributo de la misión que deseas modificar:")
        print("1. Nave")
        print("2. Armas")
        print("3. Integrantes")
        opcion = input("Escribe el número de la opción que deseas modificar: ")

        if opcion == '1':
            nueva_nave = input("Ingrese la nueva nave a utilizar: ")
            mision.nave = nueva_nave
            print("Nave actualizada exitosamente.")

        elif opcion == '2':
            print("Actualmente las armas de la misión son: ", mision.armas)
            decision = input("¿Deseas agregar o eliminar armas? (agregar/eliminar): ")

            if decision.lower() == 'agregar':
                while len(mision.armas) < 7:
                    nueva_arma = input("Ingrese la nueva arma a añadir o escriba 'salir' para terminar: ")
                    if nueva_arma.lower() == 'salir':
                        break

                    if nueva_arma not in mision.armas:
                        mision.armas.append(nueva_arma)
                        print("Arma añadida.")

                    else:
                        print("Esta arma ya está en la lista.")

                if len(mision.armas) == 7:
                    print("Has alcanzado el máximo número de armas permitidas (7).")

            elif decision.lower() == 'eliminar':
                arma_a_eliminar = input("Ingrese el arma a eliminar: ")
                if arma_a_eliminar in mision.armas:
                    mision.armas.remove(arma_a_eliminar)
                    print("Arma eliminada.")

                else:
                    print("El arma no se encuentra en la lista.")

            else:
                print("Opción no válida.")

        elif opcion == '3':
            print("Actualmente los integrantes de la misión son: ", mision.integrantes)
            decision = input("¿Deseas agregar o eliminar integrantes? (agregar/eliminar): ")
            if decision.lower() == 'agregar':
                while len(mision.integrantes) < 7:
                    nuevo_integrante = input("Ingrese el nuevo integrante a añadir o escriba 'salir' para terminar: ")
                    if nuevo_integrante.lower() == 'salir':
                        break
                    if nuevo_integrante not in mision.integrantes:
                        mision.integrantes.append(nuevo_integrante)
                        print("Integrante añadido.")

                    else:
                        print("Este integrante ya está en la lista.")

                if len(mision.integrantes) == 7:
                    print("Has alcanzado el máximo número de integrantes permitidos (7).")

            elif decision.lower() == 'eliminar':
                integrante_a_eliminar = input("Ingrese el integrante a eliminar: ")

                if integrante_a_eliminar in mision.integrantes:
                    mision.integrantes.remove(integrante_a_eliminar)
                    print("Integrante eliminado.")

                else:
                    print("El integrante no se encuentra en la lista.")

            else:
                print("Opción no válida.")

        else:
            print("Opción no válida.")

    # Requerimiento J: Visualizar mision
    def visualizar_mision(self):
        nombre_mision = input("Ingrese el nombre de la misión a visualizar: ")

        # Esta iteracion busca si existe alguna mision con el nombre que se acaba de ingresar
        mision = next((m for m in self.misiones if m.nombre == nombre_mision), None)

        if mision:
            mision.mostrar_detalle()
        else:
            print("Misión no encontrada.")

    # Requerimiento K: Guardar misiones
    def guardar_misiones(self):
        # Se abre el archivo en modo de escritura
        with open('misiones.txt', 'w') as file:
            for mision in self.misiones:
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
                self.misiones = []  # Limpiar la lista actual de misiones para evitar duplicados
                for line in file:
                    nombre, planeta_destino, nave, armas_str, integrantes_str = line.strip().split(',')

                    # El separador '|' entre armas es para que ',' separe los atributos principales de la mision
                    armas = armas_str.split('|')

                    # El separador ';' entre integrantes es para que ',' separe los atributos principales de la mision
                    integrantes = integrantes_str.split(';')
                    mision = Mision(nombre, planeta_destino, nave, armas, integrantes)

                    self.misiones.append(mision)
            print("Misiones cargadas exitosamente.")

        except FileNotFoundError:
            # Si el archivo no existe, se crea un archivo vacío
            open('misiones.txt', 'w').close()
            print("No se encontró el archivo de misiones, se ha creado un archivo nuevo.")

            self.misiones = []  # Asegurarse de que la lista de misiones esté vacía

        except Exception as e:
            print(f"Error al cargar misiones: {str(e)}")
