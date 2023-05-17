import socket
import pickle
import random
from tipos_pesos import *
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Dirección IP y puerto del equipo receptor
HOST = '192.168.0.2'  # Reemplaza con la dirección IP del equipo receptor
PORT = 22222

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Generar paquetes aleatorios
def generar_paquete():
    # Usando el método randint de la biblioteca random generar host destino y origen de forma aleatoria
    origen = f'192.168.101.{random.randint(1, 100)}'
    destino = f'192.168.101.{random.randint(1, 100)}'

    peso = random.choice(list(tipos_pesos.keys()))  # Agregar la clave 'peso' seleccionada del diccionario 'weights'

    # Retornar un diccionario (paquete) con las llaves generadas
    return {'Origen': origen, 'Destino': destino, 'Peso': peso}  
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Clasificar paquetes en las colas según sus pesos
def clasificar_paquete(paquete):
    cola_seleccionada = paquete['Peso']
    return cola_seleccionada, paquete
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Enviar paquetes al equipo receptor
def enviar_paquetes(colas):
    print('-' * 80)
    print("Envío de paquetes".center(80))
    print('-' * 80)
    
    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Conectar al equipo receptor
            s.connect((HOST, PORT))
            # Serializar y enviar los paquetes
            s.sendall(pickle.dumps(colas))
            print("Paquetes enviados con éxito.")
        except socket.error as e:
            print("Error al enviar los paquetes:", e)
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Simulación del proceso de WFQ
def simular_wfq(num_paquetes):

    # Crear diccionario colas -> {1:[], 2:[], 3:[]...}
    colas = {cola: [] for cola in tipos_pesos}

    print('-'*80)
    print('Paquetes generados aleatoriamente'.center(80))
    print('-'*80)

    # Recorrer la cantidad de paquetes especificados por el usuario
    for _ in range(num_paquetes):
        paquete_generado = generar_paquete() # Llamado a la función de generación de paquetes aleatorios
        print(paquete_generado)
        cola, paquete = clasificar_paquete(paquete_generado) # Llamado a la función de clasificación para obtener el peso (cola) de cada paquete
        colas[cola].append(paquete) # Agregar al diccionario 'colas' cada objeto según la llave

    # Envío de los paquetes al equipo receptor
    enviar_paquetes(colas)
#--------------------------------------------------------------------------------------------------------------------------------------------------

simular_wfq(int(input('Ingrese el número de paquetes a generar: ')))
