class MateriasAprobadas:
    __dni= str
    __nombre_materia= str
    __fecha= str
    __nota= int
    __aprobacion= str
    
    def __init__(self,dni,nombre,fecha,nota,aprob):
        self.__dni= dni
        self.__nombre_materia= nombre
        self.__fecha= fecha
        self.__nota= nota
        self.__aprobacion= aprob
        
    def __eq__(self,dni):
        return self.__dni == dni
    
    def getDni(self):
        return self.__dni
    
    def getNota(self):
        return self.__nota
    
    def getNombreMateria(self):
        return self.__nombre_materia
    
    def getAprobacion(self):
        return self.__aprobacion
    
    def getFecha(self):
        return self.__fecha
    
    def mostrar(self):
        print(f"dni:{self.__dni},nota:{self.__nota},materia:{self.__nombre_materia},aprobacion:{self.__aprobacion},fecha:{self.__fecha}")
    