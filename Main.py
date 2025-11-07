from Clases import Casa, Usuario, Representante
from Funciones import TryCatchInt, TryCatchString, IngresarRepresentante, OrdenarCasas, QuickSort, ValidarNumeroCasa, BuscarCasa

ListaCalle1, ListaCalle2, ListaCalle3 = [], [], []
ListaUsuarios = []
CuotaActual = 0

def Menu():
    while True:
        print("Residenciales Piedra Azul")
        print("1 = Registrar casa")
        print("2 = Registrar casas que ya pagaron su cuota")
        print("3 = Actualizar Informacion de las casas")
        print("4 = Ver Informacion de las casas")
        print("10 = salir")
        Opcion = TryCatchInt([1,2,3,10], "Ingrese una opción: ")

        if Opcion == 1:
            NumCasa = ValidarNumeroCasa()
            CalleCasa = TryCatchInt([1,2,3], "Ingrese el numero de la calle de la casa: ")
            RepreNombre, RepreNum = IngresarRepresentante()
            NuevoRepre = Representante(RepreNombre, RepreNum)
            NuevaCasa = Casa(NumCasa, CalleCasa, NuevoRepre)
            OrdenarCasas(NuevaCasa)
        elif Opcion == 2:
            while True:
                print("Busque la casa")
                NumBucar = ValidarNumeroCasa()
                calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar: ")
                House = BuscarCasa(NumBucar, calle)
                if House is None:
                    print("No se encontró la casa.")
                    continue
                print(f"Se cancelará la cuota de la casa: {House.Numero} calle: {House.Calle}")
                Pagar = TryCatchInt([1, 2], "Es correcto? (1 = si, 2 = No): ")
                if Pagar == 1: 
                    House.ActualizarPago()
                    break
                else:
                    pass
        elif Opcion == 3:
            while True:
                print("Busque la casa")
                NumBucar = ValidarNumeroCasa()
                calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar: ")
                House = BuscarCasa(NumBucar, calle)
                if House is None:
                    print("No se encontró la casa.")
                    continue
                print()
                House.ActualizarInfo()
        elif Opcion == 4:
            def MostrarCasas(Lista):
                for casa in Lista:
                    casa.MostrarInformacion()
                    print()
                print()
            print("Caalle 1")
            MostrarCasas(ListaCalle1)
            print("Caalle 2")
            MostrarCasas(ListaCalle2)
            print("Caalle 3")
            MostrarCasas(ListaCalle3)        
        elif Opcion == 10:
            break
        print()

        ListaCalle1 = QuickSort(ListaCalle1)
        ListaCalle2 = QuickSort(ListaCalle2)
        ListaCalle3 = QuickSort(ListaCalle3)

def OrdenarUsuarios(Lista):
    if len(Lista) <= 1:
        return Lista
    
    pivote = Lista[len(Lista)//2].Nombre

    menores = [User for User in Lista if User.Nombre < pivote]
    iguales = [User for User in Lista if User.Nombre == pivote]
    mayores = [User for User in Lista if User.ombre > pivote]

    return OrdenarUsuarios(menores) + iguales + OrdenarUsuarios(mayores)

while True:
    print("1 = Iniciar sesion")
    print("2 = Crear Nuevo Usuario")
    Opcion = TryCatchInt([1, 2], "Ingrese una opcion: ")

    if Opcion == 1:
        def busquedaBinaria(Lista, Valor):
            inicio = 0
            fin = len(Lista) -1

            while inicio <= fin:
                medio = (inicio +fin)//2
                if Lista[medio].Nombre == Valor:
                    return medio
                elif Lista[medio].Nombre < Valor:
                    inicio = medio+1
                else:
                    fin = medio -1
            return False
        while True:
            Name = TryCatchString("Ingrese el nombre del usuario: ", None)
            Encontrado = busquedaBinaria(ListaUsuarios, Name)
            if Encontrado != False:
                User = ListaUsuarios[Encontrado]
                break
            else: print("Ingrese un nombre valido")
        while True:
            intentos = 0
            while True:
                Contraseña = TryCatchString("Ingrese su contraseña: ", None)
                if Contraseña == User.Contraseña:
                    print("Ingreso valido")
                    Menu()
                    break
                else:
                    print("Contraseña incorrecta, intentelo nuevamente")
                    intentos += 1
                    if intentos == 3:
                        print("Demasiados intentos fallidos. Saliendo...")
                        break

    elif Opcion == 2:
        Nombre = TryCatchString("Ingrese el nombre del usuario: ", None)
        Contraseña = TryCatchString("Ingrese una nueva contraseña: ", None)

        NuevoUser = Usuario(Nombre, Contraseña)
        ListaUsuarios.append(NuevoUser)

        print("Usuario creado con exito")

    ListaUsuarios = OrdenarUsuarios(ListaUsuarios)