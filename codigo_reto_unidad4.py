import copy
internopieza={
    "actual" : " ",
    "max" :  " "
    }
Lista_de_flota = []
nombre_pieza = {}
lista_de_diccionario_de_flota = []
lista_modelo = []
casoprincipal = 1
caso2principal= 1
caso2sub1= 1
caso1sub1 = 1
caso3sub1 = 0
caso3sub2 = 1
caso4sub1 = 1
caso4sub12 = 1
avion = {
    "0- INFO" : {
        "0- MODELO" : "",
        
        "1- MATRICULA" : "",
        
        "2- HORAS DE VUELO" : "",
        
    },
    "1- COMPONENTES" : {
        
        

       }
}
contadordeaviones = 0
contadordepiezas = 0

while casoprincipal == 1 or casoprincipal == 2 or casoprincipal == 3 or casoprincipal == 4:
    casoprincipal = int(input("que desea hacer? \n 1- ver la listas \n 2- añadir un avion \n 3- editar un avion \n 4- comparar tiempo de uso \n 5-salir \n"))
    i = (f"{contadordeaviones}-  ")

    if casoprincipal == 1:
        print(Lista_de_flota)
        caso1sub1 = 1
        while caso1sub1 == 1:
            caso1sub1 = int(input("que desea hacer? \n 1- ver lista de componentes de un avion \n salir \n"))
            if caso1sub1 == 1:
                print(Lista_de_flota)
                a = int(input("que elemento desea ver:"))
                print(lista_de_diccionario_de_flota[a])
    
            

    if casoprincipal == 2:
        nombre = input("ingrese el modelo del avion: ").upper()
        nombreinfo = copy.deepcopy(avion)
        nombreconnumero = i + nombre
        Lista_de_flota.append(nombreconnumero)
        
        nombreinfo["0- INFO"]["0- MODELO"] = nombre
        nombreinfo["0- INFO"]["1- MATRICULA"] = input("ingrese la matricula del avion: ")
        nombreinfo["0- INFO"]["2- HORAS DE VUELO"] = int(input("ingrese las horas de vuelo del avion: "))
        while caso2sub1 == 1 or caso2sub1 == 2:
            caso2sub1 = int(input("desea añadir un componente? \n 1 si  \n 3 no \n"))
            J = (f"{contadordepiezas}-  ")
        
            if caso2sub1 == 1:
                        nombrepieza = input("nombre de la pieza: ").upper()
                        nombrepiezaconnumero = J + nombrepieza
                        tiempomaxpieza = int(input("tiempo maximo para cambio de pieza: "))
                        tiempoactualpieza = int(input("tiempo actual pieza"))
                        componenteinfo =copy.deepcopy(internopieza)
                        componenteinfo["max"]=tiempomaxpieza
                        componenteinfo["actual"]=tiempoactualpieza

                        nombreinfo["1- COMPONENTES"][nombrepiezaconnumero]=componenteinfo
                        print(nombreinfo)

 
                        
            contadordepiezas += 1
            
        lista_de_diccionario_de_flota.append(nombreinfo)
        print(lista_de_diccionario_de_flota)
        caso2sub1 = 1
        contadordeaviones +=1
    
    contadordepiezas = 0

    if casoprincipal == 3:
        print(Lista_de_flota)
        elementoacambiar = int(input("que avion desea cambiar?"))
        print(lista_de_diccionario_de_flota[elementoacambiar])
        caso3sub1 = 0 
        while caso3sub1 == 0 or caso3sub1==1:
            caso3sub1=int(input("desea cambiar \n 0- INFO \n 1-  AÑADIR COMPONENTES \n"))
            if caso3sub1 == 0:
                print(lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"])
                nombrenuevo = input("cual es el nuevo nombre").upper()
                k = (f"{elementoacambiar}  - ")
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["0- MODELO"] = nombrenuevo
                              
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["1- MATRICULA"] = input("ingrese la matricula del avion: ")
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["2- HORAS DE VUELO"] = int(input("ingrese las horas de vuelo del avion: "))
                Lista_de_flota[elementoacambiar]= k + nombrenuevo
            if caso3sub1 == 1:
                print(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
                l = len(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
                piezaañadir = input("nombre de la pieza que desea añadir").upper()
                
                piezaañadirlista = copy.deepcopy(internopieza)
                piezaañadirlistaactualhoras = int(input("horas actuales de la pieza nueva"))
                piezaañadiralistamaxhoras = int(input("maximo antes de cambio"))
                piezaañadirlista["actual"] = piezaañadirlistaactualhoras
                piezaañadirlista["max"] =  piezaañadiralistamaxhoras
                piezaañadirnumerada = (f"{l}- {piezaañadir}")
                
                lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"][piezaañadirnumerada] = piezaañadirlista
    if casoprincipal == 4:
        print(Lista_de_flota)
        elementoevaluar = int(input("Que avion desea evaluar"))
        tiempoactual = lista_de_diccionario_de_flota[elementoevaluar]["0- INFO"]["2- HORAS DE VUELO"]
        tiempovolado = int(input("cuanto volo el avion"))
        tiempoactualizado = tiempoactual + tiempovolado
        lista_de_diccionario_de_flota[elementoevaluar]["0- INFO"]["2- HORAS DE VUELO"] = tiempoactualizado
        print(f"\n Horas totales del avión actualizadas a: {tiempoactualizado} hrs.")
        for x in lista_de_diccionario_de_flota[elementoevaluar]["1- COMPONENTES"]:
            print("evaluando el componente", x)
            lista_de_diccionario_de_flota[elementoevaluar]["1- COMPONENTES"][x]["actual"]+=tiempovolado
            if lista_de_diccionario_de_flota[elementoevaluar]["1- COMPONENTES"][x]["actual"] < lista_de_diccionario_de_flota[elementoevaluar]["1- COMPONENTES"][x]["max"]:
                print("el componente ", x, "permite el vuelo")
            else:
                print("el componente ", x, "necesita reparacion")
                caso4sub1 = 0
                while caso4sub1 == 0:
                    caso4sub1 = int(input("Reparar \n 0- si \n 1- no"))
                    if caso4sub1 == 0:
                        lista_de_diccionario_de_flota[elementoevaluar]["1- COMPONENTES"][ x]["actual"] = 0
                        print(x, "reparado")