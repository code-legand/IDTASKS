from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint

number = randint(0, 100)
print(number)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 468)
        MainWindow.setStyleSheet("background-color: rgb(16, 16, 16);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inst_board = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.inst_board.setFont(font)
        self.inst_board.setStyleSheet("border: 5px solid rgb(0, 0, 0);\n"
"background-color: rgb(90, 229, 52);\n"
"border-radius: 20px;")
        self.inst_board.setReadOnly(True)
        self.inst_board.setObjectName("inst_board")
        self.verticalLayout.addWidget(self.inst_board)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chance1 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.chance1.setFont(font)
        self.chance1.setStyleSheet("background-color: rgb(196, 255, 242);\n"
"border: 5px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.chance1.setReadOnly(False)
        self.chance1.setObjectName("chance1")
        self.horizontalLayout_2.addWidget(self.chance1)

        self.chance2 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.chance2.setFont(font)
        self.chance2.setStyleSheet("background-color: rgb(196, 255, 242);\n"
"border: 5px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.chance2.setReadOnly(True)
        self.chance2.setObjectName("chance2")
        self.horizontalLayout_2.addWidget(self.chance2)
        self.chance3 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.chance3.setFont(font)
        self.chance3.setStyleSheet("background-color: rgb(196, 255, 242);\n"
"border: 5px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.chance3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chance3.setLineWidth(1)
        self.chance3.setReadOnly(True)
        self.chance3.setObjectName("chance3")
        self.horizontalLayout_2.addWidget(self.chance3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.chance1.setFocus()
        self.chance1.textChanged.connect(self.checkValue1)
        self.chance2.textChanged.connect(self.checkValue2)
        self.chance3.textChanged.connect(self.checkValue3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guess the number"))
        self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Can You Guess The Number</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">You have </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ff0000;\">3</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"> Chances Left</span></p></body></html>"))
        self.chance1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chance1.setPlaceholderText(_translate("MainWindow", "1"))
        self.chance2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.chance2.setPlaceholderText(_translate("MainWindow", "2"))
        self.chance3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.chance3.setPlaceholderText(_translate("MainWindow", "3"))

    
    def checkValue1(self):
        text = self.chance1.toPlainText()
        if not text.isdigit() and not text.endswith('\n') and text!="":
            self.chance1.setText("")
            return 
        
        elif text.endswith("\n"):
            global number
            num = int(text)
            if num == number:
                self.inst_board.setText("You Won")
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Congrats!That's Right</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ffffff;\">You Won</span></p></body></html>"))
                self.chance1.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Oops! Wrong Number</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">You have </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ff0000;\">2</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"> Chances Left</span></p></body></html>"))
                self.chance1.setReadOnly(True)
                self.chance2.setReadOnly(False)
                self.chance2.setFocus()
                self.chance1.setStyleSheet("background-color: rgb(255, 0, 0);")

    def checkValue2(self):
        text = self.chance2.toPlainText()
        if not text.isdigit() and not text.endswith('\n') and text!="":
            self.chance2.setText("")
            return
        elif text.endswith("\n"):
            global number
            num = int(text)
            if num == number:
                self.inst_board.setText("You Won")
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Congrats!That's Right</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ffffff;\">You Won</span></p></body></html>"))
                self.chance2.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Oops! Wrong Number</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">You have </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ff0000;\">1</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"> Chance Left</span></p></body></html>"))
                self.chance2.setReadOnly(True)
                self.chance3.setReadOnly(False)
                self.chance3.setFocus()
                self.chance2.setStyleSheet("background-color: rgb(255, 0, 0);")
            
    def checkValue3(self):
        text = self.chance3.toPlainText()
        if not text.isdigit() and not text.endswith('\n') and text!="":
            self.chance3.setText("")
            return
        elif text.endswith("\n"):
            global number
            num = int(text)
            if num == number:
                self.inst_board.setText("You Won")
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Congrats!That's Right</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ffffff;\">You Won</span></p></body></html>"))
                self.chance3.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                _translate = QtCore.QCoreApplication.translate
                self.inst_board.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">Oops! Wrong Number</span></p>\n"
                "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:22pt;\"><br /></p>\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; color:#ffffff;\">You Lost</span></p></body></html>"))
                self.chance3.setReadOnly(True)
                self.chance3.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.inst_board.setStyleSheet("background-color: rgb(255, 0, 0);")

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
