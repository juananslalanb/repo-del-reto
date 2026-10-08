import copy #importamos la libreria copy para poder hacer copias de diccionarios y listas sin que se modifiquen los originales

Lista_de_flota = [] # lista que almacena los nombres de los aviones
nombre_pieza = {} # diccionario que almacena los nombres de las piezas
lista_de_diccionario_de_flota = []  # lista que almacena los diccionarios de cada avión, cada diccionario contiene la información del avión y sus componentes
lista_modelo = [] # lista que almacena los modelos de los aviones *
casoprincipal = 1 # variable que controla el menú principal
caso2principal= 1 # variable que controla el submenú de añadir un avión *
caso2sub1= 1 # variable que controla el submenú de añadir un componente
caso1sub1 = 1 # variable que controla el submenú de ver la lista de componentes de un avión
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
                        nombreinfo["1- COMPONENTES"][nombrepiezaconnumero]= {"actual" : 0, "max" : tiempomaxpieza}
            contadordepiezas += 1
            componenteasumarcontador = contadordepiezas
        lista_de_diccionario_de_flota.append(nombreinfo)
        print(lista_de_diccionario_de_flota)
        caso2sub1 = 1
        contadordeaviones +=1
    if casoprincipal == 3:
        print(Lista_de_flota)
        elementoacambiar = int(input("que avion desea cambiar?"))
        print(lista_de_diccionario_de_flota[elementoacambiar])
        while caso3sub1 == 0 or caso3sub1==1:
            caso3sub1=int(input("desea cambiar \n 0- INFO \n 1- COMPONENTES \n"))
            if caso3sub1 == 0:
                print(lista_de_diccionario_de_flota[elementoacambiar])
                nombrenuevo = input("cual es el nuevo nombre").upper()
                k = (f"{elementoacambiar}  - ")
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["0- MODELO"] = nombrenuevo
                              
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["1- MATRICULA"] = input("ingrese la matricula del avion: ")
                lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["2- HORAS DE VUELO"] = int(input("ingrese las horas de vuelo del avion: "))
                Lista_de_flota[elementoacambiar]= k + nombrenuevo
            if caso3sub1 == 1:
                print(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
                componenteasumarcontador = len(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
                l = (f"{componenteasumarcontador} - ")
                nombrecomponenteasumar = input("Nombre componente a sumar").upper()
                nombrecomponenteasumarnumerado = l + nombrecomponenteasumar 
            
                
                tiempomaxpiezasumada = int(input("tiempo maximo para cambio de pieza nueva"))
                
                lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"][nombrecomponenteasumarnumerado] = tiempomaxpiezasumada
                print(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
            
    if casoprincipal == 4:
        caso4sub1 = 1
        while caso4sub1 == 1 or caso4sub1 == 2:
            caso4sub1 = int(input("Que desea hacer \n 1- analizar las aeronaves \n 2- analisis post vuelo \n"))
            if caso4sub1 == 1:
                print(Lista_de_flota)
                avionanalizar = int(input("que avion desea analizar"))
                modelo_av = lista_de_diccionario_de_flota[avionanalizar]["0- INFO"]["0- MODELO"]
                piezas_vencidas = []
                print("Estado componendetes del avion", modelo_av)
                for Q, datos in lista_de_diccionario_de_flota[avionanalizar]["1- COMPONENTES"].items():
                    if datos["actual"] > datos["max"]:
                        print(f" ALERTA: El componente '{Q}' ALCANZÓ SU TOPE ({datos["actual"]}/{datos["max"]} hs)!")
                        caso4sub12 = int(input("Reparar todo? \n 0- si \n 1- no "))
                        if caso4sub12 == 0:
                            lista_de_diccionario_de_flota[avionanalizar]["0- INFO"]["2- HORAS DE VUELO"] = 0
                            print("El avion",lista_de_diccionario_de_flota[avionanalizar]["0- INFO"]["0- MODELO"], "PUEDE VOLAR SEGUN EL COMPONENTE", Q)
                    else: 
                        print(f"Componente '{Q}' en estado óptimo ({datos["actual"]}/{datos["max"]} hs).")
                if piezas_vencidas:
                    caso4sub12 = int(input("desea reoarar las piezas vencidas? \n 0- si \n 1- no "))
                    if caso4sub12 == 0:
                        for pieza in piezas_vencidas:
                            lista_de_diccionario_de_flota[avionanalizar]["1- COMPONENTES"][pieza]["actual"] = 0
                            print(f"Componente '{pieza}' reparado. Ahora en estado óptimo (0/{lista_de_diccionario_de_flota[avionanalizar]['1- COMPONENTES'][pieza]['max']} hs).")
                else: 
                    print("Todos los componentes estan  bien.")
            if caso4sub1 == 2:
                print(Lista_de_flota)
                avionqsale = int(input("numero del avion que salio"))
                tiempo_vuelo_vuelta = int(input("cuanto tiempo volo el avion en cuestion"))
                lista_de_diccionario_de_flota[avionqsale]["0- INFO"]["2- HORAS DE VUELO"] += tiempo_vuelo_vuelta
                modelo_av = lista_de_diccionario_de_flota[avionqsale]["0- INFO"]["0- MODELO"]
                piezas_vencidas_post = []
                print("Estado componendetes del avion", modelo_av, "despues del vuelo")
                for m, datos in lista_de_diccionario_de_flota[avionqsale]["1- COMPONENTES"].items():
                    datos["actual"] += tiempo_vuelo_vuelta
                    if datos["actual"] >= datos["max"]:
                        print(f" ALERTA: El componente '{m}' ALCANZÓ SU TOPE ({datos["actual"]}/{datos["max"]} hs)!")
                        daño = True
                    else: 
                        print("El avion",lista_de_diccionario_de_flota[avionqsale]["0- INFO"]["0- MODELO"], "PUEDE VOLAR")  
                        daño = False
                if piezas_vencidas_post:    
                    caso4sub12 = int(input("Reparar todo? \n 0- si \n 1- no "))
                    if caso4sub12 == 0:
                        for pieza_dañada in piezas_vencidas_post:
                            lista_de_diccionario_de_flota[avionqsale]["1- COMPONENTES"][pieza_dañada]["actual"] = 0
                            print(f"Componente '{pieza_dañada}' reparado. Ahora en estado EXCELENTE (0/{lista_de_diccionario_de_flota[avionqsale]['1- COMPONENTES'][pieza_dañada]['max']} hs).")
                        print("Todos los componentes han sido reparados. El avión está listo para volar nuevamente.")
            
                
                                   
    caso4sub12 = 2
    caso4sub12 = 0
    contadordepiezas = 0    
    caso1sub1 = 1
    caso2sub1= 1
    caso3sub1 = 0
    caso3sub2 = 1
    caso4sub1 = 1 
    componenteasumarcontador = 0
    caso4sub12 = 11
    