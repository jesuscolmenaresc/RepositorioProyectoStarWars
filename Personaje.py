class Personaje:
    def __init__(self, name, homeworld_name, nombre_episodios_aparece,gender,specie,nombre_naves_utiliza,nombre_vehiculos_utiliza):
        self.name = name # Tipo = str
        self.homeworld_name = homeworld_name # Tipo = str
        self.nombre_episodios_aparece = nombre_episodios_aparece # Tipo = list
        self.gender = gender # Tipo = str
        self.specie = specie # Tipo = str
        self.nombre_naves_utiliza = nombre_naves_utiliza # Tipo = list
        self.nombre_vehiculos_utiliza = nombre_vehiculos_utiliza # Tipo = list

    def show(self):
        print(f'''--------------------------------
Nombre: {self.name}
Nombre del Planeta de origen: {self.homeworld_name}
Genero: {self.gender}
Especie: {self.specie}
Titulos de los episodios en los que interviene:''')
        for episodio_aparece in self.nombre_episodios_aparece:
             print(f'-. {episodio_aparece}')
        print('Nombre de las naves que utiliza:')
        for nombre_nave in self.nombre_naves_utiliza:
            print(f'-. {nombre_nave}')

        print(f'''Nombre de los vehiculos que utiliza:''')        
        for nombre_vehiculo in self.nombre_vehiculos_utiliza:
            print(f'-. {nombre_vehiculo}')
        print('--------------------------------')