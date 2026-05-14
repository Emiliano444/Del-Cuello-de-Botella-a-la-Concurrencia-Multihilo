# ==========================================================
# SERVIDOR TCP CONCURRENTE
# Materia: Aplicaciones de Red
# Python 3
#
# Este servidor usa HILOS (threads)
# para atender varios clientes al mismo tiempo.
# ==========================================================

# Librería para sockets
import socket

# Librería para pausas
import time

# Librería para concurrencia con hilos
import threading


# ----------------------------------------------------------
# CREAR SOCKET TCP
# ----------------------------------------------------------

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# ----------------------------------------------------------
# CONFIGURAR DIRECCIÓN Y PUERTO
# ----------------------------------------------------------

direccion_servidor = ("localhost", 8000)

print("Iniciando servidor concurrente...")

servidor.bind(direccion_servidor)


# ----------------------------------------------------------
# ACTIVAR MODO ESCUCHA
# ----------------------------------------------------------

servidor.listen(5)

print("Servidor esperando conexiones...\n")


# ----------------------------------------------------------
# FUNCIÓN QUE ATENDERÁ A CADA CLIENTE
# ----------------------------------------------------------

def atender_cliente(conexion, direccion_cliente):

    print("===================================")
    print("Cliente conectado:", direccion_cliente)

    # ------------------------------------------------------
    # RECIBIR MENSAJE
    # ------------------------------------------------------

    mensaje = conexion.recv(1024).decode()

    print("Mensaje recibido:")
    print(mensaje)

    # ------------------------------------------------------
    # SIMULAR PROCESAMIENTO PESADO
    # ------------------------------------------------------

    print("Procesando cliente...")
    print("Esperando 10 segundos...\n")

    time.sleep(10)

    # ------------------------------------------------------
    # RESPONDER AL CLIENTE
    # ------------------------------------------------------

    respuesta = "Servidor concurrente: mensaje recibido"

    conexion.sendall(respuesta.encode())

    print("Respuesta enviada a:", direccion_cliente)

    # ------------------------------------------------------
    # CERRAR CONEXIÓN
    # ------------------------------------------------------

    conexion.close()

    print("Conexión cerrada:", direccion_cliente)
    print("===================================\n")


# ----------------------------------------------------------
# BUCLE PRINCIPAL DEL SERVIDOR
# ----------------------------------------------------------

while True:

    # accept() espera nuevas conexiones
    conexion, direccion_cliente = servidor.accept()

    # ------------------------------------------------------
    # CREAR NUEVO HILO
    # ------------------------------------------------------
    #
    # target = función que ejecutará el hilo
    # args = parámetros para esa función
    # ------------------------------------------------------

    hilo = threading.Thread(
        target=atender_cliente,
        args=(conexion, direccion_cliente)
    )

    # ------------------------------------------------------
    # INICIAR HILO
    # ------------------------------------------------------

    hilo.start()

    # El servidor vuelve inmediatamente a accept()
    # para seguir aceptando clientes nuevos.