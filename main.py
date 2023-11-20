from PyQt5 import QtWidgets, uic, QtCore
import sys
import clasico

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
        self.despCifrar.clicked.connect(self.desplazamientoCifrar)
        self.despDescifrar.clicked.connect(self.desplazamientoDescifrar)
        self.despGenerar.clicked.connect(self.desplazamientoGenerarClave)
##=======================================================================================================================

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
##=======================================================================================================================

##Vigenere=========================================================================================================
##=======================================================================================================================

##Permutacion=========================================================================================================
##=======================================================================================================================

##Transposicion=========================================================================================================
##=======================================================================================================================

##Sustitucion=========================================================================================================
##=======================================================================================================================

##Afin=========================================================================================================
##=======================================================================================================================

##Hill=========================================================================================================
##=======================================================================================================================

##Sdes=========================================================================================================
##=======================================================================================================================

##Tdes=========================================================================================================
##=======================================================================================================================

##Des=========================================================================================================
##=======================================================================================================================

##Aes=========================================================================================================
##=======================================================================================================================

##Rsa(clave)=========================================================================================================
##=======================================================================================================================

##Rabin=========================================================================================================
##=======================================================================================================================

##Gamal(clave)=========================================================================================================
##=======================================================================================================================

##Rsa(firma)=========================================================================================================
##=======================================================================================================================

##DSA=========================================================================================================
##=======================================================================================================================

##Gamal(firma)=========================================================================================================
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