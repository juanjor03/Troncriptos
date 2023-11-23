from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
import numpy as np
import imageio
import cv2
import imutils
import sys
import pyperclip as clipboard
import clasico,bloque,clavePublica,firmaDigital
import collections,re,math

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
        self.sdesCopiar.clicked.connect(self.sDesTextoCopiar)
##Tdes========================================================================================================  
        self.tdesCopiar.clicked.connect(self.tDesCopiar)    
##Des======================================================================================================== 
        self.desCopiar.clicked.connect(self.desBCopiar)
##Aes========================================================================================================
        self.aesCopiar.clicked.connect(self.aesTextoCopiar)
##AesImage========================================================================================================
##Rsa========================================================================================================
        self.rsaCopiar.clicked.connect(self.rsaBCopiar)
##Rabin========================================================================================================
        self.rabCopiar.clicked.connect(self.rabinCopiar)
##Gamal========================================================================================================
        self.gamCopiar.clicked.connect(self.gamalCopiar)
##FirmaDigitalRsa========================================================================================================
        self.fiRsaCopiar.clicked.connect(self.firmaDigitalRsaCopiar)
##FirmaDigitalDsa========================================================================================================
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
            self.hilTClave.clear()
            self.hilClave.insert(clave)
        return clave
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
        self.hilCargarImagen2('src/Prueba/Encrypted.png') 

    def hilImgDescifrar(self):
        path=self.hilCargarImagen()
        clave=self.hilCargarImagen3()
        clasico.HillImage.descifrar(path,clave)
        self.hilCargarImagen2('src/Prueba/Decrypted.png')


##=======================================================================================================================

##Sdes=========================================================================================================
    def sDesTextoCopiar(self):
        clipboard.copy(self.sdesTextoResult.toPlainText())
##=======================================================================================================================

##Tdes=========================================================================================================
    def tDesCopiar(self):
        clipboard.copy(self.tdesTextoResult.toPlainText())
##=======================================================================================================================

##Des=========================================================================================================
    def desBCopiar(self):
        clipboard.copy(self.desTextoResult.toPlainText())
##=======================================================================================================================

##AesTexto=========================================================================================================
    def aesTextoCopiar(self):
        clipboard.copy(self.aesTextoResult.toPlainText())
##=======================================================================================================================

##AesImagen=========================================================================================================
##=======================================================================================================================

##Rsa(clave)=========================================================================================================
    def rsaBCopiar(self):
        clipboard.copy(self.rsaTextoResult.toPlainText())
##=======================================================================================================================

##Rabin=========================================================================================================
    def rabinCopiar(self):
        clipboard.copy(self.rabTextoResult.toPlainText())
##=======================================================================================================================

##Gamal(clave)=========================================================================================================
    def gamalCopiar(self):
        clipboard.copy(self.gamTextoResult.toPlainText())
##=======================================================================================================================

##Rsa(firma)=========================================================================================================
    def firmaDigitalRsaCopiar(self):
        clipboard.copy(self.fiRsaTextoResult.toPlainText())
##=======================================================================================================================

##DSA=========================================================================================================
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