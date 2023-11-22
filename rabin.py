import Crypto
from Crypto.PublicKey import Rabin
from Crypto import Random
import ast

random_generator = Random.new().read
key = Rabin.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

print("La clave pública es:", publickey.n) #print the public key
print("La clave privada es:", (key.p, key.q)) #print the private key

opcion = input("¿Quieres encriptar o desencriptar un mensaje con Rabin? (E/D): ") #ask the user to choose an option

if opcion == "E": #if the user wants to encrypt
    message = input("Introduce el texto a encriptar con Rabin: ") #read the message from the console
    encrypted = publickey.encrypt(message, 32) #encrypt the message with Rabin
    print ('encrypted message with Rabin:', encrypted) #ciphertext
elif opcion == "D": #if the user wants to decrypt
    encrypted = input("Introduce el texto a desencriptar con Rabin: ") #read the ciphertext from the console
    decrypted = key.decrypt(ast.literal_eval(str(encrypted))) #decrypt the ciphertext with Rabin
    print ('decrypted with Rabin', decrypted) #message
else: #if the user enters an invalid option
    print("Opción no válida. Por favor, elige E o D.") #print an error message
