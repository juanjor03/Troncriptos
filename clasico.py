import random,math,collections,re
import numpy
from numpy.linalg import det
from numpy import zeros,array
import imageio

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
    
#============================================================================

class Afin:
    def euclidian(x,y):
        w,z,u,v=0,1,1,0
        while(x != 0):
            q,r=y//x , y%x
            m,n = w-u*q, z-v*q
            y,x,w,z,u,v=x,r,u,v,m,n
        gcd=y
        return(gcd,w,z)
        
    def moduloInverso(x,m):
        gcd,w,z=Afin.euclidian(x,m)
        if gcd!=1:
            return None
        else:
            return w%m
        
    def cifrar(texto,claveA,claveB):
        cifrado=''
        for i in range(len(texto)):
            if(texto[i]!=' '):
                cifrado+=''.join([chr((claveA*(ord(texto[i])-65)+claveB)%26 + 65)])
            else:
                cifrado+=' '
        return cifrado
    
    def descifrar(texto,claveA,claveB):
        descifrado=''
        for i in range(len(texto)):
            if(texto[i]!=' '):
                descifrado+=''.join([chr((Afin.moduloInverso(claveA,26)*((ord(texto[i])-65)-claveB))%26 + 65)])
            else:
                descifrado+=' '
        
        return descifrado
    
    def clave():
        a=random.choice([i for i in range(0,26) if i not in [0,2,4,6,8,10,12,13,14,16,18,20,22,24]])
        b=random.randint(0,25)
        return(a,b)

#============================================================================    

class Vernam:
    
    def cifrar(texto, clave):
        cifrado = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(texto, clave))
        return cifrado
    
    def descifrar(texto, clave):
        plano = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(texto, clave))
        return plano
    
    def clave(longitud_texto):
        clave = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(longitud_texto))
        return clave

#============================================================================

class Transposicion:

    def cifrar(texto,clave):
        cifrado = ""
 
        k_indx = 0
 
        msg_len = float(len(texto))
        msg_lst = list(texto)
        key_lst = sorted(list(clave))
 
        col = len(clave)

        row = int(math.ceil(msg_len / col))

        fill_null = int((row * col) - msg_len)
        msg_lst.extend(' ' * fill_null)

        matrix = [msg_lst[i: i + col] 
                  for i in range(0, len(msg_lst), col)]

        for _ in range(col):
            curr_idx = clave.index(key_lst[k_indx])
            cifrado += ''.join([row[curr_idx] 
                              for row in matrix])
            k_indx += 1
 
        return cifrado
    
    def descifrar(texto,clave):
        descifrado = ""

        k_indx = 0

        msg_indx = 0
        msg_len = float(len(texto))
        msg_lst = list(texto)

        col = len(clave)

        row = int(math.ceil(msg_len / col))

        key_lst = sorted(list(clave))

        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]
 
        for _ in range(col):
            curr_idx = clave.index(key_lst[k_indx])
 
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        descifrado = ''.join(sum(dec_cipher, []))
 
        return descifrado
    
    def clave(longitud_texto):
        alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        clave = ''
        if (longitud_texto>26):
            longClave=random.randint(4,26)
        else:
            longClave=random.randint(math.ceil(longitud_texto/4),longitud_texto)
        for i in range(longClave):
            if len(alfabeto)>0:
                letra=random.choice(alfabeto)
                alfabeto=alfabeto.replace(letra,'')
                clave+=''.join(letra)
        return clave

#============================================================================

class Vigenere:

    def itemgetter(*items):
        if len(items) == 1:
            item = items[0]
            def g(obj):
                return obj[item]
        else:
            def g(obj):
                return tuple(obj[item] for item in items)
        return g

    def analisis(input):
        target_freqs = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
        uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


        nchars = len(uppercase)
        ordA = ord('A')
        sorted_targets = sorted(target_freqs)

        def frequency(input):
            result = [[c, 0.0] for c in uppercase]
            for c in input:
                result[c - ordA][1] += 1
            return result

        def correlation(input):
            result = 0.0
            freq = frequency(input)
            freq.sort(key=Vigenere.itemgetter(1))

            for i, f in enumerate(freq):
                result += f[1] * sorted_targets[i]
            return result

        cleaned = [ord(c) for c in input.upper() if c.isupper()]
        best_len = 0
        best_corr = -100.0

        for i in range(2, len(cleaned) // 20):
            pieces = [[] for _ in range(i)]
            for j, c in enumerate(cleaned):
                pieces[j % i].append(c)

            corr = -0.5 * i + sum(correlation(p) for p in pieces)

            if corr > best_corr:
                best_len = i
                best_corr = corr

        if best_len == 0:
            return ("El texto es demasiado corto para analizar", "")

        pieces = [[] for _ in range(best_len)]
        for i, c in enumerate(cleaned):
            pieces[i % best_len].append(c)

        freqs = [frequency(p) for p in pieces]

        key = ""
        for fr in freqs:
            fr.sort(key=Vigenere.itemgetter(1), reverse=True)

            m = 0
            max_corr = 0.0
            for j in range(nchars):
                corr = 0.0
                c = ordA + j
                for frc in fr:
                    d = (ord(frc[0]) - c + nchars) % nchars
                    corr += frc[1] * target_freqs[d]

                if corr > max_corr:
                    m = j
                    max_corr = corr

            key += chr(m + ordA)

        r = (chr((c - ord(key[i % best_len]) + nchars) % nchars + ordA)
             for i, c in enumerate(cleaned))
        return (key, "".join(r))

        ##ejemplo: FVUZVCFAGFMRPVMWIMBLPDTOTMTNZICIOZADFTSPGEOMMXMSUMSNMRPYVPMSTQWLVAMWTGMIOBJEZETLJLADFMTPUETGTPMSDZJMQODWOQWRNMBEWDPTPBCENI
        ##OOWMBZEZYUFWBWWSKCETWSZIMZASBBSLXATTPDKAQQULVETGMZAPSQONQPFAEPTATXSZDIOKJLAQVMILJIBLFDLEMIJYLIBPBDBAFBJZXIBKJPVTPDFTVTJAJPBEQZPGQND
        ##QBDICBLBAZOWQONQATMHFVSVMTNZIUCSLGADIELXUFJMZKOONPCUEBAVWMNHCBLTOTRVOQOTBBXJIFVDZVFPZNPISVMTNZIUCSLGLFVHFI
#============================================================================
class Sustitucion:
    def analisis(texto):
        def tokenize(string):
            return re.findall(r'\w+', string.upper())
        def countNgrams(texto, min_length=2, max_length=3):
            lengths = range(min_length, max_length + 1)
            ngrams = {length: collections.Counter() for length in lengths}
            queue = collections.deque(maxlen=max_length)
            def add_queue():
                current = tuple(queue)
                for length in lengths:
                    if len(current) >= length:
                        ngrams[length][current[:length]] += 1
            for line in texto:
                for word in tokenize(line):
                    queue.append(word)
                    if len(queue) >= max_length:
                        add_queue()
            while len(queue) > min_length:
                queue.popleft()
                add_queue()
            return ngrams
        def mostFrequentNgrams(ngrams,num=5):
            digramas=''
            trigramas=''
            for gram, count in ngrams[2].most_common(num):
                x=''.join(gram)
                digramas=digramas+x+', '
            for gram, count in ngrams[3].most_common(num):
                x=''.join(gram)
                trigramas=trigramas+x+', '
            return(digramas,trigramas)
            
        def mostFrequentLetters(texto):
            ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
            LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            def getLetterCount(message):
                letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
                for letter in message.upper():
                    if letter in LETTERS:
                        letterCount[letter] += 1
                return letterCount
            def getItemAtIndexZero(x):
                return x[0]

            def getFrequencyOrder(message):
                letterToFreq = getLetterCount(message)
                freqToLetter = {}
                for letter in LETTERS:
                    if letterToFreq[letter] not in freqToLetter:
                        freqToLetter[letterToFreq[letter]] = [letter]
                    else:
                        freqToLetter[letterToFreq[letter]].append(letter)
                for freq in freqToLetter:
                    freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
                    freqToLetter[freq] = ''.join(freqToLetter[freq])
                freqPairs = list(freqToLetter.items())
                freqPairs.sort(key=getItemAtIndexZero, reverse=True)
                freqOrder = []
                for freqPair in freqPairs:
                    freqOrder.append(freqPair[1])
                return ''.join(freqOrder)
            nuevoAlf=getFrequencyOrder(texto)
            return nuevoAlf
        
        masFrec=mostFrequentLetters(texto)    
        ngrams = countNgrams(texto)
        (di,tri)=mostFrequentNgrams(ngrams)
        return(masFrec,di,tri)   
    
        ##EJEMPLO: GYQSSZITHKGWSTDLVIOEIIQCTWTTFLXWDOZZTRZGDNYKOTFRDKLITKSGEAIGSDTLYGKLGSXZOGFRXKOFUZITNTQKLGYGXKOFZODQENZITKTVTKTGFSNZVGVIOEIOVQLZITDTQFLGYOFZKGRXEOFUZGIOLFGZOETZIQZGYDKIQZITKSTNLZIXDWQFRZIQZGYEGSGFTSVQKWXKZGFLDQRFTLLGYZITLTZITSQZZTKDQNIQCTQYYGKRTRQYOFTKYOTSRYGKQFQEXZTQFRGKOUOFQSGWLTKCTKWXZZITGZITKVQLLGLZKQFUTOFOZLOFETHZOGFQFRLGRKQDQZOEOFOZLRTZQOSLZIQZOZDQNWTZITDGKTVGKZINGYWTOFUHSQETRXHGFKTEGKRTCTFOYOZUQCTDNYKOTFRYTVTKGHTFOFULYGKZIGLTRTRXEZOCTDTZIGRLGYKTQLGFOFUWNVIOEIITQEIOTCTRLXEIKTDQKAQWSTKTLXSZLZITLZGKNIQLOWTSOTCTWTTFZGSRDGKTZIQFGFETOFZITFTVLHQHTKLWXZSOATQSSLXEIFQKKQZOCTLOZLTYYTEZOLDXEISTLLLZKOAOFUVITFLTZYGKZITFWSGEOFQLOFUSTIQSYEGSXDFGYHKOFZZIQFVITFZITYQEZLLSGVSNTCGSCTWTYGKTNGXKGVFTNTLQFRZITDNLZTKNESTQKLUKQRXQSSNQVQNQLTQEIFTVROLEGCTKNYXKFOLITLQLZTHVIOEISTQRLGFZGZITEGDHSTZTZKXZIQZZITZODTZITEOKEXDLZQFETLDQRTQRTTHODHKTLLOGFXHGFDTQFRZITSQHLTGYZVGNTQKLIQLIQKRSNLTKCTRZGVTQATFZITTYYTEZ
        ##CLAVE: QWERTYUIOPASDFGHJKLZXCVBNM
    def descifrar(texto,clave):

        letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        descifrado=''

        charsA=clave
        charsB=letras

        for simbolo in texto:
            if simbolo.upper() in charsA:
                simIndex = charsA.find(simbolo.upper())
                if simbolo.isupper():
                    descifrado+=charsB[simIndex].upper()
        return descifrado
    
    def clave(texto):
        etaoin='ETAOINSHRDLUCMFWGYPBVKXJQZ'
        (masFrec,b,c) = Sustitucion.analisis(texto)

        descifrado=''

        for i in range(65,91):     
            descifrado+=masFrec[etaoin.find(chr(i))]
        return descifrado

#============================================================================

class HillTexto:
    def gcd(a,b): #Euclid algorithm,return greatest common divisor od 2 positive integers
        while b:
            a, b= b, a%b
        return a
        
    def modInverse(a, m) :
        if(HillTexto.gcd(a,m) != 1) or ((m == 1)): 
            return 0
        m0 = m 
        y = 0
        x = 1
        while (a > 1) : 
        # q is quotient 
            q = a // m 
            t = m 
        #m is remainder , now process the same as Euclid's algorithm
            m = a % m 
            a = t 
            t = y 
        # update x and y 
            y = x - q * y 
            x = t 
    #to make x positive 
        if (x < 0) : 
            x = x + m0 
        return x
            
    def multiplicarVector(parcial,matriz,n):
        parcialCifrado=''
        vector=numpy.zeros((n,1))
        for i in range(n):
            vector[i][0]=ord(parcial[i])-65
        multiplicacion=numpy.dot(matriz,vector)
        for i in range(n):
            letra=chr(int((multiplicacion[i][0])%26)+65)
            parcialCifrado+=''.join(letra)
        return parcialCifrado
        
    def cifrar(texto,clave):
        n=int(math.sqrt(len(clave)))
        matriz=numpy.zeros(shape=(n,n))
        k=0
        for i in range(n):
            for j in range(n):
                matriz[i][j]=(ord(clave[k])-65)%26
                k+=1
        cifrado=''
        numbloques=math.ceil(len(texto)/n)
        if(numbloques*n != len(texto)):
            ad=(numbloques*n)%len(texto)
            for i in range(ad):
                texto+=''.join('A')
        for i in range(numbloques):
            ci=HillTexto.multiplicarVector(texto[i*n:(i+1)*n],matriz,n)
            cifrado+=''.join(ci)
        return cifrado

    def descifrar(texto,clave):
        n=int(math.sqrt(len(clave)))
        matriz=numpy.zeros(shape=(n,n))
        k=0
        for i in range(n):
            for j in range(n):
                matriz[i][j]=(ord(clave[k])-65)%26
                k+=1
        matriz=HillTexto.invertirMatriz(matriz)
        descifrado=''
        numbloques=math.ceil(len(texto)/n)
        if(numbloques*n != len(texto)):
            ad=(numbloques*n)%len(texto)
            for i in range(ad):
                texto+=''.join('A')
        for i in range(numbloques):
            desci=HillTexto.multiplicarVector(texto[i*n:(i+1)*n],matriz,n)
            descifrado+=''.join(desci)
        return descifrado
        
    def minor(A,i,j):
        A = array(A)
        n = len(A)
        minor = zeros((n-1,n-1),dtype = int) #for problems in cryptography integers are used
        p = 0
        for s in range(0,n-1):
            if p == i:
                p = p+1
            q = 0
            for t in range(0,n-1):
                if q == j:
                    q = q+1
                minor[s][t] = A[p][q]
                q = q+1
            p = p+1
        return minor
    
    def invertirMatriz(A):
        m=26
        n = len(A)
        for i in range(0,n):
            for j in range(0,n):
                A[i][j] = (A[i][j] % m)
        d = int(round(det(A)) % m)
        adj = zeros((n,n),dtype = int)
        for i in range(n):
            for j in range(n):
                M = HillTexto.minor(A,i,j)
                adj[j][i] = int((round(det(M)) % m))
                if (i+1+j+1)%2 == 1:
                    adj[j][i] = (-1*adj[j][i]) % 26
        return ((HillTexto.modInverse(d,m)*adj) % m)
        
    def crearMatriz(n):
        matriz=numpy.zeros(shape=(n,n))
        for i in range(n):
            for j in range(n):
                matriz[i][j]=random.randint(0,25)
        return matriz
        
    ##clave con un tamaño de matriz dado    
    def clave(n):
        m=26
        clave=''
        inv=True
        matriz=HillTexto.crearMatriz(n)
        while inv:
            matriz=HillTexto.crearMatriz(n)
            d = int(round(det(matriz)) % m)
            gcd=HillTexto.gcd(d,m)
            if(gcd==1):
                inv=False
        for i in range(n):
            for j in range(n):
                clave+=chr(int(matriz[i][j]) + 65)                
        return clave
        
    ##clave con un tamaño de matriz no dado     
    def claveNoLong(longTexto):
        m=26
        n=math.ceil(math.sqrt(longTexto))
        clave=''
        inv=True
        matriz=HillTexto.crearMatriz(n)
        while inv:
            matriz=HillTexto.crearMatriz(n)
            d = int(round(det(matriz)) % m)
            gcd=HillTexto.gcd(d,m)
            if(gcd==1):
                inv=False
                
        for i in range(n):
            for j in range(n):
                clave+=chr(int(matriz[i][j]) + 65)
        return clave



#============================================================================
class HillImage:
    def cifrar(file):

        img = imageio.imread(file, pilmode="RGB")
        l = img.shape[0]
        w = img.shape[1]
        n = max(l,w)

        if n%2:
            n = n + 1
        img2 = numpy.zeros((n,n,3))
        img2[:l,:w,:] += img 
        Mod = 256
        k = 23 

        d = numpy.random.randint(256, size = (int(n/2),int(n/2)))         
        I = numpy.identity(int(n/2))                                     
        a = numpy.mod(-d,Mod)                                             
        b = numpy.mod((k * numpy.mod(I - a,Mod)),Mod)                     
        k = numpy.mod(numpy.power(k,127),Mod)                        
        c = numpy.mod((I + a),Mod)                                        
        c = numpy.mod(c * k, Mod)

        A1 = numpy.concatenate((a,b), axis = 1)
        A2 = numpy.concatenate((c,d), axis = 1)
        A = numpy.concatenate((A1,A2), axis = 0)
        Test = numpy.mod(numpy.matmul(numpy.mod(A,Mod),numpy.mod(A,Mod)),Mod)

        key = numpy.zeros((n + 1, n))
        key[:n, :n] += A

        key[-1][0] = int(l / Mod)
        key[-1][1] = l % Mod
        key[-1][2] = int(w / Mod)
        key[-1][3] = w % Mod
        key=key.astype(numpy.uint8)
        imageio.imwrite("Prueba/Key.png", key)

        Enc1 = (numpy.matmul(A % Mod,img2[:,:,0] % Mod)) % Mod
        Enc2 = (numpy.matmul(A % Mod,img2[:,:,1] % Mod)) % Mod
        Enc3 = (numpy.matmul(A % Mod,img2[:,:,2] % Mod)) % Mod

        Enc1 = Enc1.astype(numpy.uint8)
        Enc2 = Enc2.astype(numpy.uint8)
        Enc3 = Enc3.astype(numpy.uint8)

        Enc1 = numpy.expand_dims(Enc1, axis=2)
        Enc2 = numpy.expand_dims(Enc2, axis=2)
        Enc3 = numpy.expand_dims(Enc3, axis=2)

        Enc = numpy.concatenate((Enc1,Enc2,Enc3), axis = 2)              
        imageio.imwrite('Prueba/Encrypted.png',Enc)
    
    def descifrar(imagen,clave):
        Mod = 256
        Enc = imageio.imread(imagen) 

        A = imageio.imread(clave)
        l = A[-1][0] * Mod + A[-1][1]
        w = A[-1][2] * Mod + A[-1][3]
        A = A[0:-1]
    
        Dec1 = (numpy.matmul(A % Mod,Enc[:,:,0] % Mod)) % Mod
        Dec2 = (numpy.matmul(A % Mod,Enc[:,:,1] % Mod)) % Mod
        Dec3 = (numpy.matmul(A % Mod,Enc[:,:,2] % Mod)) % Mod


        Dec1 = Dec1.astype(numpy.uint8)
        Dec2 = Dec2.astype(numpy.uint8)
        Dec3 = Dec3.astype(numpy.uint8)

    # Agregar una dimensión a cada matriz
        Dec1 = numpy.expand_dims(Dec1, axis=2)
        Dec2 = numpy.expand_dims(Dec2, axis=2)
        Dec3 = numpy.expand_dims(Dec3, axis=2)
        Dec = numpy.concatenate((Dec1,Dec2,Dec3), axis = 2)               


        Final = Dec[:l,:w,:]

        imageio.imwrite('Prueba/Decrypted.png',Final)

