def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
repartidores={}
while True:
    print("Menu")
    print("1. Ingresar")
    print("2. Mostar Ordenando")
    print("3. Buscar")
    print("4. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ingreso datos")
            cantidad = int(input("¿Cuántos Repartidores desea ingresar? "))
            for i in range(cantidad):
                print(f"\nRepartidor #{i + 1}")
                while True:
                   codigo = input(int("Ingrese el Codigo del repartidor: "))
                   if codigo in repartidores:
                       print("Este codigo ya existe Ingrese otro")
                   else:
                       break
                repartidores[codigo] = {}
                repartidores[codigo]["nombre"] = input("Ingrese el nombre del repartidor: ")
                repartidores[codigo]["cantidadPaquetes"]=int(input("Ingrese la cantidad de paquetes"))
                repartidores[codigo]["zona"]=input("Ingrese la zona")
        case 2:
            print("Datos Ordenados")
            print("\nLista de repartidores:")
            cantidadPaquetes=list(repartidores.keys())
            ordenarDiccionarios=quick_sort(cantidadPaquetes)
            for cantidadPaquetes in ordenarDiccionarios:
                datos=repartidores[cantidadPaquetes]
                print(f"\nCodigo: {codigo}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Cantidad Paquetes: {datos['cantidadPaquetes']}")
                print(f"Zona: {datos['zona']}")
        case 3:
            print("Buscar")

        case 4:
            print("Salir")
            break
        case _:
            print("Opcion invalida")