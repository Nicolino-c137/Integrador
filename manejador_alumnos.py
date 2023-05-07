import csv
import numpy as np
from clase_alumnos import Alumno

class ManejadorAlumnos:
    __arreglo_alumnos= None
    __dimension= int
    
    def __init__(self,dimension):
        self.__arreglo_alumnos= np.empty(dimension,dtype=Alumno)
        self.__dimension= dimension
        
    def agregarAlumno(self,un_Alumno,i):
        if i < self.__dimension:
            self.__arreglo_alumnos[i]= un_Alumno
    
    def lecturaArchivo(self):
        indice=0
        with open ("alumnos.csv") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader)    #salta la cabezera
            for fila in reader: 
                un_alumno= Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarAlumno(un_alumno,indice)
                indice+= 1
                
    def listarPromocionales(self,materia,manejador_materias):    
        for i in range(manejador_materias.getLen()):
            resultado, dni= manejador_materias.buscarPromocional(materia,i)
            if resultado:
                p= 0
                bandera= False
                while not bandera and p < self.__dimension:
                    p+= 1
                    if dni == self.__arreglo_alumnos[p].getDni():
                        bandera= True
                        fecha= manejador_materias.getFecha(dni) 
                        nota= manejador_materias.getNota(dni)
                        nombre= self.__arreglo_alumnos[p].getNombre()
                        apellido= self.__arreglo_alumnos[p].getApellido()
                        print("""    
DNI\t\tApellido y Nombre\tFecha\t\tNota\tAño que cursa""")
                        print(f"""
{self.__arreglo_alumnos[p].getDni()}\t{apellido}, {nombre}\t{fecha}\t{nota}\t{self.__arreglo_alumnos[p].getAño()}""")
                    p+= 1   
        if not resultado: print("El nombre ingresado de la materia no se encuentra registrado, vuelva a intentarlo")
                
    def ordenar(self):
        cota= self.__dimension
        aux= Alumno(None,None,None,None,None)
        k= 1
        while k != -1:
            k= -1
            for i in range(cota-1):
                if self.__arreglo_alumnos[i] < self.__arreglo_alumnos[i+1]:
                    aux.intercambio(self.__arreglo_alumnos[i])
                    self.__arreglo_alumnos[i].intercambio(self.__arreglo_alumnos[i+1])
                    self.__arreglo_alumnos[i+1].intercambio(aux)
                    k= i
        cota= k
        
    def mostrarLista(self):
        print("DNI      Apellido y Nombre       Carrera        Año que cursa")
        for i in range(self.__dimension):
            print(self.__arreglo_alumnos[i])