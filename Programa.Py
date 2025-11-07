import os
import time
from datetime import datetime, timedelta

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
                        if len(self.Vehiculos) == 0: break
                        else: pass
                        for i in self.Vehiculos:
                            i.MostrarInformacionVehiculos()
                            print()
                        while True:
                            placa = input("Ingrese la placa que desea eliminar: ").upper().strip()
                            Verificada = VerificarPlaca(placa)
                            if Verificada == True:
                                for i in self.Vehiculos:
                                    if placa == i.Placas:
                                        print("Eliminando")
                                        del i
                            else: print("Ingrese una placa valida") 
                            break
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

    def VerMarbetes(self):
        Marbetes = []
        for v in self.Vehiculos:
            Marbetes.append({"Tipo": v.Tipo, "Placas": v.Placas})

        print(f"Esta casa necsita: {len(Marbetes)} marbete(s)")
        for m in Marbetes:
            print(m)
    def MostrarInformacion(self):
        print(f"{self.Numero} calle: {self.Calle}")
        self.Representante.MostrarInfoRepresentante()
        if self.PagoMensual == False:
            print(f"Cuota mensual {self.VerCuota(CuotaActual)} sin pagar")
        else: print(f"Cuota mensual {self.VerCuota(CuotaActual)} pagada")
        print("Vehiculos: ")
        for vehiculo in self.Vehiculos:
            vehiculo.MostrarInformacionVehiculos()
        self.VerMarbetes()

class Usuario:
    def __init__(self, Nombre, Contraseña):
        self.Nombre = Nombre
        self.Contraseña = Contraseña

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

def TryCatchString(Texto, Lista=None):
    while True:
        Ingresar = input(f"{Texto} ").strip().title()
        if Ingresar == "":
            print("Ingrese un texto valido")
            continue
        if Lista is None or Ingresar in Lista:
            return Ingresar
        print("Ingrese un valor valido")

def VerificarPlaca(Placa):
    ListABC = [chr(n) for n in range(65, 91)]
    ListNum = [str(n) for n in range(10)]
    return (
        len(Placa) == 6 and
        all([Placa[0] in ListNum, Placa[1] in ListNum, Placa[2] in ListNum,
             Placa[3] in ListABC, Placa[4] in ListABC, Placa[5] in ListABC])
    )

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
            if len(str(numero)) == 8:
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
        if len(NumeroHouse) == 5:
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
            if NumeroValid == True: return NumeroCasa
            else: print("Ingrese un numero valido")
        elif len(NumeroCasa) != 4: print("Ingrese un numero Valido")

def BuscarCasa(Numero, CalleB):
    lista_calle = None
    if CalleB == 1:
        lista_calle = ListaCalle1
    elif CalleB == 2:
        lista_calle = ListaCalle2
    elif CalleB == 3:
        lista_calle = ListaCalle3

    if lista_calle:
        for Casita in lista_calle:
            if Casita.Numero == Numero:
                return Casita
        print("La casa que busca no existe")
    else: print("Calle inválida")
    return None

def OrdenarUsuarios(Lista):
    if len(Lista) <= 1:
        return Lista
    
    pivote = Lista[len(Lista)//2].Nombre

    menores = [User for User in Lista if User.Nombre < pivote]
    iguales = [User for User in Lista if User.Nombre == pivote]
    mayores = [User for User in Lista if User.Nombre > pivote]

    return OrdenarUsuarios(menores) + iguales + OrdenarUsuarios(mayores)

def busquedaBinaria(Lista, Valor):
    inicio = 0
    fin = len(Lista) -1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if Lista[medio].Nombre == Valor:
            return medio
        elif Lista[medio].Nombre < Valor:
            inicio = medio + 1
        else:
            fin = medio -1
    return -1

def ValidarExistencia(objeto):
    if objeto: return True
    else: return False

def LimpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def ReiniciarPagos():
    global fechaInicio
    hoy = datetime.now()

    if hoy >= fechaInicio + timedelta(days=30):
        print("Han pasado 30 días, reiniciando pagos de todas las casas")
        for lista in [ListaCalle1, ListaCalle2, ListaCalle3]:
            for casa in lista:
                casa.PagoMensual = False

        fechaInicio = hoy
        print("Pagos reiniciados correctamente")

# Manejo de datos
    # Lista de calles
ListaCalle1, ListaCalle2, ListaCalle3 = [], [], []
    # Lista de usuarios
ListaUsuarios = []
    # Cuota actual 
CuotaActual = -1
fechaInicio = datetime(2025, 10, 25)

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
                    time.sleep(2)
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
            LimpiarPantalla()
            while True:
                if ValidarExistencia(ListaCalle1) == True:
                    print("Calle 1")
                    MostrarCasas(ListaCalle1)
                if ValidarExistencia(ListaCalle2) == True:
                    print("Calle 2")
                    MostrarCasas(ListaCalle2)
                if ValidarExistencia(ListaCalle3) == True:
                    print("Calle 3")
                    MostrarCasas(ListaCalle3)
                Salir = TryCatchInt([1], "Si desea salir escriba 1")
                if Salir == 1:
                    break
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
        LimpiarPantalla()

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
                time.sleep(2)
                LimpiarPantalla()
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
    LimpiarPantalla()

    ReiniciarPagos()