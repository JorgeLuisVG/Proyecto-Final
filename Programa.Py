# clases
class Casa:
    def __init__(self, Numero, Calle, Representante):
        self.Numero = Numero
        self.Calle= Calle
        self.Representante = Representante
        self.Vehiculos = [] 
        self.PagoMensual = False
    def AñadirVehiculos(self, vehiculo):
        self.Vehiculos.append(vehiculo)
    def ActualizarInfo(self):
        def BorrarVehiculo(Vh):
            del Vh
        print("Para cada opcion seleccione (1 = si, 2 = no)")
        OP = TryCatchInt([1,2], "Desea Cambiar al representante?")
        if OP == 1:
            RepreNombre, RepreNum = IngresarRepresentante()
            self.Representante = Representante(RepreNombre, RepreNum)
        else: pass
        OP = TryCatchInt([1,2], "Desea hacer cambios en los vehiculos?")
        if OP == 1:
            OP = TryCatchInt([1,2], "Desea eliminar un vehiculo?")
            if OP == 1:
                if len(self.Vehiculos) == 1:
                    OP = TryCatchInt([1,2], f"Desea eliminar el vehiculo: {self.Vehiculos}?")

                for i in self.Vehiculos:
                    i.MosrtrarInformacionVehiculos()
                    print()
                
                
        else: pass

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
        self.Representante.MostrarInformacionRepresentante()
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
    def MosrtrarInformacionVehiculos(self):
        print(f"Tipo de Vehiculo:       {self.Tipo}")
        print(f"Marca:                  {self.Marca}")
        print(f"Placas:                 {self.Placas}")
    def __del__(self):
        print(f"EL vehiculo:")
        self.MosrtrarInformacionVehiculos()
        print(f"Esta siendo eliminado")

class Representante:
    def __init__(self, Nombre, Telefono):
        self.Nombre = Nombre
        self.Telefono = Telefono
    def MostrarInfoRepresentante(self):
        print(f"Nombre:                 {self.Nombre}")
        print(f"Numero de telefono:     {self.Telefono}")

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

while True:
    print("Residenciales Piedra Azul")
    print("1 = Registrar casa")
    print("2 = Registrar casas que ya pagaron su cuota")
    print("3 = Actualizar Informacion de las casas")
    print("10 = salir")
    Opcion = TryCatchInt([1,2,3,10], "Ingrese una opción")

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
            calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar")
            House = BuscarCasa(NumBucar, calle)
            print(f"Se cancelará la cuota de la casa: {House.Numero} calle: {House.Calle}")
            Pagar = TryCatchInt([1, 2], "Es correcto? (1 = si, 2 = No)")
            if Pagar == 1: 
                House.ActualizarPago()
                break
            else:
                pass
    elif Opcion == 3:
        while True:
            print("Busque la casa")
            NumBucar = ValidarNumeroCasa()
            calle = TryCatchInt([1,2,3], "Ingrese la calle donde desea buscar")
            House = BuscarCasa(NumBucar, calle)
            print()



    elif Opcion == 10:
        break
    print()

    ListaCalle1 = QuickSort(ListaCalle1)
    ListaCalle2 = QuickSort(ListaCalle2)
    ListaCalle3 = QuickSort(ListaCalle3)