class Direccion():
    def __init__(self, calle: str, numero: int, ciudad: str, estado: str, cp: int) -> None:
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp

    def __str__(self):
        return f'({self.calle} {self.numero} {self.ciudad} {self.estado} {self.cp})'
    

# d = Direccion()
# d.calle = artigas
# d.numero = 10
# d.ciudad = caracas
# d.estado = america
# d.cp= 4400

# print(d)
