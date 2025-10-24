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

class Representante:
    def __init__(self, Nombre, Telefono):
        self.Nombre = Nombre
        self.Telefono = Telefono
    def MostrarInfoRepresentante(self):
        print(f"Nombre:                 {self.Nombre}")
        print(f"Numero de telefono:     {self.Telefono}")

class Usuario:
    def __init__(self, Nombre, Contraseña):
        self.Nombre = Nombre
        self.Contraseña = Contraseña
    def CambiarContraseña(self, NuevaContraseña):
        self.Contraseña = NuevaContraseña

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

def TryCatchString(Texto):
    while True:
        Ingresar = input(f"{Texto} ").strip().title()
        if Ingresar == "":
            print("Ingrese un texto valido")

# Funcionamiento del sistema

def ValidarNumeroCasa():
    NumeroCasa = TryCatchString("Ingrese el numero de la casa")
    

while True:
    print("Residenciales Piedra Azul")
    print("1 = Registrar casa")
    print("2 = Registrar casas que ya pagaron su cuota")
    print("3 = Actualizar Informacion de las casas")
    print("10 = salir")
    Opcion = TryCatchInt([1,2,3,10], "Ingrese una opción")

    if Opcion == 1:
        NumCasa = 0
    elif Opcion == 2:
        print()
    elif Opcion == 3:
        print()
    elif Opcion == 10:
        break
    print()
