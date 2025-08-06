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
        case 2:
            print("Datos Ordenados")
        case 3:
            print("Buscar")
        case 4:
            print("Salir")
            break
        case _:
            print("Opcion invalida")