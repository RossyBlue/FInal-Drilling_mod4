#Extraer los datos desde las clases

from clases_vehi import Vehiculo, Automovil

instancias = []

n= int(input("Inserte los vehiculos que desea informar: "))

for i in range(n):
    print(f"Datos del automovil {i+1}")
    marca = input("Inserte la marca del automovil: ")
    modelo = input("Inserte el modelo: ")
    nruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad: "))
    cilindrada = int(input("Inserte el cilindraje: "))
    print("")
    auto = Automovil (marca,modelo,nruedas,velocidad,cilindrada)
    instancias.append(auto)


print("-------------------------------")

print("Imprimiendo por pantalla los Vehículos:")

for index,item in enumerate(instancias):
    print(f"Datos del automóvil {index +1} : Marca {item.marca}, Modelo {item.modelo}, Ruedas {item.nruedas}, Velocidad {item.velocidad}, Cilindrada {item.cilindrada} cc")



