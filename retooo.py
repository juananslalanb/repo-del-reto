import copy

# Estructuras principales
Lista_de_flota = []
lista_de_diccionario_de_flota = [] 


avion_plantilla = {
    "0- INFO": {
        "0- MODELO": "",
        "1- MATRICULA": "",
        "2- HORAS DE VUELO": 0,
    },
    "1- COMPONENTES": {}
}

contadordeaviones = 0

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    casoprincipal = int(input("¿Qué desea hacer?\n 1- Ver listas\n 2- Añadir un avión\n 3- Editar un avión\n 4- Analizar tiempo de uso / Post-vuelo\n 5- Salir\nOpción: "))
    
    if casoprincipal == 5:
        print("Saliendo del sistema...")
        break

    elif casoprincipal == 1:
        if not Lista_de_flota:
            print("\nNo hay aviones registrados en la flota.")
        else:
            print("\n--- LISTA DE FLOTA ---")
            for idx, av in enumerate(Lista_de_flota):
                print(f"{idx} - {av}")
            
            caso1sub1 = int(input("\n¿Qué desea hacer?\n 1- Ver detalles/componentes de un avión\n 2- Volver al menú principal\nOpción: "))
            if caso1sub1 == 1:
                a = int(input("Ingrese el índice del avión a consultar: "))
                if 0 <= a < len(lista_de_diccionario_de_flota):
                    info = lista_de_diccionario_de_flota[a]
                    print(f"\nINFORMACIÓN DE {Lista_de_flota[a]}:")
                    print("Info General:", info["0- INFO"])
                    print("Componentes:", info["1- COMPONENTES"])
                else:
                    print("Índice no válido.")

    
    elif casoprincipal == 2:
        i = f"{contadordeaviones} - "
        nombre = input("Ingrese el modelo del avión: ").upper()
        nombreinfo = copy.deepcopy(avion_plantilla)
        
        nombreconnumero = i + nombre
        Lista_de_flota.append(nombreconnumero)
        
        nombreinfo["0- INFO"]["0- MODELO"] = nombre
        nombreinfo["0- INFO"]["1- MATRICULA"] = input("Ingrese la matrícula del avión: ")
        nombreinfo["0- INFO"]["2- HORAS DE VUELO"] = int(input("Ingrese las horas de vuelo del avión: "))
        
        contadordepiezas = 0
        while True:
            caso2sub1 = int(input("\n¿Desea añadir un componente?\n 1- Sí\n 2- No\nOpción: "))
            if caso2sub1 == 1:
                j = f"{contadordepiezas} - "
                nombrepieza = input("Nombre de la pieza: ").upper()
                nombrepiezaconnumero = j + nombrepieza
                tiempomaxpieza = int(input("Tiempo máximo para cambio de pieza (hs): "))
                
                
                nombreinfo["1- COMPONENTES"][nombrepiezaconnumero] = {"actual": 0, "max": tiempomaxpieza}
                contadordepiezas += 1
            else:
                break
                
        lista_de_diccionario_de_flota.append(nombreinfo)
        contadordeaviones += 1
        print(f"\nAvión '{nombreconnumero}' registrado con éxito.")

    elif casoprincipal == 3:
        if not Lista_de_flota:
            print("\nNo hay aviones registrados para editar.")
        else:
            print("\n--- AVIONES DISPONIBLES ---")
            for idx, av in enumerate(Lista_de_flota):
                print(f"{idx} - {av}")
                
            elementoacambiar = int(input("¿Qué avión desea modificar?: "))
            if 0 <= elementoacambiar < len(lista_de_diccionario_de_flota):
                caso3sub1 = int(input("\n¿Qué desea editar?\n 0- Info General\n 1- Añadir Componente\nOpción: "))
                
                if caso3sub1 == 0:
                    nombrenuevo = input("Nuevo modelo: ").upper()
                    k = f"{elementoacambiar} - "
                    
                    lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["0- MODELO"] = nombrenuevo
                    lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["1- MATRICULA"] = input("Ingrese la matrícula: ")
                    lista_de_diccionario_de_flota[elementoacambiar]["0- INFO"]["2- HORAS DE VUELO"] = int(input("Ingrese horas de vuelo: "))
                    Lista_de_flota[elementoacambiar] = k + nombrenuevo
                    print("Información actualizada.")
                    
                elif caso3sub1 == 1:
                    componenteasumarcontador = len(lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"])
                    l = f"{componenteasumarcontador} - "
                    nombrecomponenteasumar = input("Nombre del componente nuevo: ").upper()
                    nombrecomponenteasumarnumerado = l + nombrecomponenteasumar 
                    tiempomaxpiezasumada = int(input("Tiempo máximo para cambio de pieza (hs): "))
                    
                    lista_de_diccionario_de_flota[elementoacambiar]["1- COMPONENTES"][nombrecomponenteasumarnumerado] = {
                        "actual": 0, 
                        "max": tiempomaxpiezasumada
                    }
                    print("Componente añadido correctamente.")
            else:
                print("Índice no válido.")

    elif casoprincipal == 4:
        if not Lista_de_flota:
            print("\nNo hay aviones registrados.")
        else:
            caso4sub1 = int(input("\n¿Qué desea hacer?\n 1- Analizar estado de aeronave\n 2- Análisis post-vuelo\nOpción: "))
            
        
            if caso4sub1 == 1:
                for idx, av in enumerate(Lista_de_flota):
                    print(f"{idx} - {av}")
                avionanalizar = int(input("¿Qué avión desea analizar?: "))
                
                if 0 <= avionanalizar < len(lista_de_diccionario_de_flota):
                    modelo_av = lista_de_diccionario_de_flota[avionanalizar]["0- INFO"]["0- MODELO"]
                    piezas_vencidas = []
                    print(f"\nEstado de componentes del avión '{modelo_av}':")
                    
                    
                    for comp, datos in lista_de_diccionario_de_flota[avionanalizar]["1- COMPONENTES"].items():
                        if datos["actual"] >= datos["max"]:
                            print(f"  [ALERTA] El componente '{comp}' ALCANZÓ O SUPERÓ SU TOPE ({datos['actual']}/{datos['max']} hs)!")
                            piezas_vencidas.append(comp) 
                        else:
                            print(f"  [OK] Componente '{comp}' en estado óptimo ({datos['actual']}/{datos['max']} hs).")
                    
                    
                    if piezas_vencidas:
                        reparar = int(input("\n¿Desea reparar/reemplazar ÚNICAMENTE las piezas vencidas?\n 0- Sí\n 1- No\nOpción: "))
                        if reparar == 0:
                            for pieza in piezas_vencidas:
                                
                                lista_de_diccionario_de_flota[avionanalizar]["1- COMPONENTES"][pieza]["actual"] = 0
                                print(f"  Componente '{pieza}' reparado. Ahora tiene 0/{lista_de_diccionario_de_flota[avionanalizar]['1- COMPONENTES'][pieza]['max']} hs.")
                            print("Las piezas vencidas han sido reestablecidas. El resto conservó su uso actual.")
                    else:
                        print("Todos los componentes están dentro de sus límites de uso.")

            
            elif caso4sub1 == 2:
                for idx, av in enumerate(Lista_de_flota):
                    print(f"{idx} - {av}")
                avionqsale = int(input("Seleccione el avión que realizó el vuelo: "))
                
                if 0 <= avionqsale < len(lista_de_diccionario_de_flota):
                    tiempo_vuelo_vuelta = int(input("Ingrese las horas del vuelo realizado: "))
                    
                    
                    lista_de_diccionario_de_flota[avionqsale]["0- INFO"]["2- HORAS DE VUELO"] += tiempo_vuelo_vuelta
                    modelo_av = lista_de_diccionario_de_flota[avionqsale]["0- INFO"]["0- MODELO"]
                    piezas_vencidas_post = []
                    
                    print(f"\nEstado de componentes de '{modelo_av}' tras sumar {tiempo_vuelo_vuelta} hs de vuelo:")
                    
                    
                    for m, datos in lista_de_diccionario_de_flota[avionqsale]["1- COMPONENTES"].items():
                        datos["actual"] += tiempo_vuelo_vuelta
                        if datos["actual"] >= datos["max"]:
                            print(f"  [ALERTA] El componente '{m}' LLEGÓ AL LÍMITE DE USO ({datos['actual']}/{datos['max']} hs)!")
                            piezas_vencidas_post.append(m)
                        else:
                            print(f"  [OK] Componente '{m}' en estado óptimo ({datos['actual']}/{datos['max']} hs).")
                    
                    
                    if piezas_vencidas_post:
                        reparar = int(input("\n¿Desea reparar/reemplazar ÚNICAMENTE los componentes alertados?\n 0- Sí\n 1- No\nOpción: "))
                        if reparar == 0:
                            for pieza_dañada in piezas_vencidas_post:
                
                                lista_de_diccionario_de_flota[avionqsale]["1- COMPONENTES"][pieza_dañada]["actual"] = 0
                                print(f"  Componente '{pieza_dañada}' reestablecido a 0 hs.")
                            print("Mantenimiento finalizado. Los demás componentes conservan sus horas correspondientes.")