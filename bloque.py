from re import A
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
from PIL import Image
from PIL import ImageOps
from secrets import token_bytes
import random
import sys


#===========================================================================
class BloqueSDES:
	p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
	p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
	p4_table = [2, 4, 3, 1]
	IP = [2, 6, 3, 1, 4, 8, 5, 7]
	IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
	expansion = [4, 1, 2, 3, 2, 3, 4, 1]
	s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
	s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

	def cifrar(message,clave):
		key1,key2=BloqueSDES.clave(clave)
		temp = BloqueSDES.apply_table(message, BloqueSDES.IP)
		temp = BloqueSDES.function(BloqueSDES.expansion, BloqueSDES.s0, BloqueSDES.s1, key1, temp)
		temp = temp[4:] + temp[:4]
		temp = BloqueSDES.function(BloqueSDES.expansion, BloqueSDES.s0, BloqueSDES.s1, key2, temp)
		CT = BloqueSDES.apply_table(temp, BloqueSDES.IP_inv)
		return(CT)
	def descifrar(CT,clave):
		key1,key2=BloqueSDES.clave(clave)
		temp = BloqueSDES.apply_table(CT, BloqueSDES.IP)
		temp = BloqueSDES.function(BloqueSDES.expansion, BloqueSDES.s0, BloqueSDES.s1, key2, temp)
		temp = temp[4:] + temp[:4]
		temp = BloqueSDES.function(BloqueSDES.expansion, BloqueSDES.s0, BloqueSDES.s1, key1, temp)
		PT = BloqueSDES.apply_table(temp, BloqueSDES.IP_inv)
		return(PT)
	def key():
		caracteresValidos=['1','0']
		k=''.join(random.choice(caracteresValidos) for _ in range(10))
		return(k)

	def clave(key):
		temp = BloqueSDES.apply_table(key, BloqueSDES.p10_table)
		left = temp[:5]
		right = temp[5:]
		left = BloqueSDES.left_shift(left)
		right = BloqueSDES.left_shift(right)
		key1 = BloqueSDES.apply_table(left + right, BloqueSDES.p8_table)
		left = BloqueSDES.left_shift(left)
		right = BloqueSDES.left_shift(right)
		left = BloqueSDES.left_shift(left)
		right = BloqueSDES.left_shift(right)
		key2 = BloqueSDES.apply_table(left + right, BloqueSDES.p8_table)
		return(key1,key2)
	def apply_table(inp, table):
		res = ""
		for i in table:
			res += inp[i - 1]
		return res
	def left_shift(data):
		return data[1:] + data[0]
	def xor(a, b):
		res = ""
		for i in range(len(a)):
			if a[i] == b[i]:
				res += "0"
			else:
				res += "1"
		return res
	def apply_sbox(s, data):
		row = int("0b" + data[0] + data[-1], 2)
		col = int("0b" + data[1:3], 2)
		return bin(s[row][col])[2:]
	def function(expansion, s0, s1, key, message):
		left = message[:4]
		right = message[4:]
		temp = BloqueSDES.apply_table(right, expansion)
		temp = BloqueSDES.xor(temp, key)
		l = BloqueSDES.apply_sbox(s0, temp[:4])  # noqa: E741
		r = BloqueSDES.apply_sbox(s1, temp[4:])
		l = "0" * (2 - len(l)) + l  # noqa: E741
		r = "0" * (2 - len(r)) + r
		temp = BloqueSDES.apply_table(l + r, BloqueSDES.p4_table)
		temp = BloqueSDES.xor(left, temp)
		return temp + right
#===========================================================================
class BloqueDES:
	def verificar_texto(texto):
		return texto + (8 - len(texto) % 8) * b'\0'
	
	def cifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_ECB)
		padded_plaintext = BloqueDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_ECB)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')
	
	def cifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_CBC,iv)
		padded_plaintext = BloqueDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_CBC,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_OFB,iv)
		padded_plaintext = BloqueDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')
	def descifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_OFB,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarCTR(clave,texto,iv):
		nonce = iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_CTR,nonce=nonce)
		padded_plaintext = BloqueDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')		
	def descifrarCTR(clave,texto,iv):
		nonce=iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(8, b'\0')[:8]
		cipher = DES.new(clave, DES.MODE_CTR,nonce=nonce)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def clave():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		clave = ''.join(random.choice(caracteresValidos) for _ in range(8))
		return(clave)
	
	def claveIv():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(8))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(8))
		return(clave,iv)
	def claveCTR():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(4))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(8))
		return(clave,iv)

#============================================================================
class BloqueTDES:
	def verificar_texto(texto):
		return texto + (8 - len(texto) % 8) * b'\0'
	
	def cifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_ECB)
		padded_plaintext = BloqueTDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_ECB)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')
	
	def cifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_CBC,iv)
		padded_plaintext = BloqueTDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_CBC,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_OFB,iv)
		padded_plaintext = BloqueTDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')
	def descifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(8, b'\0')[:8]
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_OFB,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarCTR(clave,texto,iv):
		nonce = iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_CTR,nonce=nonce)
		padded_plaintext = BloqueTDES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')		
	def descifrarCTR(clave,texto,iv):
		nonce=iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(24, b'\0')[:24]
		cipher = DES3.new(clave, DES3.MODE_CTR,nonce=nonce)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def clave():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		clave = ''.join(random.choice(caracteresValidos) for _ in range(24))
		return(clave)
	
	def claveIv():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(8))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(24))
		return(clave,iv)
	def claveCTR():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(4))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(24))
		return(clave,iv)
#============================================================================

class BloqueAES:
	def verificar_texto(texto):
		return texto + (8 - len(texto) % 8) * b'\0'
	
	def cifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_ECB)
		padded_plaintext = BloqueAES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarECB(clave, texto):
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_ECB)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')
	
	def cifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(16, b'\0')[:16]
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_CBC,iv)
		padded_plaintext = BloqueAES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')	
	def descifrarCBC(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(16, b'\0')[:16]
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_CBC,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(16, b'\0')[:16]
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_OFB,iv)
		padded_plaintext = BloqueAES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')
	def descifrarOFB(clave,texto,iv):
		iv=iv.encode('utf-8')
		iv = iv.ljust(16, b'\0')[:16]
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_OFB,iv)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def cifrarCTR(clave,texto,iv):
		nonce = iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_CTR,nonce=nonce)
		padded_plaintext = BloqueAES.verificar_texto(texto.encode('utf-8'))
		ciphertext = cipher.encrypt(padded_plaintext)
		return b64encode(ciphertext).decode('utf-8')		
	def descifrarCTR(clave,texto,iv):
		nonce=iv.encode('utf-8')
		clave=clave.encode('utf-8')
		clave = clave.ljust(32, b'\0')[:32]
		cipher = AES.new(clave, AES.MODE_CTR,nonce=nonce)
		decrypted_text = cipher.decrypt(b64decode(texto.encode('utf-8')))
		return decrypted_text.rstrip(b'\0').decode('utf-8')

	def clave():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave)
	
	def claveIv():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(16))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave,iv)
	def claveCTR():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(4))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave,iv)
#============================================================================

class AesImage:

	def DecimalToHex(l):
		result = ""
		for i in l:
			if len(hex(i).split('x')[-1]) != 1:
				result += hex(i).split('x')[-1]
			else:
				result += '0' + hex(i).split('x')[-1]
		return result.upper()
	
	def HexToDecimal(s):
		result = []
		while len(s) != 32:
			s = '0' + s
		for i in range(0, 32, 8):
			pixel = []
			for j in range(i, i+8, 2):
				pixel.append(int(s[j]+s[j+1], base=16))
			result.append(tuple(pixel))
		return result
	
	def cifrarECB(file,key):
		cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
		img = Image.open(file)
		encryptedImg = img.convert("RGBA")
		if encryptedImg.width % 4 != 0:
			diff = 4 - (encryptedImg.width % 4)
			encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
		for y in range(0, encryptedImg.height):
			rowPixels = []
			for x in range(0, encryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.encrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += encryptedImg.getpixel((x,y))
		encryptedImg.save("Prueba/AesEncrypted.png")

	def descifrarECB(file,key):
		cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
		img = Image.open(file)
		decryptedImg = img
		for y in range(0, decryptedImg.height):
			rowPixels = []
			for x in range(0, decryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.decrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += decryptedImg.getpixel((x,y))
		decryptedImg.save("Prueba/AesDecrypted.png")


	def cifrarCBC(file,key,iv):
		cipher = AES.new(key, AES.MODE_CBC, iv)
		img = Image.open(file)
		encryptedImg = img.convert("RGBA")
		if encryptedImg.width % 4 != 0:
			diff = 4 - (encryptedImg.width % 4)
			encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
		for y in range(0, encryptedImg.height):
			rowPixels = []
			for x in range(0, encryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.encrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += encryptedImg.getpixel((x,y))
		encryptedImg.save("Prueba/AesEncrypted.png")
	def descifrarCBC(file,key,iv):
		cipher = AES.new(key, AES.MODE_CBC, iv)
		img = Image.open(file)
		decryptedImg = img
		for y in range(0, decryptedImg.height):
			rowPixels = []
			for x in range(0, decryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.decrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += decryptedImg.getpixel((x,y))
		decryptedImg.save("Prueba/AesDecrypted.png")

	def cifrarOFB(file,key,iv):
		cipher = AES.new(key, AES.MODE_OFB, iv)
		img = Image.open(file)
		encryptedImg = img.convert("RGBA")
		if encryptedImg.width % 4 != 0:
			diff = 4 - (encryptedImg.width % 4)
			encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
		for y in range(0, encryptedImg.height):
			rowPixels = []
			for x in range(0, encryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.encrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += encryptedImg.getpixel((x,y))
		encryptedImg.save("Prueba/AesEncrypted.png")

	def descifrarOFB(file,key,iv):
		cipher = AES.new(key, AES.MODE_OFB, iv)
		img = Image.open(file)
		decryptedImg = img
		for y in range(0, decryptedImg.height):
			rowPixels = []
			for x in range(0, decryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.decrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += decryptedImg.getpixel((x,y))
		decryptedImg.save("Prueba/AesDecrypted.png")

	def cifrarCTR(file,key,ivCTR):
		cipher = AES.new(key,AES.MODE_CTR,nonce=ivCTR[:16//2])
		img = Image.open(file)
		encryptedImg = img.convert("RGBA")
		if encryptedImg.width % 4 != 0:
			diff=4-(encryptedImg.width %4)
			encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
		for y in range(0, encryptedImg.height):
			rowPixels = []
			for x in range(0, encryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.encrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += encryptedImg.getpixel((x,y))
		encryptedImg.save("Prueba/AesEncrypted.png")

	def descifrarCTR(file,key,ivCTR):
		cipher = AES.new(key,AES.MODE_CTR,nonce=ivCTR[:16//2])
		img = Image.open(file)
		decryptedImg = img
		for y in range(0, decryptedImg.height):
			rowPixels = []
			for x in range(0, decryptedImg.width):
				if x % 4 == 0 and x > 0:
					newRowPixels = cipher.encrypt(bytes(rowPixels))
					newRowPixels = AesImage.HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
					for i in range(x - 4, x):
						decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
					rowPixels = []
				rowPixels += decryptedImg.getpixel((x,y))
		decryptedImg.save("Prueba/AesDecrypted.png")
	
	def GenerarClave():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave.encode('utf-8')) #retorna clave aleatoria de 16 bytes de tipo bytes

	def GenerarClaveIv():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(16))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave.encode('utf-8'),iv.encode('utf-8')) #retorna clave e iv aleatoria de 16 bytes de tipo bytes
	
	def GenerarClaveCtr():
		caracteresValidos = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
		iv=''.join(random.choice(caracteresValidos) for _ in range(8))
		clave = ''.join(random.choice(caracteresValidos) for _ in range(32))
		return(clave.encode('utf-8'),iv.encode('utf-8')) #retorna clave e iv aleatoria de 8 bytes de tipo bytes


##iv es un string de tamaño 16 hexadecimal que se trabaja como bytes, ivCTR es un string de tamaño 8 hexadecimal que se trabaja como bytes