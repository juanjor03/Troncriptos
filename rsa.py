import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

print("La clave pública es:", (publickey.n, publickey.e)) #print the public key
print("La clave privada es:", key.d) #print the private key

opcion = input("¿Quieres encriptar o desencriptar un mensaje con RSA? (E/D): ") #ask the user to choose an option

if opcion == "E": #if the user wants to encrypt
    message = input("Introduce el texto a encriptar con RSA: ") #read the message from the console
    encrypted = publickey.encrypt(message, 32) #encrypt the message with RSA
    print ('encrypted message with RSA:', encrypted) #ciphertext
elif opcion == "D": #if the user wants to decrypt
    encrypted = input("Introduce el texto a desencriptar con RSA: ") #read the ciphertext from the console
    decrypted = key.decrypt(ast.literal_eval(str(encrypted))) #decrypt the ciphertext with RSA
    print ('decrypted with RSA', decrypted) #message
else: #if the user enters an invalid option
    print("Opción no válida. Por favor, elige E o D.") #print an error message
