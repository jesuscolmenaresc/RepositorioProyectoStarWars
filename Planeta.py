class Planeta: 
    def __init__(self,name,rotation_period,orbital_period,climate,population,nombre_episodios_aparece,nombre_personajes_planeta):
        self.name = name # Tipo: str
        self.rotation_period = rotation_period # Tipo: str
        self.orbital_period = orbital_period # Tipo: str
        self.climate = climate # Tipo: str
        self.population = population # Tipo: str
        self.nombre_episodios_aparece = nombre_episodios_aparece # Tipo: Lista
        self.nombre_personajes_planeta = nombre_personajes_planeta # Tipo: Lista

    def show(self):
        print(f'''--------------------------------
Nombre: {self.name}
Periodo de rotacion: {self.rotation_period}
Periodo de orbita: {self.orbital_period}
Clima: {self.climate}
Poblacion: {self.population}
Nombre de episodios en donde aparece el planeta:''')

        if self.nombre_episodios_aparece == []:
            print("No se ha encontrado en ningun episodio")
        else:
            for nombre_episodio in self.nombre_episodios_aparece:
                print(f'-. {nombre_episodio}')

        print(f'''Nombre de personajes originarios de este planeta:''')        
        if self.nombre_personajes_planeta == []:
            print("No se han encontrado personajes originarios de este planeta")
        else:
            for nombre_personaje in self.nombre_personajes_planeta:
                print(f'-. {nombre_personaje}')

        print('--------------------------------')