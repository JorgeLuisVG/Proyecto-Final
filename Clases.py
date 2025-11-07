from Funciones import TryCatchInt, TryCatchString, VerificarPlaca, CrearVehiculo, IngresarRepresentante
from Main import *

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
