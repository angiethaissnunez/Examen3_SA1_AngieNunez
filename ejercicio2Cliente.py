import socket

# Configuración del socket
HOST = '192.168.0.11'
PORT = 8087

# Conexión al servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Ingreso de la cadena de texto
    print("")
    print("===============================================Sigue la intrucciones===============================================")
    print("1. Primero introduce El pais:01=Honduras, 02=Costa Rica, 03=Mexico")
    print("2. Introduce tu edad:23")
    print("3. Tu genero:F=Femenino, M=Masculino")
    print("4. Introduce Tu fecha de nacimiento:anio,mes y dia, ejemplo(20000205)")
    print("5. Y por ultimo tu nombre:Angie Nunez")
    print("")
    cadenaDatos = input("Dijite una cadena de texto: ejemplo(0123F20000205Angie Nunez):")
    print("")

    # Envío de la cadena de texto al servidor
    s.sendall(cadenaDatos.encode())

    # Recepción de la respuesta del servidor
    respuesta = s.recv(1024).decode()

    # Impresión de la respuesta del servidor
    print(respuesta)
    print("")
    print("ʕ•́ᴥ•̀ʔっ   Bye!!")
    print("👋≧◉ᴥ◉≦   Bye!!")
    print(" (✿◠‿◠)")