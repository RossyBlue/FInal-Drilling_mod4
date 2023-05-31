import csv

class Vehiculo:
    def __init__(self,marca,modelo,nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a") as archivo:
                datos = [(self.__class__, self.__dict__)]  # con self se puede invocar cualquier vehiculo 
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe el archivovehiculo.csv")     
        except Exception as e:
            print("Error reportado: ", e)       

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                #datos = [(self.__class__, self.__dict__)]  # con self se puede invocar cualquier vehiculo 
                vehiculos =csv.reader(archivo)
                print(f"Lista de Vehículos {type(self).__name__}")
                #print(self.__class__)
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                     print(item[1])    
                     print("")

        except FileNotFoundError:
            print("No existe el archivovehiculo.csv")     
        except Exception as e:
            print("Error reportado: ", e)  








    
    def __str__(self):
       return f"Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.nruedas} "

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nruedas,velocidad, cilindrada):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad        
        self.cilindrada = cilindrada

    def __str__(self):   
        return Vehiculo.__str__(self) + f"Velocidad:  {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc, "

    
class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas,velocidad, cilindrada, numpuestos):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.numpuestos = numpuestos       
        
    def get_numpuesto(self):
        return self.numpuestos

    def set_numpuestos(self,numpuesto_new):
        self.numpuesto = numpuesto_new
    
    def __str__(self):
        return Automovil.__str__(self) + f"Puestos: {self.numpuestos}"

    
class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas,velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.carga = carga       
        

    def __str__(self):   
        return Automovil.__str__(self) + f"Carga:  {self.carga}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo  

    def __str__(self):   
        return Vehiculo.__str__(self) + f"Tipo: {self.tipo}, "
    

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipo, numradios, cuadro, motor):
        super().__init__(marca, modelo, nruedas, tipo)
        self.numradios = numradios 
        self.cuadro = cuadro
        self.motor = motor
        
    def __str__(self):   
        return Bicicleta.__str__(self) + f"Motor :  {self.motor}, Cuadro :  {self.cuadro}, Radios:  {self.numradios}"
    





