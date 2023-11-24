from re import A
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
from PIL import ImageOps
from secrets import token_bytes
import random

#===========================================================================
#============================================================================
#============================================================================
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
		encryptedImg.save("src/Prueba/AesEncrypted.png")

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
		decryptedImg.save("src/Prueba/AesDecrypted.png")


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
		encryptedImg.save("src/Prueba/AesEncrypted.png")
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
		decryptedImg.save("src/Prueba/AesDecrypted.png")

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
		encryptedImg.save("src/Prueba/AesEncrypted.png")

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
		decryptedImg.save("src/Prueba/AesDecrypted.png")

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
		encryptedImg.save("src/Prueba/AesEncrypted.png")

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
		decryptedImg.save("src/Prueba/AesDecrypted.png")
	
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


##clave de 32 caracteres |"src/Prueba/AesEncrypted.png" | "src/Prueba/AesDecrypted.png"
##iv es un string de tamaño 16 hexadecimal que se trabaja como bytes, ivCTR es un string de tamaño 8 hexadecimal que se trabaja como bytes

##iv_str = "0123456789ABCDEF"  # IV como string hexadecimal
##iv_bytes = bytes.fromhex(iv_str)  # Convierte el string hexadecimal a bytes