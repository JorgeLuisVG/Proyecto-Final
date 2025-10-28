# clases
class Casa:
    def __init__(self, Numero, Calle, Representante):
        self.Numero = Numero
        self.Calle= Calle
        self.Representante = Representante
        self.Vehiculos = []
    def AñadirVehiculos(self, vehiculo):
        self.Vehiculos.append(vehiculo)
    def ActualizarInformacionRepresentante(self, RepresentanteNuevo):
        self.Representante = RepresentanteNuevo
    def MostrarInformacion(self):
        print(f"{self.Numero} calle: ")
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
            numero = TryCatchInt(None, "Ingrese el numero telefonico")
            if len<(numero) == 8:
                return numero 
            else: print("Ingrese un numero valido")
    Nombre = TryCatchString("Ingrese el nombre del representante", None)
    Telefono = IngresarTelefono()
    return Nombre, Telefono

def OrdenarCasa(House):
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

ListaCalle1 = []
ListaCalle2 = []
ListaCalle3 = []

# Funcionamiento del sistema
while True:
    print("Residenciales Piedra Azul")
    print("1 = Registrar casa")
    print("2 = Registrar casas que ya pagaron su cuota")
    print("3 = Actualizar Informacion de las casas")
    print("10 = salir")
    Opcion = TryCatchInt([1,2,3,10], "Ingrese una opción")

    if Opcion == 1:
        NumCasa = TryCatchString("Ingrese el numero de casa (ej: 1-01)", None)
        CalleCasa = TryCatchInt([1,2,3], "Ingrese el numero de la calle de la casa")
        RepreNombre, RepreNum = IngresarRepresentante()
        NuevoRepre = Representante(RepreNombre, RepreNum)
        NuevaCasa = Casa(NumCasa, CalleCasa, NuevoRepre)
        OrdenarCasa(NuevaCasa)
    elif Opcion == 2:
        print()
    elif Opcion == 3:
        print()
    elif Opcion == 10:
        break
    print()
    
    ListaCalle1 = QuickSort(ListaCalle1)
    ListaCalle2 = QuickSort(ListaCalle2)
    ListaCalle3 = QuickSort(ListaCalle3)