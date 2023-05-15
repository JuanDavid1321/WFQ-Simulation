import random
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Definir los pesos asignados a cada cola
weights = {
    '1': 1,
    '2': 2,
    '3': 3
}
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Generar paquetes aleatorios
def generar_paquete():
    # Usando el método randint de la biblioteca random generar host destino y origen de forma aleatoria
    origen = f'192.168.101.{random.randint(1, 100)}'
    destino = f'192.168.101.{random.randint(1, 100)}'

    peso = random.choice(list(weights.keys()))  # Agregar la clave 'peso' seleccionada del diccionario 'weights'

    # Retornar un diccionario (paquete) con las llaves generadas
    return {'Origen': origen, 'Destino': destino, 'Peso': peso}  
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Clasificar paquetes en las colas según sus pesos
def clasificar_paquete(paquete):
    cola_seleccionada = paquete['Peso']
    return cola_seleccionada, paquete
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Enviar paquetes de las colas
def enviar_paquetes():
    print('-' * 80)
    print("Envío de paquetes".center(80))
    print('-' * 80)
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Recepción y ordenamiento de paquetes
def recepcion_ordenamiento_paquetes(colas):
    # Crear la lista vacía
    paquetes_recibidos = []

    # Recorrer el diccionario 'colas' recibido como parámetro
    for cola in colas:
        paquetes_recibidos.extend(colas[cola])

    # Ordenar según el peso (cola) los paquetes
    paquetes_recibidos.sort(key=lambda p: weights[p['Peso']])

    print("Paquetes recibidos y ordenados por peso".center(80))
    print('-' * 80)
    for paquete in paquetes_recibidos:
        print(paquete)