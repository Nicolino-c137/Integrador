import csv
from clase_materiasAprobadas import MateriasAprobadas 

class ManejadorMaterias:
    __lista_materias= None
    
    def __init__(self):
        self.__lista_materias= []
        
    def agregarMateria(self,una_materia):
        self.__lista_materias.append(una_materia)
        
    def getLen(self):
        return len(self.__lista_materias)
        
    def lecturaArchivo(self):
        with open ("materiasAprobadas.csv") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader)    #salta la cabecera
            for fila in reader:
                nota= int(fila[3])
                una_materia= MateriasAprobadas(fila[0],fila[1],fila[2],nota,fila[4])
                self.agregarMateria(una_materia)
                    
    def calcularProm(self,dni):
        sum= 0
        sum_sin_aplazos= 0
        cont1= cont2= 0
        bandera= False
        for i in range(len(self.__lista_materias)):
            if self.__lista_materias[i] == dni:
                bandera= True
                sum+= int(self.__lista_materias[i].getNota())
                cont1+= 1
                if self.__lista_materias[i].getNota() >= 4:
                    sum_sin_aplazos+= int(self.__lista_materias[i].getNota())
                    cont2+= 1
        if bandera:
            print(f"El promedio del alumno con aplazos es de {sum/cont1}") 
            print(f"El promedio del alumno sin aplazos es de {sum_sin_aplazos/cont2}")
        else: print("No se encontro el dni ingresado")
        
    def buscarPromocional(self,materia,i):
        bandera= False
        #for i in range(len(self.__lista_materias)):
        if self.__lista_materias[i].getNombreMateria() == materia:
                bandera= True
                if self.__lista_materias[i].getAprobacion() == 'P':
                    dni= self.__lista_materias[i].getDni()
                else:
                    print("Ningún alumno promociono la materia")
        else: dni=None  
        return bandera, dni
        
    def getFecha(self,dni):
        for i in range(len(self.__lista_materias)):
            if self.__lista_materias[i].getDni() == dni:
                fecha= self.__lista_materias[i].getFecha()
        return fecha
    
    def getNota(self,dni):
        for i in range(len(self.__lista_materias)):
            if self.__lista_materias[i].getDni() == dni:
                nota= self.__lista_materias[i].getNota()
        return nota

        