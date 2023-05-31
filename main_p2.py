#parte 2 

from clases_vehi import Vehiculo, Automovil, Particular,Carga, Bicicleta, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
print(particular)

carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
print(carga)

bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera" )
print(bicicleta)

motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva",21,"DobleViga", "2T")
print(motocicleta)

print("")

#Llamando instancias

print("Motocicleta es instancia con relación a Vehículo: ", isinstance(motocicleta,Vehiculo))
print("Motocicleta es instancia con relación a Automovil: ", isinstance(motocicleta,Automovil))
print("Motocicleta es instancia con relación a Vehículo particular: ", isinstance(motocicleta,Particular))
print("Motocicleta es instancia con relación a Vehículo de carga: ", isinstance(motocicleta,Carga))
print("Motocicleta es instancia con relación a Bicicleta: ", isinstance(motocicleta,Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta: ", isinstance(motocicleta,Motocicleta))

