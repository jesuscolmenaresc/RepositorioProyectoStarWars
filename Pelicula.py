class Pelicula:
    def __init__(self, title, id, release_date, opening_crawl, director, nombres_especies, nombres_planetas, nombres_personajes):
        self.title = title # Tipo: string
        self.id = id # Tipo: int
        self.release_date = release_date # Tipo: str
        self.opening_crawl = opening_crawl # Tipo: str
        self.director = director # Tipo: str
        self.nombres_especies = nombres_especies # Tipo: list
        self.nombres_planetas = nombres_planetas # Tipo: list
        self.nombres_personajes = nombres_personajes # Tipo: list

    def show(self):
        print(f'''--------------------------------
Title: {self.title}
Episode: {self.id}
Release Date: {self.release_date}
"Director: {self.director}

Opening Crawl: {self.opening_crawl}
--------------------------------''')