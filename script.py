def calcular_altitud(presion_hpa):
    altitud = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
    return altitud


def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    if altitud_actual > altitud_previa:
        estado = 1
    else:
        if aceleracion > -3.0:
            estado = 3
        else:
            estado = 2
    return estado


def evaluar_alerta_temperatura(temp_celsius):
    if temp_celsius > 80.0:
        alerta = True
    else:
        alerta = False
    return alerta


def texto_estado(codigo_estado):
    if codigo_estado == 1:
        texto = "Ascenso"
    elif codigo_estado == 2:
        texto = "Apogeo / Caida libre"
    else:
        texto = "Despliegue de Paracaidas"
    return texto


def main():
    tiempo = 0
    altitud_previa = 0.0
    altitud_maxima = 0.0
    apogeo_detectado = False
    suma_temperaturas = 0.0
    contador_lecturas = 0
    aceleracion_maxima = 0.0

    while True:
        print("--- Segundo " + str(tiempo) + " ---")
        entrada = input("Presione ENTER para continuar o escriba 'fin' para terminar: ")

        if entrada.strip().lower() == "fin":
            print("Simulacion finalizada.")
            break

        presion = float(input("Presion (hPa): "))
        aceleracion = float(input("Aceleracion (m/s^2): "))
        temperatura = float(input("Temperatura (C): "))

        altitud_actual = calcular_altitud(presion)

        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        if apogeo_detectado == False and altitud_actual < altitud_previa:
            apogeo_detectado = True
            print(">> APOGEO DETECTADO <<")

        codigo_estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        estado_legible = texto_estado(codigo_estado)

        alerta_activa = evaluar_alerta_temperatura(temperatura)

        contador_lecturas = contador_lecturas + 1
        suma_temperaturas = suma_temperaturas + temperatura
        temperatura_promedio = suma_temperaturas / contador_lecturas

        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        print("Altitud actual: " + str(round(altitud_actual, 2)) + " m")
        print("Estado de vuelo: " + estado_legible)
        print("Altitud maxima: " + str(round(altitud_maxima, 2)) + " m")
        print("Temperatura promedio: " + str(round(temperatura_promedio, 2)) + " C")
        print("Aceleracion maxima: " + str(round(aceleracion_maxima, 2)) + " m/s^2")

        if alerta_activa:
            print("ALERTA: Temperatura critica detectada.")

        altitud_previa = altitud_actual
        tiempo = tiempo + 1

        if apogeo_detectado and altitud_actual <= 0:
            print("El cohete ha aterrizado.")
            break


main()