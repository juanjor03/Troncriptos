import random,math,collections,re

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
#============================================================================
#============================================================================
#============================================================================
#============================================================================
#============================================================================
