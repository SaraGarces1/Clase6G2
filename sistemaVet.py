class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n 


class sistemaV:
    def __init__(self):
        self.__felinos = {}
        self.__caninos = {}
        

    def verificarExiste(self,historia):
        if historia in self.__felinos or self.__caninos:
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroFelinos(self):
        return len(self.__felinos)
        
    
    def verNumeroCaninos(self):
        return len(self.__caninos)

    def ingresarFelino(self,mascota):
        #self.__lista_mascotas.append(mascota) 
        self.__felinos[mascota.verHistoria()]=mascota

    def ingresarCanino(self,mascota):
        #self.__lista_mascotas.append(mascota) 
        self.__caninos[mascota.verHistoria()]=mascota

    def verFechaIngresoFelino(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__felinos:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None
    
    def verFechaIngresoCanino(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__caninos:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamentoFelinos(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__felinos:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None

    def verMedicamentoCaninos(self,historia):
        
        for masc in self.__caninos:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None
        

    def eliminarFelino(self, historia):

        for masc in self.__felinos:
            if historia == masc.verHistoria():
                del self.__felinos[masc]
                #self.__felinos.remove(masc)  #opcion con el pop
                return True  #eliminado con exito

        return False 

    def eliminarCanino(self, historia):

        for masc in self.__caninos:
            if historia == masc.verHistoria():
                del self.__caninos[masc]
                #self.__caninos.remove(masc)  #opcion con el pop
                return True  #eliminado con exito

        return False


class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        