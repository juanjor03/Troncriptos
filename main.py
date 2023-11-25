from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
import cv2
import imutils
import sys,math
import pyperclip as clipboard
import clasico,bloque,clavePublica,firmaDigital
from Cryptodome.PublicKey import RSA
from Cryptodome.PublicKey import DSA

class MainGui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("troncriptos.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_2.clicked.connect(lambda: MainApp.exit())
        self.pushButton.clicked.connect(lambda: self.showMinimized())
        self.frame_2.mouseMoveEvent = self.MoveWindow

        self.stackedWidget.setCurrentWidget(self.inicio)
##SIDE BAR===============================================================================================================
        self.toolButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.inicio))
        self.toolButton_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clasico))
        self.toolButton_3.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.bloque))
        self.toolButton_5.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clave))
        self.toolButton_6.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.firma))
        self.toolButton_7.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.ayuda))
##=======================================================================================================================
##INICIO=================================================================================================================
        self.toolButton_8.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clasico))
        self.toolButton_9.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.bloque))
        self.toolButton_10.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clave))
        self.toolButton_11.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.firma))
##=======================================================================================================================
##CLASICO================================================================================================================
        self.toolButton_12.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clDesplazamiento))
        self.toolButton_13.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clVigenere))
        self.toolButton_14.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clPermutacion))
        self.toolButton_15.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clTransposicion))
        self.toolButton_16.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clSustitucion))
        self.toolButton_17.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clAfin))
        self.toolButton_18.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clHill))
        self.toolButton_29.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clHillImage))
        self.toolButton_30.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clHill))
##=======================================================================================================================
##BLOQUE=================================================================================================================
        self.toolButton_19.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blSdes))
        self.toolButton_20.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blTdes))
        self.toolButton_21.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blDes))
        self.toolButton_22.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blAes))
        self.toolButton_31.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blAesImage))
        self.toolButton_32.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.blAes))
##=======================================================================================================================
##CLAVE PUBLICA==========================================================================================================
        self.toolButton_23.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clGamal))
        self.toolButton_24.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clRsa))
        self.toolButton_25.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clRabin))
##=======================================================================================================================
##FIRMA DIGITAL==========================================================================================================
        self.toolButton_26.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.fiRsa))
        self.toolButton_27.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.fiDsa))
        self.toolButton_28.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.fiGamal))
##=======================================================================================================================
##Ocultar SIDEBAR========================================================================================================
        self.toolButton_4.clicked.connect(lambda: self.Side_Menu_Def_0())
        self.frame_5.mousePressEvent = self.Side_Menu_Def_1
        self.clasico.mousePressEvent = self.Side_Menu_Def_1
        self.bloque.mousePressEvent = self.Side_Menu_Def_1
        self.clave.mousePressEvent = self.Side_Menu_Def_1
        self.firma.mousePressEvent = self.Side_Menu_Def_1
        self.ayuda.mousePressEvent = self.Side_Menu_Def_1

        self.clDesplazamiento.mousePressEvent = self.Side_Menu_Def_1
        self.clVigenere.mousePressEvent = self.Side_Menu_Def_1
        self.clPermutacion.mousePressEvent = self.Side_Menu_Def_1
        self.clTransposicion.mousePressEvent = self.Side_Menu_Def_1
        self.clSustitucion.mousePressEvent = self.Side_Menu_Def_1
        self.clAfin.mousePressEvent = self.Side_Menu_Def_1
        self.clHill.mousePressEvent = self.Side_Menu_Def_1
        self.clHillImage.mousePressEvent = self.Side_Menu_Def_1
        self.blSdes.mousePressEvent = self.Side_Menu_Def_1
        self.blTdes.mousePressEvent = self.Side_Menu_Def_1
        self.blDes.mousePressEvent = self.Side_Menu_Def_1
        self.blAes.mousePressEvent = self.Side_Menu_Def_1
        self.blAesImage.mousePressEvent = self.Side_Menu_Def_1
        self.clRsa.mousePressEvent = self.Side_Menu_Def_1
        self.clRabin.mousePressEvent = self.Side_Menu_Def_1
        self.clGamal.mousePressEvent = self.Side_Menu_Def_1
        self.fiRsa.mousePressEvent = self.Side_Menu_Def_1
        self.fiDsa.mousePressEvent = self.Side_Menu_Def_1
        self.fiGamal.mousePressEvent = self.Side_Menu_Def_1

        self.pushButton_4.mousePressEvent = self.Side_Menu_Def_1
        self.pushButton_5.mousePressEvent = self.Side_Menu_Def_1
        self.pushButton_6.mousePressEvent = self.Side_Menu_Def_1
        self.pushButton_7.mousePressEvent = self.Side_Menu_Def_1

##==========================================Conectar botones===========================================================
##Desplazamiento========================================================================================================
        self.despCifrar.clicked.connect(self.desplazamientoCifrar)
        self.despDescifrar.clicked.connect(self.desplazamientoDescifrar)
        self.despGenerar.clicked.connect(self.desplazamientoGenerarClave)
        self.despCopiar.clicked.connect(self.vigenereCopiar)
##Vigenere========================================================================================================
        self.vigDescifrar.clicked.connect(self.analisisVigenere)
        self.vigCopiar.clicked.connect(self.vigenereCopiar)
##Permutacion(VERNAM)========================================================================================================
        self.permCifrar.clicked.connect(self.vernamCifrar)
        self.permDescifrar.clicked.connect(self.vernamDescifrar)
        self.permGenerar.clicked.connect(self.vernamGenerarClave)
        self.permCopiar.clicked.connect(self.permutacionCopiar)
##Transposicion========================================================================================================
        self.transCifrar.clicked.connect(self.transposicionCifrar)
        self.transDescifrar.clicked.connect(self.transposicionDescifrar)
        self.transGenerar.clicked.connect(self.transposicionGenerarClave)
        self.transCopiar.clicked.connect(self.transposicionCopiar)
##Sustitucion========================================================================================================
        self.susAnalizar.clicked.connect(self.sustitucionAnalisis)
        self.susDescifrar.clicked.connect(self.sustitucionDescifrar)
        self.susCopiar.clicked.connect(self.sustitucionCopiar)
##Afin========================================================================================================
        self.afinCifrar.clicked.connect(self.afCifrar)
        self.afinDescifrar.clicked.connect(self.afDescifrar)
        self.afinGenerar.clicked.connect(self.afGenerarClave)
        self.afinCopiar.clicked.connect(self.afinBCopiar)
##Hill========================================================================================================
        self.hilCifrar.clicked.connect(self.hilTextoCifrar)
        self.hilDescifrar.clicked.connect(self.hilTextoDescifrar)
        self.hilGenerar.clicked.connect(self.hilTextoGenerarClave)
        self.hilCopiar.clicked.connect(self.hillTextoCopiar)
##HillImage========================================================================================================
        self.hilImageCifrar.clicked.connect(self.hilImgCifrar)
        self.hilImageDescifrar.clicked.connect(self.hilImgDescifrar)
##Sdes========================================================================================================
        self.sdesCifrar.clicked.connect(self.sdesBCifrar)
        self.sdesDescifrar.clicked.connect(self.sdesBDescifrar)
        self.sdesGenerar.clicked.connect(self.sdesBGenerarClave)
        self.sdesCopiar.clicked.connect(self.sDesTextoCopiar)
##Tdes======================================================================================================== 
        self.tdesCifrar.clicked.connect(self.tdesBCifrar)
        self.tdesDescifrar.clicked.connect(self.tdesBDescifrar)
        self.tdesGenerar.clicked.connect(self.tdesBGenerarClave) 
        self.tdesCopiar.clicked.connect(self.tDesCopiar)    
##Des======================================================================================================== 
        self.desCifrar.clicked.connect(self.desBCifrar)
        self.desDescifrar.clicked.connect(self.desBDescifrar)
        self.desGenerar.clicked.connect(self.desBGenerarClave)
        self.desCopiar.clicked.connect(self.desBCopiar)
##Aes========================================================================================================
        self.aesCifrar.clicked.connect(self.aesBCifrar)
        self.aesDescifrar.clicked.connect(self.aesBDescifrar)
        self.aesGenerar.clicked.connect(self.aesBGenerarClave)
        self.aesCopiar.clicked.connect(self.aesTextoCopiar)
##AesImage========================================================================================================
        self.aesImageGenerar.clicked.connect(self.aesImageGenerarClave)
        self.aesImageDescifrar.clicked.connect(self.aesImgDescifrar)
        self.aesImageCifrar.clicked.connect(self.aesImgCifrar)
##Rsa========================================================================================================
        self.rsaCifrar.clicked.connect(self.rsaBCifrar)
        self.rsaDescifrar.clicked.connect(self.rsaBDescifrar)
        self.rsaGenerar.clicked.connect(self.rsaBGenerar)
        self.rsaCopiar.clicked.connect(self.rsaBCopiar)
##Rabin========================================================================================================
        self.rabCifrar.clicked.connect(self.rabinCifrar)
        self.rabDescifrar.clicked.connect(self.rabinDescifrar)
        self.rabGenerar.clicked.connect(self.rabinGenerar)
        self.rabCopiar.clicked.connect(self.rabinCopiar)
##Gamal========================================================================================================
        self.gamCifrar.clicked.connect(self.gamalCifrar)
        self.gamDescifrar.clicked.connect(self.gamalDescifrar)
        self.gamGenerar.clicked.connect(self.gamalGenerar)
        self.gamCopiar.clicked.connect(self.gamalCopiar)
##FirmaDigitalRsa========================================================================================================
        self.fiRsaCopiar.clicked.connect(self.firmaDigitalRsaCopiar)
##FirmaDigitalDsa========================================================================================================
        self.fiDsaCifrar.clicked.connect(self.dsaBFirmar)
        self.fiDsaDescifrar.clicked.connect(self.dsaBVerificar)
        self.fiDsaGenerar.clicked.connect(self.dsaBGenerarClave)
        self.fiDsaCopiar.clicked.connect(self.firmaDigitalDsaCopiar)
##FirmaDigitalGamal========================================================================================================
        self.fiGamCopiar.clicked.connect(self.firmaDigitalGamalCopiar)
##=======================================================================================================================        
##=====================================FUNCIONES DE BOTONES Y CAMPOS DE TEXTO============================================
##=======================================================================================================================

##Desplazamiento=========================================================================================================
    def desplazamientoCifrar(self):
        if(self.despTextoOriginal.toPlainText()!=""):
            if(self.cantDesplazamiento.text()!=""):
                self.despTextoResult.clear()
                textoDesp= clasico.Desplazamiento.cifrar(self.despTextoOriginal.toPlainText(),int(self.cantDesplazamiento.text()))
                self.despTextoResult.insertPlainText(textoDesp)
    def desplazamientoDescifrar(self):
        if(self.despTextoOriginal.toPlainText()!=""):
            if(self.cantDesplazamiento.text()!=""):
                self.despTextoResult.clear()
                textoDesp= clasico.Desplazamiento.descifrar(self.despTextoOriginal.toPlainText(),int(self.cantDesplazamiento.text()))
                self.despTextoResult.insertPlainText(textoDesp)
    def desplazamientoGenerarClave(self):
        self.cantDesplazamiento.clear()
        despl=clasico.Desplazamiento.clave()
        self.cantDesplazamiento.insert(str(despl))
    def desplazamientoCopiar(self):
        clipboard.copy(self.despTextoResult.toPlainText())

##=======================================================================================================================

##Vigenere=========================================================================================================
    def analisisVigenere(self):
        (clave,texto) = clasico.Vigenere.analisis(self.vigTextoOriginal.toPlainText())
        self.vigTextoResult.clear()
        self.vigClave.clear()
        self.vigTextoResult.insertPlainText(texto)
        self.vigClave.insert(clave)
    def vigenereCopiar(self):
        clipboard.copy(self.vigTextoResult.toPlainText())
##=======================================================================================================================

##Permutacion(VERNAM)=========================================================================================================
    def vernamCifrar(self):
        if(len(self.permTextoOriginal.toPlainText())==len(self.verClave.text())):
            textoVer=clasico.Vernam.cifrar(self.permTextoOriginal.toPlainText(),self.verClave.text())
            self.permTextoResult.clear()
            self.permTextoResult.insertPlainText(textoVer)
    def vernamDescifrar(self):
        if(len(self.permTextoOriginal.toPlainText())==len(self.verClave.text())):
            textoDescVer=clasico.Vernam.descifrar(self.permTextoOriginal.toPlainText(),self.verClave.text())
            self.permTextoResult.clear()
            self.permTextoResult.insertPlainText(textoDescVer)        
    def vernamGenerarClave(self):
        self.verClave.clear()
        clave=clasico.Vernam.clave(len(self.permTextoOriginal.toPlainText()))
        self.verClave.insert(str(clave))
    def permutacionCopiar(self):
        clipboard.copy(self.permTextoResult.toPlainText())
##=======================================================================================================================

##Transposicion=========================================================================================================
    def transposicionCifrar(self):
        if(self.transTextoOriginal.toPlainText()!=""):
            if(self.transClave.text()!=""):
                self.transTextoResult.clear()
                textoTrans= clasico.Transposicion.cifrar(self.transTextoOriginal.toPlainText(),self.transClave.text())
                self.transTextoResult.insertPlainText(textoTrans)    
    def transposicionDescifrar(self):
        if(self.transTextoOriginal.toPlainText()!=""):
            if(self.transClave.text()!=""):
                self.transTextoResult.clear()
                textoTrans= clasico.Transposicion.descifrar(self.transTextoOriginal.toPlainText(),self.transClave.text())
                self.transTextoResult.insertPlainText(textoTrans)    
    def transposicionGenerarClave(self):
        self.transClave.clear()
        clave=clasico.Transposicion.clave(len(self.transTextoOriginal.toPlainText()))
        self.transClave.insert(str(clave))
    def transposicionCopiar(self):
        clipboard.copy(self.transTextoResult.toPlainText())
##=======================================================================================================================

##Sustitucion=========================================================================================================
    def sustitucionAnalisis(self):
        (alfabeto,digramas,trigramas) = clasico.Sustitucion.analisis(str(self.susTextoOriginal.toPlainText()))
        self.letrasFrec.clear()
        self.digramas.clear()
        self.trigramas.clear()
        self.letrasFrec.insert(alfabeto)
        self.digramas.insert(digramas)
        self.trigramas.insert(trigramas)
    def sustitucionDescifrar(self):
        if self.susClave.text() == '':
            self.susClave.clear()
            clave=clasico.Sustitucion.clave(str(self.susTextoOriginal.toPlainText()))
            self.susClave.insert(str(clave))
        self.susTextoResult.clear()
        textoSus=clasico.Sustitucion.descifrar(self.susTextoOriginal.toPlainText(),self.susClave.text())
        self.susTextoResult.insertPlainText(textoSus)
    def sustitucionCopiar(self):
        clipboard.copy(self.susTextoResult.toPlainText())
##=======================================================================================================================

##Afin=========================================================================================================
    def maximo_comun_divisor(self,a,b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a
    def afCifrar(self):
        if(self.afinClave.text()!=""):
                clave=self.afinClave.text()
                claveLst=clave.split(sep=',')
                claveA=int(claveLst[0])
                claveB=int(claveLst[1])

                if(self.maximo_comun_divisor(claveA,26) == 1):
                    self.afinTextoResult.clear()
                    textoAfin= clasico.Afin.cifrar(self.afinTextoOriginal.toPlainText(),claveA,claveB)
                    self.afinTextoResult.insertPlainText(textoAfin) 
    def afDescifrar(self):
        if(self.afinClave.text()!=""):
                clave=self.afinClave.text()
                claveLst=clave.split(sep=',')
                claveA=int(claveLst[0])
                claveB=int(claveLst[1])

                if(self.maximo_comun_divisor(claveA,26) == 1):
                    self.afinTextoResult.clear()
                    textoAfin= clasico.Afin.descifrar(self.afinTextoOriginal.toPlainText(),claveA,claveB)
                    self.afinTextoResult.insertPlainText(textoAfin) 
    def afGenerarClave(self):
        self.afinClave.clear()
        (claveA,claveB)=clasico.Afin.clave()
        self.afinClave.insert(str(claveA)+','+str(claveB))
    def afinBCopiar(self):
        clipboard.copy(self.afinTextoResult.toPlainText())
##=======================================================================================================================

##HillTexto=========================================================================================================
    def hilTextoCifrar(self):
        if (self.hilTextoOriginal.toPlainText()!=''):
            if(self.hilClave.text()!=""):
                    clave=self.hilClave.text()
                    self.hilTextoResult.clear()
                    textoHil= clasico.HillTexto.cifrar(self.hilTextoOriginal.toPlainText(),clave)
                    self.hilTextoResult.insertPlainText(textoHil) 
    
    def hilTextoDescifrar(self):
        if(self.hilClave.text()!=""):
                clave=self.hilClave.text()
                self.hilTextoResult.clear()
                textoHil= clasico.HillTexto.descifrar(self.hilTextoOriginal.toPlainText(),clave)
                self.hilTextoResult.insertPlainText(textoHil) 

    def hilTextoGenerarClave(self):
        if(self.tamMatriz.text() ==''):
            clave=clasico.HillTexto.claveNoLong(int(len(self.hilTextoOriginal.toPlainText())))
            self.hilClave.clear()
            self.hilClave.insert(clave) 
        else:
            clave=clasico.HillTexto.clave(int(self.tamMatriz.text()))
            self.hilClave.clear()
            self.hilClave.insert(clave)
    def hillTextoCopiar(self):
        clipboard.copy(self.hilTextoResult.toPlainText())
##=======================================================================================================================

##HillImagen=========================================================================================================

    def hilCargarImagen(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        return(self.filename)
    def hilCargarImagen2(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto2(self.image)
    def hilCargarImagen3(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        return(self.filename)
    def setPhoto(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto2(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_2.setPixmap(QtGui.QPixmap.fromImage(image))


    def hilImgCifrar(self):
        path=self.hilCargarImagen()
        clasico.HillImage.cifrar(path)   
        self.hilCargarImagen2('Prueba/Encrypted.png') 

    def hilImgDescifrar(self):
        path=self.hilCargarImagen()
        clave=self.hilCargarImagen3()
        clasico.HillImage.descifrar(path,clave)
        self.hilCargarImagen2('Prueba/Decrypted.png')


##=======================================================================================================================

##Sdes=========================================================================================================
    def sdesBCifrar(self):
        if(self.sdesTextoOriginal.toPlainText()!=''):
            mensaje=self.sdesTextoOriginal.toPlainText()
            if(self.sdesClave.text()!=''):
                clave=self.sdesClave.text()
                cifrado=bloque.BloqueSDES.cifrar(mensaje,clave)
                self.sdesTextoResult.clear()
                self.sdesTextoResult.insertPlainText(cifrado)
    def sdesBDescifrar(self):
        if(self.sdesTextoOriginal.toPlainText()!=''):
            mensaje=self.sdesTextoOriginal.toPlainText()
            if(self.sdesClave.text()!=''):
                clave=self.sdesClave.text()
                descifrado=bloque.BloqueSDES.descifrar(mensaje,clave)
                self.sdesTextoResult.clear()
                self.sdesTextoResult.insertPlainText(descifrado)
    def sdesBGenerarClave(self):
        self.sdesClave.clear()
        clave=bloque.BloqueSDES.key()
        self.sdesClave.insert(clave)

    def sDesTextoCopiar(self):
        clipboard.copy(self.sdesTextoResult.toPlainText())
##=======================================================================================================================

##Tdes=========================================================================================================
    def tdesBCifrar(self):
        if (self.tdesTextoOriginal.toPlainText()!=''):
            texto=self.tdesTextoOriginal.toPlainText()
            if(self.claveTDes.text()!=""):
               modo=self.tdesModo.currentText()
               clave=self.claveTDes.text()
               self.tdesTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.cifrarCBC(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveTDes.text()
                    cifrado=bloque.BloqueTDES.cifrarECB(clave,texto)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.cifrarOFB(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.cifrarCTR(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
    def tdesBDescifrar(self):
        if (self.tdesTextoOriginal.toPlainText()!=''):
            texto=self.tdesTextoOriginal.toPlainText()
            if(self.claveTDes.text()!=""):
               modo=self.tdesModo.currentText()
               clave=self.claveTDes.text()
               self.tdesTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.descifrarCBC(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveTDes.text()
                    cifrado=bloque.BloqueTDES.descifrarECB(clave,texto)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.descifrarOFB(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveTDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueTDES.descifrarCTR(clave,texto,iv)
                    self.tdesTextoResult.insertPlainText(cifrado)
    def tdesBGenerarClave(self):
        self.claveTDes.clear()
        modo=modo=self.tdesModo.currentText()
        if(modo=='CBC'):
            clave,iv=bloque.BloqueTDES.claveIv()
            self.claveTDes.insert(clave+','+iv)
        elif(modo=='ECB'):
            clave=bloque.BloqueTDES.clave()
            self.claveTDes.insert(clave)
        elif(modo=='OFB'):
            clave,iv=bloque.BloqueTDES.claveIv()
            self.claveTDes.insert(clave+','+iv)
        elif(modo=='CTR'):
            clave,iv=bloque.BloqueTDES.claveCTR()
            self.claveTDes.insert(clave+','+iv)
    def tDesCopiar(self):
        clipboard.copy(self.tdesTextoResult.toPlainText())
##=======================================================================================================================

##Des=========================================================================================================
    def desBCifrar(self):
        if (self.desTextoOriginal.toPlainText()!=''):
            texto=self.desTextoOriginal.toPlainText()
            if(self.claveDes.text()!=""):
               modo=self.desModo.currentText()
               clave=self.claveDes.text()
               self.desTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.cifrarCBC(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveDes.text()
                    cifrado=bloque.BloqueDES.cifrarECB(clave,texto)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.cifrarOFB(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.cifrarCTR(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
    def desBDescifrar(self):
        if (self.desTextoOriginal.toPlainText()!=''):
            texto=self.desTextoOriginal.toPlainText()
            if(self.claveDes.text()!=""):
               modo=self.desModo.currentText()
               clave=self.claveDes.text()
               self.desTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.descifrarCBC(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveDes.text()
                    cifrado=bloque.BloqueDES.descifrarECB(clave,texto)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.descifrarOFB(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveDes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueDES.descifrarCTR(clave,texto,iv)
                    self.desTextoResult.insertPlainText(cifrado)
    def desBGenerarClave(self):
        self.claveDes.clear()
        modo=modo=self.desModo.currentText()
        if(modo=='CBC'):
            clave,iv=bloque.BloqueDES.claveIv()
            self.claveDes.insert(clave+','+iv)
        elif(modo=='ECB'):
            clave=bloque.BloqueDES.clave()
            self.claveDes.insert(clave)
        elif(modo=='OFB'):
            clave,iv=bloque.BloqueDES.claveIv()
            self.claveDes.insert(clave+','+iv)
        elif(modo=='CTR'):
            clave,iv=bloque.BloqueDES.claveCTR()
            self.claveDes.insert(clave+','+iv)
    def desBCopiar(self):
        clipboard.copy(self.desTextoResult.toPlainText())
##=======================================================================================================================

##AesTexto=========================================================================================================
    def aesBCifrar(self):
        if (self.aesTextoOriginal.toPlainText()!=''):
            texto=self.aesTextoOriginal.toPlainText()
            if(self.claveAes.text()!=""):
               modo=self.aesModo.currentText()
               clave=self.claveAes.text()
               self.aesTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.cifrarCBC(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveAes.text()
                    cifrado=bloque.BloqueAES.cifrarECB(clave,texto)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.cifrarOFB(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.cifrarCTR(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
    def aesBDescifrar(self):
        if (self.aesTextoOriginal.toPlainText()!=''):
            texto=self.aesTextoOriginal.toPlainText()
            if(self.claveAes.text()!=""):
               modo=self.aesModo.currentText()
               clave=self.claveAes.text()
               self.aesTextoResult.clear()
               if(modo=='CBC'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.descifrarCBC(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='ECB'):
                    clave=self.claveAes.text()
                    cifrado=bloque.BloqueAES.descifrarECB(clave,texto)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='OFB'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.descifrarOFB(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
               elif(modo=='CTR'):
                    claveIv=self.claveAes.text()
                    claveIvLst=claveIv.split(sep=',')
                    clave=claveIvLst[0]
                    iv=claveIvLst[1]
                    cifrado=bloque.BloqueAES.descifrarCTR(clave,texto,iv)
                    self.aesTextoResult.insertPlainText(cifrado)
    def aesBGenerarClave(self):
        self.claveAes.clear()
        modo=self.aesModo.currentText()
        if(modo=='CBC'):
            clave,iv=bloque.BloqueAES.claveIv()
            self.claveAes.insert(clave+','+iv)
        elif(modo=='ECB'):
            clave=bloque.BloqueAES.clave()
            self.claveAes.insert(clave)
        elif(modo=='OFB'):
            clave,iv=bloque.BloqueAES.claveIv()
            self.claveAes.insert(clave+','+iv)
        elif(modo=='CTR'):
            clave,iv=bloque.BloqueAES.claveCTR()
            self.claveAes.insert(clave+','+iv)
    def aesTextoCopiar(self):
        clipboard.copy(self.aesTextoResult.toPlainText())
##=======================================================================================================================

##AesImagen============================================================================================================
    def aesCargarImagen(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhotoAes(self.image)
        return(self.filename)
    def aesCargarImagen2(self,filename):
        self.image = cv2.imread(filename)
        self.setPhotoAes2(self.image)
    def setPhotoAes(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_3.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhotoAes2(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_4.setPixmap(QtGui.QPixmap.fromImage(image))


    def aesImgCifrar(self):
        path=self.aesCargarImagen()
        modo=self.aesImageModo.currentText()
        if(modo=='CBC'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.cifrarCBC(path,clave,iv)
        elif(modo=='ECB'):
            clave=self.claveAesImage.text()
            bloque.AesImage.cifrarECB(path,clave)
        elif(modo=='OFB'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.cifrarOFB(path,clave,iv)
        elif(modo=='CTR'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.cifrarCTR(path,clave,iv)
        self.aesCargarImagen2('Prueba/AesEncrypted.png')
    def aesImgDescifrar(self):
        path=self.aesCargarImagen()
        modo=self.aesImageModo.currentText()
        if(modo=='CBC'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.descifrarCBC(path,clave,iv)
        elif(modo=='ECB'):
            clave=self.claveAesImage.text()
            bloque.AesImage.descifrarECB(path,clave)
        elif(modo=='OFB'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.descifrarOFB(path,clave,iv)
        elif(modo=='CTR'):
            claveIv=self.claveAesImage.text()
            claveIvLst=claveIv.split(sep=',')
            clave=claveIvLst[0].encode('utf-8')
            iv=claveIvLst[1].encode('utf-8')
            bloque.AesImage.descifrarCTR(path,clave,iv)
        self.aesCargarImagen2('Prueba/AesDecrypted.png')
    def aesImageGenerarClave(self):
        self.claveAesImage.clear()
        modo=self.aesImageModo.currentText()
        if(modo=='CBC'):
            clave,iv = bloque.AesImage.GenerarClaveIv()
            self.claveAesImage.insert(clave.decode('utf-8')+','+ iv.decode('utf-8'))
        elif(modo=='ECB'):
            clave=bloque.AesImage.GenerarClave()
            self.claveAesImage.insert(clave.decode('utf-8'))
        elif(modo=='OFB'):
            clave,iv = bloque.AesImage.GenerarClaveIv()
            self.claveAesImage.insert(clave.decode('utf-8')+','+ iv.decode('utf-8'))
        elif(modo=='CTR'):
            clave,iv=bloque.AesImage.GenerarClaveCtr()
            self.claveAesImage.insert(clave.decode('utf-8')+','+ iv.decode('utf-8'))
        
##=======================================================================================================================

##Rsa(clave)========================================================================================================= 
    def rsaBDescifrar(self):
        clavePath='Prueba/claveRSAPrivada.pem'
        with open(clavePath,'r') as file:
            claveStr=file.read()
        clave=RSA.import_key(claveStr.encode('utf-8'))
        self.rsaTextoResult.clear()
        texto=clavePublica.ClavePublicaRsa.descifrar(self.rsaTextoOriginal.toPlainText(),clave)
        self.rsaTextoResult.insertPlainText(texto)

    def rsaBCifrar(self):
        clavePath='Prueba/claveRSAPublica.pem'
        with open(clavePath,'r') as file:
            claveStr=file.read()
        clave=RSA.import_key(claveStr.encode('utf-8'))
        self.rsaTextoResult.clear()
        texto=clavePublica.ClavePublicaRsa.cifrar(self.rsaTextoOriginal.toPlainText(),clave)
        self.rsaTextoResult.insertPlainText(texto)

    def rsaBGenerar(self):
        clave=clavePublica.ClavePublicaRsa.clave()
        clave2=clave.public_key()
        claveStr=clave.export_key().decode('utf-8')
        claveStr2=clave2.export_key().decode('utf-8')
        clavePath='Prueba/claveRSAPrivada.pem'
        with open(clavePath,'w') as file:
            file.write(claveStr)
        clavePublicaPath='Prueba/claveRSAPublica.pem'
        with open(clavePublicaPath,'w') as file:
            file.write(claveStr2)
    def rsaBCopiar(self):
        clipboard.copy(self.rsaTextoResult.toPlainText())
##=======================================================================================================================

##Gamal(clave)=========================================================================================================

    def gamalDescifrar(self):
        clave=self.claveGamalPrivada.text()
        claveLst=clave.split(sep=',')
        a=int(claveLst[0])
        p=int(claveLst[1])
        self.gamTextoResult.clear()
        cifrado=self.gamTextoOriginal.toPlainText()
        cifradoLst=cifrado.split(sep=',')
        y1str=cifradoLst[0]
        y2str=cifradoLst[1]
        texto=clavePublica.ClavePublicaElGamal.descifrar(y1str,y2str,a,p)
        self.gamTextoResult.clear()
        self.gamTextoResult.insertPlainText(texto)

    def gamalCifrar(self):
        clave=self.claveGamalPublica.text()
        claveLst=clave.split(sep=',')
        g=int(claveLst[0])
        p=int(claveLst[1])
        K=int(claveLst[2])
        self.rsaTextoResult.clear()
        texto=clavePublica.ClavePublicaElGamal.cifrar(self.gamTextoOriginal.toPlainText(),g,p,K)
        y1Str=texto[0]
        y2Str=texto[1]
        self.gamTextoResult.clear()
        self.gamTextoResult.insertPlainText((y1Str+','+y2Str))

    def gamalGenerar(self):
        g,p,K,a=clavePublica.ClavePublicaElGamal.clave()
        self.claveGamalPublica.clear()
        self.claveGamalPrivada.clear()
        self.claveGamalPublica.insert(str(g)+','+str(p)+','+str(K))
        self.claveGamalPrivada.insert(str(a)+','+str(p))
    
    def gamalCopiar(self):
        clipboard.copy(self.gamTextoResult.toPlainText())
##=======================================================================================================================

##Rabin=========================================================================================================
    def rabinCifrar(self):
        clave=int(self.claveRabinPublica.text())
        self.rabTextoResult.clear()
        s=self.rabTextoOriginal.toPlainText()
        m = int.from_bytes(s.encode('utf-8'), byteorder='big')
        cifrado=clavePublica.Rabin.cifrar(m,clave)
        self.rabTextoResult.insertPlainText(str(cifrado))
    def rabinDescifrar(self):
        clave=self.claveRabinPrivada.text()
        claveLst=clave.split(sep=',')
        p=int(claveLst[0])
        q=int(claveLst[1])
        self.rabTextoResult.clear()
        cifrado=clavePublica.Rabin.descifrar(int(self.rabTextoOriginal.toPlainText()),p,q)
        for b in cifrado:
            dec = b.to_bytes(math.ceil(b.bit_length() / 8), byteorder='big').decode('utf-8', 'replace')
            self.rabTextoResult.insertPlainText(dec)
            self.rabTextoResult.insertPlainText("\n")
    def rabinGenerar(self):
        clave=clavePublica.Rabin.clave(self.rabTextoOriginal.toPlainText())
        n,p,q=clave
        self.claveRabinPublica.clear()
        self.claveRabinPrivada.clear()
        self.claveRabinPublica.insert(str(n))
        self.claveRabinPrivada.insert(str(p)+','+str(q))
        return

    def rabinCopiar(self):
        clipboard.copy(self.rabTextoResult.toPlainText())
##=======================================================================================================================

##Rsa(firma)=========================================================================================================
    def firmaDigitalRsaCopiar(self):
        clipboard.copy(self.fiRsaTextoResult.toPlainText())
##=======================================================================================================================

##DSA=========================================================================================================
    def dsaBFirmar(self):
        f=open("Prueba/clavePrivadaFirmaDSA.pem","r")
        clave=DSA.import_key(f.read().encode('utf-8'))
        texto=self.fiDsaTextoOriginal.toPlainText()
        firma=firmaDigital.FirmaDigitalDSA.firma(texto,clave)
        self.fiDsaTextoResult.clear()
        self.fiDsaTextoResult.insertPlainText(firma)
        f.close()
    def dsaBVerificar(self):
        f=open("Prueba/clavePublicaFirmaDSA.pem","r")
        clave=DSA.import_key(f.read().encode('utf-8'))
        textoFirma=self.fiDsaTextoOriginal.toPlainText()
        textoFirmaLst=textoFirma.split(sep=',')
        texto=textoFirmaLst[0]
        firma=textoFirmaLst[1]
        try:
            verificar=firmaDigital.FirmaDigitalDSA.verificar(texto,clave,firma)
            self.fiDsaTextoResult.clear()
            self.fiDsaTextoResult.insertPlainText(verificar)
        except ValueError:
            self.fiDsaTextoResult.clear()
            self.fiDsaTextoResult.insertPlainText('EL MENSAJE NO ES AUTÉNTICO')
        f.close()
    def dsaBGenerarClave(self):
        clave=firmaDigital.FirmaDigitalDSA.clave()
        f=open("Prueba/clavePrivadaFirmaDSA.pem","w")
        f.write(clave.export_key().decode('utf-8'))
        f.close()
        g=open("Prueba/clavePublicaFirmaDSA.pem","w")
        g.write(clave.public_key().export_key().decode('utf-8'))
        g.close()
    def firmaDigitalDsaCopiar(self):
        clipboard.copy(self.fiDsaTextoResult.toPlainText())
##=======================================================================================================================

##Gamal(firma)=========================================================================================================
    def firmaDigitalGamalCopiar(self):
        clipboard.copy(self.fiGamTextoResult.toPlainText())
##=======================================================================================================================

##=======================================================================================================================
    def Side_Menu_Def_0(self):
        if self.frame.width() <= 10:
            self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(163)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(163)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

        else:
            self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(163)
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(163)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

    def Side_Menu_Def_1(self,Event):
        if Event.button()==QtCore.Qt.LeftButton:
            if self.frame.width()>=10:
                 self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
                 self.animation1.setDuration(500)
                 self.animation1.setStartValue(163)
                 self.animation1.setEndValue(0)
                 self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                 self.animation1.start()
                 
                 self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
                 self.animation2.setDuration(500)
                 self.animation2.setStartValue(163)
                 self.animation2.setEndValue(0)
                 self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                 self.animation2.start()
        else:
            pass

    def MoveWindow(self, event):
        self.move(self.pos() + event.globalPos() - self.clickPosition)
        self.clickPosition = event.globalPos()
        event.accept()
        pass
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass

    def copiar(self, event):
        self.stackedWidget.currentWidget()

def ajustar(texto):
    texto=texto.upper()
    return texto.replace(" ","")

if __name__ == "__main__":
    MainApp = QtWidgets.QApplication([])
    App = MainGui()
    App.show()
    sys.exit(MainApp.exec_())