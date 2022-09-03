from JSONprueba import iniciarPrograma
from print_HTML import plantillaHTML




#-------------------------Ingrese el archivo que se desea escanear (classic,gold,black)---------------------------------------------------------#
archivo = input("Ingrese el archivo que desea leer (black,classic o gold): ")

x,y = iniciarPrograma(archivo)
plantillaHTML(x,y)
#--------------------------El archivo HTML se llama: indexpy.html (Carpeta "SEGMENTACION CLIENTES")-------------------------------------------------------------------------------------------------------#