from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import DSA
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
import random

#============================================================================
class FirmaDigitalDSA:
    def firma(texto,clave):
        mensaje=texto.encode('utf-8')
        hash_obj=SHA256.new(mensaje)
        signer=DSS.new(clave,'fips-186-3')
        firma=signer.sign(hash_obj)
        return(firma.hex()) ##RETORNA string
    def verificar(texto,clave,firma):
        firma=bytes.fromhex(firma)
        mensaje=texto.encode('utf-8')
        hash_obj = SHA256.new(mensaje)
        verifier=DSS.new(clave,'fips-186-3')
        try:
            verifier.verify(hash_obj, firma)
            return('EL MENSAJE ES AUTÉNTICO')
        except ValueError:
            return('EL MENSAJE NO ES AUTÉNTICO')
    def clave(): 
        key=DSA.generate(2048)
        return(key)
#============================================================================
class FirmaDigitalRSA:
    def firma(texto,clave):
        n,b,a,p,q=clave.n,clave.e,clave.d,clave.p,clave.q
        textoEntero=0
        j=len(texto)-1
        for i in range(len(texto)):
            textoEntero+=(ord(texto[i])-65)*(26**j)
            j-=1
        firma=pow(textoEntero,a,n)
        return(firma)
    def verificar(texto,clave,firma):
        n,b=clave.n,clave.e
        textoEntero=0
        j=len(texto)-1
        for i in range(len(texto)):
            textoEntero+=(ord(texto[i])-65)*(26**j)
            j-=1
        verifier=pow(firma,b,n)
        if(verifier==textoEntero):
            return('EL MENSAJE ES AUTÉNTICO')
        else:
            return('EL MENSAJE NO ES AUTÉNTICO')
    def clave(): 
        key=RSA.generate(2048)
        return(key)
#============================================================================
class FirmaDigitalElGamal:
    def firmar(texto,g,p,a):
        m=0
        j=len(texto)-1
        for i in range(len(texto)):
            m+=(ord(texto[i])-65)*(26**j)
            j-=1
        b=random.randint(2,p-1) ##b=k en la presentación del profe
        mcd=FirmaDigitalElGamal.mcd(b,p-1)
        if(mcd!=1):
            while(mcd!=1):
                b=random.randint(2,p-1) ##b=k en la presentación del profe
                mcd=FirmaDigitalElGamal.mcd(b,p-1)

        gamma=pow(g,b,p)
        kInv=FirmaDigitalElGamal.moduloInverso(b,p-1)
        delta=((m-(a*gamma))*kInv)%(p-1)
        
        gammastr=''
        while gamma > 0:
            residuo = gamma % 26
            gammastr = chr(residuo + 65) + gammastr
            gamma = gamma // 26
        deltastr=''
        while delta > 0:
            residuo = delta % 26
            deltastr = chr(residuo + 65) + deltastr
            delta = delta // 26
        
        return(gammastr,deltastr)
        
    def verificar(texto,gammastr,deltastr,K,g,p):
        m=0
        j=len(texto)-1
        for i in range(len(texto)):
            m+=(ord(texto[i])-65)*(26**j)
            j-=1

        gamma=0
        j=len(gammastr)-1
        for i in range(len(gammastr)):
            gamma+=(ord(gammastr[i])-65)*(26**j)
            j-=1
        delta=0
        j=len(deltastr)-1
        for i in range(len(deltastr)):
            delta+=(ord(deltastr[i])-65)*(26**j)
            j-=1
        
        verifier=(pow(K,gamma,p)*pow(gamma,delta,p))%p
        comparer=(pow(g,m,p))

        if(verifier==comparer):
            return('EL MENSAJE ES AUTÉNTICO')
        else:
            return('EL MENSAJE NO ES AUTÉNTICO')
    
    def mcd(x,y):
        w,z,u,v=0,1,1,0
        while(x != 0):
            q,r=y//x , y%x
            m,n = w-u*q, z-v*q
            y,x,w,z,u,v=x,r,u,v,m,n
        gcd=y
        return(gcd)
    
    def euclidian(x,y):
        w,z,u,v=0,1,1,0
        while(x != 0):
            q,r=y//x , y%x
            m,n = w-u*q, z-v*q
            y,x,w,z,u,v=x,r,u,v,m,n
        gcd=y
        return(gcd,w,z)
        
    def moduloInverso(x,m):
        gcd,w,z=FirmaDigitalElGamal.euclidian(x,m)
        if gcd!=1:
            return None
        else:
            return w%m
        
    def clave():
        p=2305843009213693951 ##p = p en la presentacion del profe
        g=random.randint(2,20) ##g = alpha en la presentacion del profe
        a=random.randint(0,p-1)#random.randint(21702,p-1)##clave privada ##a = a en la presentacion del profe
        K=pow(g,a,p)#132#pow(g,a,p) ##K=beta  en la presentacion del profe
        
        return(g,p,K,a)##g,p,K publicas y a privada