# clases
class Casa:
    def __init__(self, Numero, Calle, Representante):
        self.Numero = Numero
        self.Calle= Calle
        self.Representante = Representante
        self.Vehiculos = [] 
        self.PagoMensual = False
    def ActualizarInfo(self):
        while True:
            print("1 = Cambiar representante")
            print("2 = Hacer cammbios en los vehiculos")
            print("3 = salir")
            OP = TryCatchInt([1,2,3], "Ingrese una opcion: ")
            if OP == 1:
                RepreNombre, RepreNum = IngresarRepresentante()
                self.Representante = Representante(RepreNombre, RepreNum)
            elif OP == 2:
                while True:
                    print("1 = Eliminar vehiculo")
                    print("2 = Añadir vehiculo")
                    print("3 = Salir")
                    OP = TryCatchInt([1, 2, 3], "Ingrese una opcion: ")
                    if OP == 1:
                        for i in self.Vehiculos:
                            i.MostrarInformacionVehiculos()
                            print()
                        while True:
                            placa = TryCatchString("Ingrese la placa que desea eliminar: ")
                            Verificada = VerificarPlaca(placa)
                            if Verificada == True:
                                for i in self.Vehiculos:
                                    if placa == i.Placas:
                                        del i
                                        break
                            else: print("Ingrese una placa valida") 
                    elif OP == 2:
                        NuevoVehiculo = CrearVehiculo()
                        self.Vehiculos.append(NuevoVehiculo)
                    elif OP == 3: break
            else: break
    def VerCuota(self, CA):
        Total = CA 
        if len(self.Vehiculos) > 2:
            Total += (len(self.Vehiculos)-2)*10
        else: pass
        return f"El total es: {Total}"
    def ActualizarPago(self):
        self.PagoMensual = True
    def MostrarInformacion(self):
        print(f"{self.Numero} calle: {self.Calle}")
        self.Representante.MostrarInfoRepresentante()
        if self.PagoMensual == False:
            print(f"Cuota mensual {self.VerCuota()} sin pagar")
        else: print(f"Cuota mensual {self.VerCuota()} pagada")
        for vehiculo in self.Vehiculos:
            vehiculo.MostrarInformacionVehiculos()

class Usuario:
    def __init__(self, Nombre, Contraseña):
        self.Nombre = Nombre
        self.Contraseña = Contraseña
    def CambiarContraseña(self, NuevaContraseña):
        self.Contraseña = NuevaContraseña

class Vehiculo:
    def __init__(self, Tipo, Placas, Marca):
        self.Tipo = Tipo
        self.Placas = Placas
        self.Marca = Marca
    def MostrarInformacionVehiculos(self):
        print(f"Tipo de Vehiculo:       {self.Tipo}")
        print(f"Marca:                  {self.Marca}")
        print(f"Placas:                 {self.Placas}")
    def __del__(self):
        print(f"EL vehiculo:")
        self.MostrarInformacionVehiculos()
        print(f"Esta siendo eliminado")

class Representante:
    def __init__(self, Nombre, Telefono):
        self.Nombre = Nombre
        self.Telefono = Telefono
    def MostrarInfoRepresentante(self):
        print(f"Nombre:                 {self.Nombre}")
        print(f"Numero de telefono:     {self.Telefono}")
    def __del__(self):
        print("Se está eliminando al representante")

# Funciones
def TryCatchInt(ListaOpciones, Texto):
    while True:
        while True:
            try:
                Ingresar = int(input(f"{Texto} ").strip())
            except ValueError:
                print("Ingrese un valor valido")
            else: break
        if ListaOpciones:
            if Ingresar in ListaOpciones:
                return Ingresar
            else: print("Intentelo nuevamente")
        elif not ListaOpciones:
            return Ingresar

def TryCatchString(Texto, Lista):
    while True:
        while True:
            Ingresar = input(f"{Texto} ").strip().title()
            if Ingresar == "":
                print("Ingrese un texto valido")
            else: break
        if Lista== None:
            return Ingresar
        elif Lista:
            if Ingresar in Lista:
                return Ingresar
            else:
                print("Ingrese un valor valido")

def VerificarPlaca(Placa):
    ListABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ListNum = [str(n) for n in range(9)]
    if Placa[0] in ListABC and Placa[1] in ListABC and Placa[2] in ListABC and Placa[3] in ListNum and Placa[4] in ListNum and Placa[5] in ListNum:
        return True
    else: return False

def CrearVehiculo():
    while True:
        while True:
            Placa = input("Ingrese la placa del vehiculo: ").upper().strip()
            if VerificarPlaca(Placa) == True:
                break
            else: print("Ingrese una placa valida")
        Tipo = TryCatchString("Ingrese el tipo de vehiculo que es (Carro, Moto, Vehiculo pesado)", ["Carro", "Moto", "Vehiculo pesado"])
        Marca = TryCatchString("Ingrese la marca del vehiculo", None)
        print(f"Se creara el vehiculo tipo {Tipo}: {Marca} con placas: {Placa}")
        Fun = TryCatchInt([1,2], "Es correcto? (1 = si, 2 = no)")
        if Fun == 1: 
            NuevoVehiculo = Vehiculo(Tipo, Placa, Marca)
            return NuevoVehiculo
        else: pass

def IngresarRepresentante():
    def IngresarTelefono():
        while True:
            numero = TryCatchInt(None, "Ingrese el numero telefonico: ")
            if len<(numero) == 8:
                return numero 
            else: print("Ingrese un numero valido")
    Nombre = TryCatchString("Ingrese el nombre del representante: ", None)
    Telefono = IngresarTelefono()
    return Nombre, Telefono

def OrdenarCasas(House):
    if House.Calle == 1:
        ListaCalle1.append(House)
    elif House.Calle == 2:
        ListaCalle2.append(House)
    elif House.Calle == 3:
        ListaCalle3.append(House)

def QuickSort(Lista):
    if len(Lista) <= 1:
        return Lista
    
    pivote = Lista[len(Lista)//2].Numero

    menores = [House for House in Lista if House.Numero < pivote]
    iguales = [House for House in Lista if House.Numero == pivote]
    mayores = [House for House in Lista if House.Numero > pivote]

    return QuickSort(menores) + iguales + QuickSort(mayores)

def ValidarNumeroCasa():
    def ExplorarNumero(NumeroHouse):
        if NumeroHouse[0] in [str(N) for N in range(9)] and NumeroHouse[1] == "-" and NumeroHouse[2] in [str(N) for N in range(9)] and NumeroHouse[3] in [str(N) for N in range(9)]:
            pass
        else: 
            return False
        if NumeroHouse[4]:
            if NumeroHouse[4] in [str(N) for N in range(9)]:
                pass
            else: return False
        else:
            pass
        return True
    
    while True:
        NumeroValid = True
        NumeroCasa = TryCatchString("Ingrese el numero de casa (ej: 1-01)", None)
        if 4 <= len(NumeroCasa) <= 5:
            NumeroValid = ExplorarNumero(NumeroCasa)
            if NumeroValid == True:
                return NumeroCasa
            else:
                print("Ingrese un numero valido")
        elif len(NumeroCasa) != 4:
            print("Ingrese un numero Valido")

def BuscarCasa(Numero, CalleB):
    Encontrado = True
    if CalleB == 1:
        for Casita in ListaCalle1:
            if Casita.Numero == Numero:
                return Casita
            else: Encontrado == False
    elif CalleB == 2:
        for Casita in ListaCalle2:
            if Casita.Numero == Numero:
                return Casita
            else: Encontrado == False
    elif CalleB == 3:
        for Casita in ListaCalle3:
            if Casita.Numero == Numero:
                return Casita
            else: Encontrado == False
    if Encontrado == False:
        print("La casa que busca no existe")
        return None

# Manejo de datos
    # Lista de calles
ListaCalle1 = []
ListaCalle2 = []
ListaCalle3 = []

    # Lista de usuarios
ListaUsuarios = []
    # Cuota actual 
CuotaActual = 0

# Funcionamiento del sistema
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
            MostrarCasas(ListaCalle1)
            print("Caalle 3")
            MostrarCasas(ListaCalle1)        
        elif Opcion == 10:
            break
        print()

        ListaCalle1 = QuickSort(ListaCalle1)
        ListaCalle2 = QuickSort(ListaCalle2)
        ListaCalle3 = QuickSort(ListaCalle3)

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
            i = 0
            Contraseña = TryCatchString("Ingrese su contraseña: ", None)
            if Contraseña == User.Contraseña:
                print("Ingreso valido")
                Menu()
                break
            else:
                print("Contraseña incorrecta intentelo nuevamente")
            if i == 3:
                print("Saliendo")

    elif Opcion == 2:
        Nombre = TryCatchString("Ingrese el nombre del usuario: ", None)
        Contraseña = TryCatchString("Ingrese una nueva contraseña: ", None)

        NuevoUser = Usuario(Nombre, Contraseña)
        ListaUsuarios.append(NuevoUser)

        print("Usuario creado con exito")