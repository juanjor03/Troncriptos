import random

class Desplazamiento:
    def cifrar(texto,desplazamiento):
        cifrado = ""
        for i in range(len(texto)):
            char=texto[i]
            cifrado+= chr((ord(char) + desplazamiento)%256)
        return cifrado
    def descifrar(texto,desplazamiento):
        plano = ""
        for i in range(len(texto)):
            char=texto[i]
            plano+= chr((ord(char) - desplazamiento)%256)
        return plano
    def clave():
        return(random.randint(0,255))
        
        

#class Vigenere:
#    def criptoanalisis(texto):


    

#class Afin:
    #def cifrar():
    #def descifrar():
