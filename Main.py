from Clases import Casa, Usuario, Representante
from Funciones import (TryCatchInt, TryCatchString, IngresarRepresentante, OrdenarCasas,
QuickSort, ValidarNumeroCasa, BuscarCasa, OrdenarUsuarios, ValidarExistencia, busquedaBinaria)

ListaCalle1, ListaCalle2, ListaCalle3 = [], [], []
ListaUsuarios = []

CuotaActual = -1

# Funcionamiento del sistema
def Menu():
    global ListaCalle1, ListaCalle2, ListaCalle3, CuotaActual
    while True:
        print("Residenciales Piedra Azul")
        print("1 = Registrar casa")
        print("2 = Registrar casas que ya pagaron su cuota")
        print("3 = Actualizar Informacion de las casas")
        print("4 = Ver Informacion de las casas")
        print("5 = Actualizar precio de la cuota mensual")
        print("10 = salir")
        Opcion = TryCatchInt([1, 2, 3, 4, 5, 10], "Ingrese una opción: ")

        if Opcion == 1:
            NumCasa = ValidarNumeroCasa()
            CalleCasa = TryCatchInt([1,2,3], "Ingrese el numero de la calle de la casa: ")
            RepreNombre, RepreNum = IngresarRepresentante()
            NuevoRepre = Representante(RepreNombre, RepreNum)
            NuevaCasa = Casa(NumCasa, CalleCasa, NuevoRepre)
            OrdenarCasas(NuevaCasa)
        elif Opcion == 2:
            while True:
                if CuotaActual == -1:
                    print("Defina Primero un precio a la cuota mensual")
                    break
                else: pass
                if ValidarExistencia(ListaCalle1) == False and ValidarExistencia(ListaCalle2) == False and ValidarExistencia(ListaCalle2) == False:
                    break
                else: pass

                print("Busque la casa")
                calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar: ")
                if calle == 1 and len(ListaCalle1) == 0: break
                if calle == 2 and len(ListaCalle2) == 0: break
                if calle == 3 and len(ListaCalle3) == 0: break
                else: 
                    print("Continue")


                NumBucar = ValidarNumeroCasa()

                House = BuscarCasa(NumBucar, calle)
                if House is None:
                    print("No se encontró la casa.")
                    continue
                print(f"Se cancelará la cuota de la casa: {House.Numero} calle: {House.Calle}")
                Pagar = TryCatchInt([1, 2], "Es correcto? (1 = si, 2 = No): ")
                if Pagar == 1: 
                    House.ActualizarPago()
                    break
                else: pass
        elif Opcion == 3:
            while True:
                if ValidarExistencia(ListaCalle1) == False and ValidarExistencia(ListaCalle2) == False and ValidarExistencia(ListaCalle2) == False:
                    break
                else: pass

                print("Busque la casa")
                calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar: ")
                if calle == 1 and len(ListaCalle1) == 0: break
                if calle == 2 and len(ListaCalle2) == 0: break
                if calle == 3 and len(ListaCalle3) == 0: break
                else: 
                    print("Continue")

                NumBucar = ValidarNumeroCasa()

                House = BuscarCasa(NumBucar, calle)
                if House is None:
                    print("No se encontró la casa.")
                    continue
                print()
                House.ActualizarInfo()
                break
        elif Opcion == 4:
            def MostrarCasas(Lista):
                for casa in Lista:
                    casa.MostrarInformacion()
                    print()
                print()
            if ValidarExistencia(ListaCalle1) == True:
                print("Caalle 1")
                MostrarCasas(ListaCalle1)
            if ValidarExistencia(ListaCalle2) == True:
                print("Caalle 2")
                MostrarCasas(ListaCalle2)
            if ValidarExistencia(ListaCalle3) == True:
                print("Caalle 3")
                MostrarCasas(ListaCalle3)
        elif Opcion == 5:
            while True:
                try:
                    NCP = float(input("Ingrese el nuevo precio de la cuota mensual: ").strip())
                except ValueError:
                    print("Ingrese un precio valido")
                else: break
            CuotaActual = NCP
        elif Opcion == 10: break
        print()
        if ListaCalle1: ListaCalle1 = QuickSort(ListaCalle1)
        if ListaCalle2: ListaCalle2 = QuickSort(ListaCalle2)
        if ListaCalle3: ListaCalle3 = QuickSort(ListaCalle3)

while True:
    print("1 = Iniciar sesion")
    print("2 = Crear Nuevo Usuario")
    Opcion = TryCatchInt([1, 2], "Ingrese una opcion: ")

    if Opcion == 1:
        if ValidarExistencia(ListaUsuarios) == True: pass
        else: 
            print("No existen usuarios")
            continue
        while True:
            Name = TryCatchString("Ingrese el nombre del usuario: ", None)
            UsuarioEncontrado = busquedaBinaria(ListaUsuarios, Name)
            if UsuarioEncontrado == -1:
                print("Ingrese un nombre valido")
            else: 
                User = ListaUsuarios[UsuarioEncontrado]
                break
        while True:
            intentos = 0
            Contraseña = TryCatchString("Ingrese su contraseña: ", None)
            if Contraseña == User.Contraseña:
                print("Ingreso valido")
                Menu()
            else:
                print("Contraseña incorrecta, intentelo nuevamente")
                intentos += 1
                if intentos == 3:
                    print("Demasiados intentos fallidos. Saliendo...")
                    break
            break

    elif Opcion == 2:
        Nombre = TryCatchString("Ingrese el nombre del usuario: ", None)
        Contraseña = TryCatchString("Ingrese una nueva contraseña: ", None)

        NuevoUser = Usuario(Nombre, Contraseña)
        ListaUsuarios.append(NuevoUser)

        print("Usuario creado con exito")

    ListaUsuarios = OrdenarUsuarios(ListaUsuarios)