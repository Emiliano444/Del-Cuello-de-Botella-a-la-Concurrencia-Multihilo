# ==========================================================
# SERVIDOR TCP SECUENCIAL
# Materia: Aplicaciones de Red
# Python 3
#
# Este servidor SOLO puede atender un cliente a la vez.
# Mientras procesa un cliente, los demás deben esperar.
# ==========================================================

# Librería para trabajar con sockets TCP/IP
import socket

# Librería para usar pausas de tiempo
import time


# ----------------------------------------------------------
# CREACIÓN DEL SOCKET TCP
# ----------------------------------------------------------

# AF_INET  -> usa IPv4
# SOCK_STREAM -> usa TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# ----------------------------------------------------------
# CONFIGURACIÓN DEL SERVIDOR
# ----------------------------------------------------------

# localhost = nuestra propia computadora
# 8000 = puerto donde escuchará el servidor
direccion_servidor = ("localhost", 8000)

print("Iniciando servidor en:", direccion_servidor)

# bind() une el socket al puerto indicado
servidor.bind(direccion_servidor)


# ----------------------------------------------------------
# ACTIVAR MODO ESCUCHA
# ----------------------------------------------------------

# listen(5)
# El servidor aceptará conexiones entrantes.
# El número 5 es la cola máxima de espera.
servidor.listen(5)

print("Servidor esperando conexiones...\n")


# ----------------------------------------------------------
# BUCLE PRINCIPAL DEL SERVIDOR
# ----------------------------------------------------------

while True:

    # ------------------------------------------------------
    # accept()
    #
    # El servidor se detiene aquí hasta que un cliente
    # intente conectarse.
    # ------------------------------------------------------
    conexion, direccion_cliente = servidor.accept()

    print("===================================")
    print("Cliente conectado:", direccion_cliente)

    # ------------------------------------------------------
    # recv()
    #
    # Recibe datos enviados por el cliente.
    # 1024 = cantidad máxima de bytes.
    # ------------------------------------------------------
    mensaje = conexion.recv(1024).decode()

    print("Mensaje recibido del cliente:")
    print(mensaje)

    # ------------------------------------------------------
    # SIMULACIÓN DE PROCESAMIENTO PESADO
    # ------------------------------------------------------
    print("\nProcesando información...")
    print("Esperando 10 segundos...\n")

    # El servidor queda "ocupado"
    time.sleep(10)

    # ------------------------------------------------------
    # RESPUESTA AL CLIENTE
    # ------------------------------------------------------
    respuesta = "Servidor: mensaje recibido correctamente"

    # encode() convierte texto a bytes
    conexion.sendall(respuesta.encode())

    print("Respuesta enviada al cliente")

    # ------------------------------------------------------
    # CERRAR CONEXIÓN
    # ------------------------------------------------------
    conexion.close()

    print("Conexión cerrada")
    print("--" * 30)