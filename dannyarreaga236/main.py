#Programa principal
import lemur
import oso
import cebra

cebras = []
osos = []
lemures = []
while True:
    print(f'MENU\n1. Agregar animal\n2. Ver todos los animales del mini-zoo\n3. Salir')
    opc = int(input('Elige una opcion: '))
    match(opc):
        case 1:
            print("\n1. Cebra\n2. Oso\n3. Lemur")
            animal = int(input("\nQue animal agregara? "))
            if animal == 1:
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                sexo = input("Sexo: ")
                peso = input("Peso: ")
                longitud = input("Longitud: ")
                especie = input("Especie: ")
                pareja = input("Pareja: ")
                nuevaCebra = cebra.Cebra(nombre, edad, sexo, peso, longitud, especie, pareja)
                cebras.append(nuevaCebra)
            elif animal == 2:
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                sexo = input("Sexo: ")
                peso = input("Peso: ")
                altura = input("Altura: ")
                pareja = input("Pareja: ")
                nuevoOso = oso.Oso(nombre, edad, sexo, peso, altura, pareja)
                osos.append(nuevoOso)
            elif animal == 3:
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                sexo = input("Sexo: ")
                peso = input("Peso: ")
                largo = input("Largo: ")
                pareja = input("Pareja: ")
                nuevoLemur = lemur.Lemur(nombre, edad, sexo, peso, largo, pareja)
                lemures.append(nuevoLemur)
            else:
                print("Ingrese una opcion valida")
        case 2:
            print("Cebras:\n")
            for i in cebra.Cebra:
                print(cebra.Cebra.nombre[i])
            print("Osos:\n")
            for i in oso.Oso:
                print(oso.Oso.nombre[i])
            print("Lemures:\n")
            for i in lemur.Lemur:
                print(lemur.Lemur.nombre[i])
                
        case 3:
            break
        case _:
            print("ERROR. Ingrese una opcion valida.")