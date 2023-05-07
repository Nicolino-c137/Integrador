import sys, os

class Menu:
    __elecciones= {}
    __materias= None
    __alumnos= None
    
    def __init__(self,lista,arreglo):
        self.__manejador_materias= lista
        self.__manejador_alumnos= arreglo
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Mostrar promedio de un alumno
2. Mostrar estudiantes promocionales que aprobaron 
3. Listar alumnos ordenados
0. Salir
""")
        
    def generarMenu(self):
        while True:
            self.mostrarMenu()
            op= input("Seleccion alguna opción: ")
            os.system("cls")
            ejecutar= self.__elecciones.get(op)
            if ejecutar:
                ejecutar()
            else: 
                print("Opcion no valida, vuelva a intentarlo")
                os.system("pause")
            
            
    def opcion1(self):
        print("1. Mostrar promedio de un alumno")
        print()
        dni= input("Ingrese el dni de un alumno para ver su promedio con aplazos y sin aplazos: ")
        self.__manejador_materias.calcularProm(dni)
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar estudiantes promocionales que aprobaron")
        print()
        materia= input("Ingrese el nombre de una materia para ver los estudiantes que la aprobaron de forma promocional: ")
        self.__manejador_alumnos.listarPromocionales(materia,self.__manejador_materias)
        os.system("pause")
    
    def opcion3(self):
        print("3. Listar alumnos ordenados")
        print()
        self.__manejador_alumnos.ordenar()
        print("Lista ordenada exitosamente")
        self.__manejador_alumnos.mostrarLista()
        os.system("pause")
    
    def salir(self):
        sys.exit(0)