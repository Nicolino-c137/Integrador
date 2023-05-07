from clase_menu import Menu
from manejador_materias import ManejadorMaterias
from manejador_alumnos import ManejadorAlumnos

def contarFilasArchi():
    archivo= open("alumnos.csv")
    lineas= archivo.readlines()
    cant= len(lineas)
    archivo.close()
    return cant-1
            
if __name__ == '__main__':
    lista_materias= ManejadorMaterias()
    lista_materias.lecturaArchivo()
    dimension= contarFilasArchi()
    arreglo_alumnos= ManejadorAlumnos(dimension)
    arreglo_alumnos.lecturaArchivo()
    menu= Menu(lista_materias,arreglo_alumnos)
    menu.generarMenu()