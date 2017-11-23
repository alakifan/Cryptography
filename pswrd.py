# coding=utf-8
import base64
import os
import time
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

print "En este programa solo podrás leer el mensaje desencriptado si pones la contraseña correcta"
time.sleep(3)
pswrd = raw_input("Introduce la contraseña para la key: ")

# Generamos unos bytes aleatorios utilizando el método del propio sistema operativo
bytes_aleatorios = os.urandom(16)

# Deriva los bytes aleatorios el número de veces que se le indique con una función pseudoaleatoria
key_derivation_func = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=bytes_aleatorios,
                 iterations=100000, # Tan grande como se pueda, 100000 por lo menos
                 backend=default_backend())

# Crea la key final en base a la KDF y la contraseña introducida
key = base64.urlsafe_b64encode(key_derivation_func.derive(pswrd))

# A partir de aquí es igual que en el otro ejemplo
f = Fernet(key)
msg = raw_input("Introduce tu mensaje a codificar: ")
msg_encriptado = f.encrypt(msg)

# Este código se repetirá hasta que se introduzca la misma contraseña que antes
while True:
    pswrd2 = raw_input("Vuelve a introducir la contraseña para ver el mensaje: ")

    try:
        # Hace lo mismo que la primera KDF, y al tener los mismos bytes aleatorios e iteraciones, da el mismo resultado
        # Hay que volver a hacerlo porque las KDF son de un solo uso
        key_derivation_func2 = PBKDF2HMAC(algorithm=hashes.SHA256(),
                        length=32,
                        salt=bytes_aleatorios,
                        iterations=100000,
                        backend=default_backend())

        # Se genera la key para desencriptar el mensaje, si pswrd2 es la misma que pswrd,
        # será la misma key que la de encriptación
        key2 = base64.urlsafe_b64encode(key_derivation_func2.derive(pswrd2))

        # Usa la key2 para intentar desencriptar el mensaje, si la contraseña es correcta, lo hará sin problema
        f2 = Fernet(key2)
        print f2.decrypt(msg_encriptado)
        break

    # En caso de que la contraseña fuera incorrecta, saltará la excepción y se volverá a pedir la contraseña
    except InvalidToken:
        print "¿Ves? Esa contraseña no funciona"
        time.sleep(1)
