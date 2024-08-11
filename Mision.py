class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def mostrar_detalle(self):
        print(f"Nombre de la misión: {self.nombre}")
        print(f"Planeta destino: {self.planeta_destino}")
        print(f"Nave: {self.nave}")
        print("Armas:")
        for arma in self.armas:
            print(f" - {arma}")
        print("Integrantes:")
        for integrante in self.integrantes:
            print(f" - {integrante}")

    def editar_mision(self, nueva_nave=None, nuevas_armas=None, nuevos_integrantes=None):
        if nueva_nave:
            self.nave = nueva_nave
        if nuevas_armas:
            self.armas = nuevas_armas
        if nuevos_integrantes:
            self.integrantes = nuevos_integrantes