def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

def buscar(diccionario, nombre_objetivo):
    for datos in diccionario.values():
        if datos["nombre"].lower() == nombre_objetivo.lower():
            return datos
    return None
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
                   codigo = int(input("Ingrese el Codigo del repartidor: "))
                   if codigo in repartidores:
                       print("Este codigo ya existe Ingrese otro")
                   else:
                       break
                repartidores[codigo] = {}
                repartidores[codigo]["nombre"] = input("Ingrese el nombre del repartidor: ")
                repartidores[codigo]["cantidadPaquetes"]=int(input("Ingrese la cantidad de paquetes"))
                repartidores[codigo]["zona"]=input("Ingrese la zona")
        case 2:
            listaOrdenada = [(codigo, datos["nombre"], datos["cantidadPaquetes"], datos["zona"])for codigo, datos in repartidores.items()]
            listaOrdenada = quick_sort(listaOrdenada)
            print("Datos Ordenados")
            for i, (codigo, nombre, paquetes, zona) in enumerate(listaOrdenada, 1):
                print(f"{i}. {nombre} - Paquetes: {paquetes}, Zona: {zona}")
        case 3:
            nombreBbuscar = input("Ingrese el nombre del repartidor: ").strip()
            resultado = buscar(repartidores, nombreBbuscar)
            if resultado:
                print(f"{resultado['nombre']} entregó {resultado['cantidadPaquetes']} paquetes en la zona {resultado['zona']}.")
            else:
                print("no se encontro a nadie.")
        case 4:
            print("Salir")
            break
        case _:
            print("Opcion invalida")