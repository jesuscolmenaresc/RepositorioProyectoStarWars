class Especie(): 
    def __init__(self,name,height,origin_planet,language,classification,nombre_personajes_especie,nombre_episodios_aparece): 
        self.name = name # Tipo: str
        self.height = height # Tipo: int
        self.origin_planet = origin_planet # Tipo: str
        self.language = language # Tipo: str
        self.classification = classification # Tipo: str
        self.nombre_personajes_especie = nombre_personajes_especie # Tipo: list
        self.nombre_episodios_aparece = nombre_episodios_aparece # Tipo: list

    def show(self):
        print(f'''--------------------------------
Nombre: {self.name}
Altura promedio: {self.height}
Planeta de origen: {self.origin_planet}
Lengua materna: {self.language}
Clasificación: {self.classification}
Nombre de personajes que pertenecen a la especie:''')

        for nombre_personaje in self.nombre_personajes_especie:
            print(f'-. {nombre_personaje}')

        print(f'''Nombre de episodios donde aparece la especie:''')        
        for nombre_episodio in self.nombre_episodios_aparece:
            print(f'-. {nombre_episodio}')

        print('--------------------------------')