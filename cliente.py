# ==========================================================
# CLIENTE TCP
# Materia: Aplicaciones de Red
# Python 3 
# ==========================================================

# Librería para sockets
import socket


# ----------------------------------------------------------
# CREAR SOCKET TCP
# ----------------------------------------------------------

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# ----------------------------------------------------------
# DATOS DEL SERVIDOR
# ----------------------------------------------------------

direccion_servidor = ("localhost", 8000)

print("Conectando al servidor...")

# connect() intenta conectarse al servidor
cliente.connect(direccion_servidor)

print("Conexión exitosa\n")


# ----------------------------------------------------------
# MENSAJE ESCRITO POR EL USUARIO
# ----------------------------------------------------------

mensaje = input("Escribe un mensaje para el servidor: ")

# sendall() envía datos al servidor
cliente.sendall(mensaje.encode())

print("\nMensaje enviado")
print("Esperando respuesta del servidor...\n")


# ----------------------------------------------------------
# RECIBIR RESPUESTA
# ----------------------------------------------------------

respuesta = cliente.recv(1024).decode()

print("Respuesta del servidor:")
print(respuesta)


# ----------------------------------------------------------
# CERRAR SOCKET
# ----------------------------------------------------------

cliente.close()

print("\nConexión cerrada")