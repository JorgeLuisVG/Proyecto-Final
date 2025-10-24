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
    def __init__(self, Numero, Representante):
        self.Numero = Numero
        self.Representante = Representante
        self.Vehiculos = []
    def AñadirVehiculos(self, vehiculo):
        self.Vehiculos.append(vehiculo)
    def ActualizarInformacionRepresentante(self, RepresentanteNuevo):
        self.Representante = RepresentanteNuevo
    def MostrarInformacion(self):
        print(f"{self.Numero}")
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

def TryCatchInt(ListaOpciones, Texto):
    while True:
        while True:
            try:
                Ingresar = int(input(Texto).strip())
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
        Ingresar = input(Texto).strip().title()
        if Ingresar == "":
            print("Ingrese un texto valido")


