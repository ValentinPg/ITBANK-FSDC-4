class Direccion():
    def __init__(self, calle: str, numero: str, ciudad: str, estado: str, cp: str) -> None:
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp

    def __str__(self):
        return f'(calle:{self.calle}\n numero:{self.numero}\n ciudad:{self.ciudad}\n prvincia:{self.estado}\n pais:{self.cp})'
    

# d = Direccion()
# d.calle = artigas
# d.numero = 10
# d.ciudad = caracas
# d.estado = america
# d.cp= 4400

# print(d)
