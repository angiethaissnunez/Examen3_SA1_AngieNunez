import socket
from datetime import datetime

def Respuesta_en_cadena(cadenaDatos):
    # Obtenemos los datos de la cadena de la consulta que envia el cliente
    pais = ""
    edad = ""
    genero = ""
    fecha_nac = ""
    nombre = ""
    
    if len(cadenaDatos) >= 20:#0120F20001120Juan Galvez
        pais = cadenaDatos[0:2]#estos son la cantidad de caracteres que va a tomar
        edad = int(cadenaDatos[2:4])
        genero = cadenaDatos[4]
        fecha_nac = datetime.strptime(cadenaDatos[5:13], '%Y%m%d')
        nombre = cadenaDatos[13:]
        
        # Analizamos la edad ingresada
        if edad >= 1 and edad <= 18:
            Dato_edad = "menor de edad"
        elif edad >= 19 and edad <= 50:
            Dato_edad = "adulto"
        elif edad >= 51:
            Dato_edad = "de la tercera edad"
        else:
            Dato_edad = "Upps! edad desconocida"
        
        # Analizamos el país ingresado
        if pais == "01":
            Dato_pais = "Honduras"
        elif pais == "02":
            Dato_pais = "Costa Rica"
        elif pais == "03":
            Dato_pais = "México"
        else:
            Dato_pais = "Ups! país desconocido"
        
        # Analizamos el género ingresado
        if genero == "F" or genero == "f":
            Dato_genero = "femenino"
        elif genero == "M" or genero == "m":
            Dato_genero = "masculino"
        else:
            Dato_genero = "Ups! género desconocido"
        
        # determinar si la edad concuerda con la fecha de nacimiento restando la la fecha actual menos la fecha introducida por el usuario
        fecha_actual = datetime.now()
        edad_calculada = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))

        if edad_calculada == edad:
                respuesta = "Hola {} veo que eres del país de {}, tienes una edad de {} años. Por los datos enviados me indica que eres {}, tambien que tu género es {}, y viendo tu fecha de nacimiento {} me indica que tu edad si concuerda con la fecha de naciemiento que ingresaste.".format(nombre, Dato_pais, edad, Dato_edad, Dato_genero, fecha_nac.strftime('%Y-%m-%d'))
        else:
            respuesta = "Hola {} veo que eres del país de {}, tienes una edad de {} años. Por los datos enviados me indica que eres {}, y tu género es {} pero viendo tu fecha de nacimiento {} la edad tuya no concuerda con tu fecha de nacimiento.".format(nombre, Dato_pais, edad, Dato_edad, Dato_genero,fecha_nac.strftime('%Y-%m-%d'))
        
        return respuesta
    
    return "Cadena de entrada inválida, intentalo nuevamente"


def servidor():
    # Creamos el socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlace del socket a un puerto y dirección
    server_address = ('0.0.0.0', 8087)
    print('Iniciando servidor en {} puerto {}'.format(*server_address))
    sock.bind(server_address)

    # Escuchando conexiones entrantes
    sock.listen(1)

    continuar = True # Variable para controlar el ciclo del servidor

    while True:
        # Esperando conexión
        print('Esperando conexión...')
        connection, client_address = sock.accept()
        print('Conexión desde', client_address)

        try:
            # Recibimos los datos en trozos y decodificamos
            data = connection.recv(1024).decode('utf-8')
            print('Cadena de entrada recibida:', data)

            # Analizamos la cadena y construimos la respuesta
            if data.strip().lower() == 'exit':
                continuar = False # Modificamos el valor de la variable para salir del ciclo
                respuesta = "Saliendo del servidor..."
            else:
                respuesta = Respuesta_en_cadena(data)

            # Enviamos la respuesta
            connection.sendall(respuesta.encode('utf-8'))

        finally:
            # Cerramos la conexión
            connection.close()

if __name__ == '__main__':
    servidor()
