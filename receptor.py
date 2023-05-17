import socket
import pickle
from tipos_pesos import tipos_pesos
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Dirección IP y puerto del equipo receptor
HOST = '192.168.20.13'  # Reemplaza con la dirección IP de este equipo
PORT = 22222

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Recepción y ordenamiento de paquetes
def recepcion_ordenamiento_paquetes():
    # Crear la lista vacía
    paquetes_recibidos = []

    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Enlace del socket a una dirección y puerto
        s.bind((HOST, PORT))

        # Escucha las conexiones entrantes (solo 1 en este caso)
        s.listen(1)

        print("Esperando conexión...")

        # Aceptar la conexión entrante
        conn, addr = s.accept()
        with conn:

            print('Conexión establecida desde', addr)

            # Recibir los datos y deserializarlos
            data = conn.recv(4096)
            colas = pickle.loads(data)

            # Ordenar según el peso (cola) los paquetes
            for cola in colas:
                paquetes_recibidos.extend(colas[cola])
            paquetes_recibidos.sort(key=lambda p: tipos_pesos[p['Peso']]) # Agregar reverse=True para cambiar la prioridad

            print("Paquetes recibidos y ordenados por peso".center(80))
            print('-' * 80)
            for paquete in paquetes_recibidos:
                print(paquete)
#--------------------------------------------------------------------------------------------------------------------------------------------------

recepcion_ordenamiento_paquetes()
