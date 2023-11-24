from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
import ast
import base64,random,math


#============================================================================
class ClavePublicaRsa:
    #tamaño maximo de texto de 32 bytes
    def cifrar(texto,clave):
        cipher = PKCS1_OAEP.new(clave)
        cifrado=cipher.encrypt(texto.encode('utf-8'))
        cifradoStr=base64.b64encode(cifrado).decode('utf-8')
        return(cifradoStr)
    def descifrar(texto,clave):
        textoCifradoBytes=base64.b64decode(texto)
        cipher = PKCS1_OAEP.new(clave)
        descifrado=cipher.decrypt(textoCifradoBytes).decode('utf-8')
        return(descifrado)
    def clave():
        random_generator=Random.new().read
        clave=RSA.generate(1024, random_generator)
        return(clave)
#============================================================================
class ClavePublicaElGamal: 
    def cifrar(texto,g,p,K):
        m=0
        j=len(texto)-1
        for i in range(len(texto)):
            m+=(ord(texto[i])-65)*(26**j)
            j-=1
        b=random.randint(2,p-1)
        y1=pow(g,b,p)
        y2=((pow(K,b,p))*m)%p 
        
        y1str=''
        while y1 > 0:
            residuo = y1 % 26
            y1str = chr(residuo + 65) + y1str
            y1 = y1 // 26
        y2str=''
        while y2 > 0:
            residuo = y2 % 26
            y2str = chr(residuo + 65) + y2str
            y2 = y2 // 26
        
        return(y1str,y2str)
        
    def descifrar(y1str,y2str,a,p):
        y1=0
        j=len(y1str)-1
        for i in range(len(y1str)):
            y1+=(ord(y1str[i])-65)*(26**j)
            j-=1
        y2=0
        j=len(y2str)-1
        for i in range(len(y2str)):
            y2+=(ord(y2str[i])-65)*(26**j)
            j-=1
        y1Inv=pow(y1,p-1-a,p)
        d=(y1Inv*y2)%p
        descifrado=''
        while d > 0:
            residuo = d % 26
            descifrado= chr(residuo + 65) + descifrado
            d = d // 26
        return(descifrado)
    
    def clave():
        p=2305843009213693951
        g=random.randint(2,20)
        a=random.randint(21702,p-1)##clave privada
        K=pow(g,a,p)
        
        return(g,p,K,a)##g,p,K publicas y a privada
 
#============================================================================
class Rabin:
    
    def clave(text):
        text_size_bits = len(text) * 8
        key_size_bits = 2 ** math.ceil(math.log2(text_size_bits * 2))
        key_size_bits = max(512, text_size_bits * 2)
        key = Rabin.generarClave(key_size_bits)
        return key
        
    def generarClave(bit_length):
        p = Rabin.blum_prime(bit_length // 2)
        q = Rabin.blum_prime(bit_length // 2)
        N = p * q
        return N, p, q

    def cifrar(texto, N):
        return pow(texto, 2, N)

    def descifrar(texto, p, q):
        N = p * q
        p1 = pow(texto, (p + 1) // 4, p)
        p2 = p - p1
        q1 = pow(texto, (q + 1) // 4, q)
        q2 = q - q1
        ext = Rabin.gcd(p, q)
        y_p = ext[1]
        y_q = ext[2]
        d1 = (y_p * p * q1 + y_q * q * p1) % N
        d2 = (y_p * p * q2 + y_q * q * p1) % N
        d3 = (y_p * p * q1 + y_q * q * p2) % N
        d4 = (y_p * p * q2 + y_q * q * p2) % N
        return d1, d2, d3, d4

    def gcd(a, b):
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = b, a
        while r != 0:
            q = old_r // r
            r, old_r = old_r - q * r, r
            s, old_s = old_s - q * s, s
            t, old_t = old_t - q * t, t
        return old_r, old_s, old_t

    def blum_prime(bit_length): ##trabajamos con 3 mod 4
        while True:
            p = random.getrandbits(bit_length)
            if p % 4 == 3 and Rabin.is_probable_prime(p):
                return p

    def is_probable_prime(n, k=5):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randint(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

