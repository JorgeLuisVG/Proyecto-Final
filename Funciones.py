from Clases import Vehiculo
from Main import *

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
        all([Placa[0] in ListABC, Placa[1] in ListABC, Placa[2] in ListABC,
             Placa[3] in ListNum, Placa[4] in ListNum, Placa[5] in ListNum])
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
            print("Retornará un valor", medio)
            return medio
        elif Lista[medio].Nombre < Valor:
            inicio = medio + 1
        else:
            fin = medio -1
    print("Retornará false")
    return -1

def ValidarExistencia(objeto):
    if objeto: return True
    else: return False