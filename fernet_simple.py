# coding=utf-8
from cryptography.fernet import Fernet
import time

print "Securizador sencillito de cadenas de texto \n"
time.sleep(2)

print "Vamos a generar nuestra key única:"
time.sleep(2)
key = Fernet.generate_key()
print key
time.sleep(1)
print "\nEsta es nuestra key, generada aleatoriamente. Protege esto con tu vida o podrán leer lo que escribes\n"
time.sleep(5)
f = Fernet(key)

love = raw_input("Ahora introduce lo que quieras encriptar, como un mensaje confesando tu amor por mí: ")
token_love = f.encrypt(love)
time.sleep(2)
print "\nEl mensaje ya ha sido encriptado con tu key, imagina que está guardado en una base datos. Para cualquiera que " \
      "quiera leerlo verá lo siguiente:"
time.sleep(4)
print token_love
time.sleep(2)

print "\nAhora, para leer lo que hemos escrito necesitaremos la key, por lo que si solo quieres que lo lea su " \
      "destinatario, solo él puede tener la key además de tí."
time.sleep(6)
print "\nPasamos el mensaje encriptado por la key y..."
amor_desencriptado = f.decrypt(token_love)
time.sleep(2)
print "\nvoilà! aquí tienes tu mensaje desencriptado:"
time.sleep(1.5)
print amor_desencriptado