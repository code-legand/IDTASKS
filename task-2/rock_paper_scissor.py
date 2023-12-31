from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint

rock = 0
paper = 1
scissor = 2
result = ["You lose", "You win", "Draw"]
moves = ["rock", "paper", "scissor"]
pairs = {(rock, paper) : 0, (rock, scissor): 1, (rock, rock) : 2,
         (paper, rock) : 1, (paper, scissor) : 0, (paper, paper) : 2,
         (scissor, rock) : 0, (scissor, paper) : 1, (scissor, scissor) : 2}



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 865)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(50, 0))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setStyleSheet("background-color: qconicalgradient(cx:0, cy:1, angle:225, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.keyPressEvent = self.keyPressEvent

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissor"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\banner.png\" /></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "↓↓↓ You  V/S  System ↑↑↑"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\banner.png\" /></p></body></html>"))

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_R:
            # print("Rock")
            user_move = 0
            system_move = randint(0, 2)
            self.textEdit_2.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\rock.png\" /></p></body></html>")
            self.textEdit.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\{}.png\" /></p></body></html>".format(moves[system_move]))
            res_index = pairs[(user_move, system_move)]

            self.lineEdit.setText(result[res_index])
            if res_index == 0:
                self.lcdNumber.display(self.lcdNumber.intValue() + 1)
            elif res_index == 1:
                self.lcdNumber_2.display(self.lcdNumber_2.intValue() + 1)
            self.score_check()

        elif key == QtCore.Qt.Key_P:
            # print("Paper")
            user_move = 1
            system_move = randint(0, 2)
            self.textEdit_2.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\paper.png\" /></p></body></html>")
            self.textEdit.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\{}.png\" /></p></body></html>".format(moves[system_move]))
            res_index = pairs[(user_move, system_move)]

            self.lineEdit.setText(result[res_index])
            if res_index == 0:
                self.lcdNumber.display(self.lcdNumber.intValue() + 1)
            elif res_index == 1:
                self.lcdNumber_2.display(self.lcdNumber_2.intValue() + 1)
            self.score_check()

        
        elif key == QtCore.Qt.Key_S:
            # print("Scissor")
            user_move = 2
            system_move = randint(0, 2)
            self.textEdit_2.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\scissor.png\" /></p></body></html>")
            self.textEdit.setHtml("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"D:\\interndev\\task-2\\{}.png\" /></p></body></html>".format(moves[system_move]))
            res_index = pairs[(user_move, system_move)]
            self.lineEdit.setText(result[res_index])
            if res_index == 0:
                self.lcdNumber.display(self.lcdNumber.intValue() + 1)
            elif res_index == 1:
                self.lcdNumber_2.display(self.lcdNumber_2.intValue() + 1)
            self.score_check()

    def score_check(self):
        if self.lcdNumber.intValue() == 5:
            self.lineEdit.setText("You Lost the Game")
            self.lineEdit.setStyleSheet("color: White; background-color: Red;")
            self.lcdNumber.display(0)
            self.lcdNumber_2.display(0)
        elif self.lcdNumber_2.intValue() == 5:
            self.lineEdit.setText("You Won the Game")
            self.lineEdit.setStyleSheet("color: White; background-color: Green;")
            self.lcdNumber.display(0)
            self.lcdNumber_2.display(0)
        else:
            self.lineEdit.setStyleSheet("color: Black; background-color: White;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
