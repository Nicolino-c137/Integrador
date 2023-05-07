class Alumno: 
    __dni= str
    __apellido= str
    __nombre= str
    __carrera= str
    __año_queCursa= int
    
    def __init__(self,dni,apellido,nombre,carrera,año):
        self.__dni= dni
        self.__apellido= apellido
        self.__nombre= nombre
        self.__carrera= carrera
        self.__año_queCursa= año
        
    def __str__(self):
        return f"{self.__dni}   {self.__apellido}, {self.__nombre}        {self.__carrera}           {self.__año_queCursa}"
        
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getAño(self):
        return self.__año_queCursa
    
    def __lt__(self,otro):
        resultado= False
        if self.__año_queCursa < otro.__año_queCursa:
            resultado= True
        elif self.__año_queCursa == otro.__año_queCursa:
            if self.__apellido < otro.__apellido:
                resultado= True
        return resultado
    
    def intercambio(self, otro):
        self.__apellido = otro.__apellido
        self.__año_queCursa = otro.__año_queCursa
        self.__carrera = otro.__carrera 
        self.__dni = otro.__dni
        self.__nombre = otro.__nombre
    
    
            
        
    