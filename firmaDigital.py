from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import DSA
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256

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
        return(firma.hex())
    def verificar(texto,clave,firma):
        return('EL MENSAJE ES AUTÉNTICO')
        return('EL MENSAJE NO ES AUTÉNTICO')
    def clave(): 
        key=RSA.generate(2048)
        return(key)
#============================================================================
f=open("Prueba/clavePrivadaFirmaDSA.pem","r")
clave=DSA.import_key(f.read().encode('utf-8'))
f.close()
g=open("Prueba/clavePublicaFirmaDSA.pem","r")
clave2=DSA.import_key(g.read().encode('utf-8'))
g.close()
texto='Hola amiguitos'
print('TEXTO:',texto)
firma=FirmaDigitalDSA.firma(texto,clave)
a=firma
print(a)
c=FirmaDigitalDSA.verificar(texto,clave2,a)
print(c)