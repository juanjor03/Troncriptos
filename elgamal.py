import Crypto
from Crypto.PublicKey import ElGamal
from Crypto import Random
from Crypto.Util.number import GCD
import ast

random_generator = Random.new().read
key = ElGamal.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

print("La clave pública es:", (publickey.p, publickey.g, publickey.y)) #print the public key
print("La clave privada es:", key.x) #print the private key

opcion = input("¿Quieres encriptar o desencriptar un mensaje con ElGamal? (E/D): ") #ask the user to choose an option

if opcion == "E": #if the user wants to encrypt
    message = input("Introduce el texto a encriptar con ElGamal: ") #read the message from the console
    encrypted = publickey.encrypt(message, 32) #encrypt the message with ElGamal
    print ('encrypted message with ElGamal:', encrypted) #ciphertext
elif opcion == "D": #if the user wants to decrypt
    encrypted = input("Introduce el texto a desencriptar con ElGamal: ") #read the ciphertext from the console
    decrypted = key.decrypt(ast.literal_eval(str(encrypted))) #decrypt the ciphertext with ElGamal
    print ('decrypted with ElGamal', decrypted) #message
else: #if the user enters an invalid option
    print("Opción no válida. Por favor, elige E o D.") #print an error message
