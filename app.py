
from funciones import *
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Simulación del proceso de WFQ
def simular_wfq(num_paquetes):

    # Crear diccionario colas -> {1:[], 2:[], 3:[]}...
    colas = {cola: [] for cola in weights}

    # Recorrer la cantidad de paquetes especificados por usuario
    for _ in range(num_paquetes):
        paquete_generado = generar_paquete() # Llamado a la función de generación de paquetes aleatorios
        cola, paquete = clasificar_paquete(paquete_generado) # Llamado a la función de clasificación para obtener el peso (cola) de cada paquete
        colas[cola].append(paquete) # Agregar al diccionario 'colas' cada objeto según la llave

    # Llamado a la función de envío de paquetes
    enviar_paquetes()

    # Llamado de la función de recepción y ordenamiento de paquetes, pasando como parámetro el diccionario 'colas'
    recepcion_ordenamiento_paquetes(colas)

#--------------------------------------------------------------------------------------------------------------------------------------------------
entrada_num_paquetes = int(input('Ingrese el número de paquetes a generar: '))
simular_wfq(entrada_num_paquetes)
#--------------------------------------------------------------------------------------------------------------------------------------------------

