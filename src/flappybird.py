from PyQt5 import QtCore, QtGui, QtWidgets
import pygame,os,sys
from pygame.locals import *
from random import randint as rand
from random import choice
from game_core import game

def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)# Garante que import de imagens funciona

def game_GUI():
	class Ui_FirstWindow(object):
		def setupUi(self, MainWindow):
			MainWindow.setObjectName("MainWindow")
			MainWindow.setFixedSize(570, 860) # Prende tamanho da janela
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
			MainWindow.setSizePolicy(sizePolicy)
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(getdir(getdir("Assets\\icon.ico"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			MainWindow.setWindowIcon(icon)
			self.centralwidget = QtWidgets.QWidget(MainWindow)
			self.centralwidget.setObjectName("centralwidget")
			self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
			self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 400, 571, 281))
			self.gridLayoutWidget.setObjectName("gridLayoutWidget")
			self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
			self.gridLayout.setContentsMargins(0, 0, 0, 0)
			self.gridLayout.setObjectName("gridLayout")
			self.store_button = QtWidgets.QPushButton(self.gridLayoutWidget)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.store_button.sizePolicy().hasHeightForWidth())
			self.store_button.setSizePolicy(sizePolicy)
			self.store_button.setMaximumSize(QtCore.QSize(250, 70))
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.store_button.setFont(font)
			self.store_button.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.store_button.setObjectName("store_button")
			self.gridLayout.addWidget(self.store_button, 2, 0, 1, 1)
			self.play_button = QtWidgets.QPushButton(self.gridLayoutWidget)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
			self.play_button.setSizePolicy(sizePolicy)
			self.play_button.setMaximumSize(QtCore.QSize(250, 70))
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.play_button.setFont(font)
			self.play_button.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.play_button.setObjectName("play_button")
			self.gridLayout.addWidget(self.play_button, 1, 0, 1, 1)
			self.label_2 = QtWidgets.QLabel(self.centralwidget)
			self.label_2.setGeometry(QtCore.QRect(270, 160, 55, 16))
			self.label_2.setText("")
			self.label_2.setObjectName("label_2")
			self.label = QtWidgets.QLabel(self.centralwidget)
			self.label.setGeometry(QtCore.QRect(0, 0, 581, 861))
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
			self.label.setSizePolicy(sizePolicy)
			self.label.setText("")
			self.label.setPixmap(QtGui.QPixmap(getdir("Assets\\sky0.png")))
			self.label.setScaledContents(True)
			self.label.setWordWrap(True)
			self.label.setObjectName("label")
			self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
			self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 571, 304))
			self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
			self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
			self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
			self.gridLayout_2.setObjectName("gridLayout_2")
			self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
			self.label_3.setMaximumSize(QtCore.QSize(450, 200))
			self.label_3.setText("")
			self.label_3.setPixmap(QtGui.QPixmap(getdir("Assets\\title.png")))
			self.label_3.setScaledContents(True)
			self.label_3.setObjectName("label_3")
			self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
			self.OWN_L = QtWidgets.QLabel(self.centralwidget)
			self.OWN_L.setGeometry(QtCore.QRect(404, 829, 161, 31))
			font = QtGui.QFont()
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			self.OWN_L.setFont(font)
			self.OWN_L.setObjectName("OWN_L")
			self.highscore_label = QtWidgets.QLabel(self.centralwidget)
			self.highscore_label.setGeometry(QtCore.QRect(5, 832, 161, 31))
			font = QtGui.QFont()
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			self.highscore_label.setFont(font)
			self.highscore_label.setObjectName("highscore_label")
			self.label_4 = QtWidgets.QLabel(self.centralwidget)
			self.label_4.setGeometry(QtCore.QRect(0, -20, 571, 881))
			self.label_4.setText("")
			self.label_4.setPixmap(QtGui.QPixmap("../sky0.png"))
			self.label_4.setScaledContents(True)
			self.label_4.setObjectName("label_4")
			self.label_4.raise_()
			self.label.raise_()
			self.gridLayoutWidget.raise_()
			self.label_2.raise_()
			self.gridLayoutWidget_2.raise_()
			self.OWN_L.raise_()
			self.highscore_label.raise_()
			MainWindow.setCentralWidget(self.centralwidget)

			self.retranslateUi(MainWindow)
			QtCore.QMetaObject.connectSlotsByName(MainWindow)

			self.play_button.clicked.connect(lambda: game())
			# self.store_button.clicked.connect(lambda: print("Store"))

		def retranslateUi(self, MainWindow):
			with open(getdir("Assets\\stored_info.txt"),"r") as f:
				stored_info = f.read().split(",")
				HIGHSCORE = int(stored_info[0])

			_translate = QtCore.QCoreApplication.translate
			MainWindow.setWindowTitle(_translate("MainWindow", "Flappy Bird"))
			self.store_button.setText(_translate("MainWindow", "Loja"))
			self.play_button.setText(_translate("MainWindow", "Play"))
			self.OWN_L.setText(_translate("MainWindow", "Marco André 2020"))
			self.highscore_label.setText(_translate("MainWindow", f"Highscore: {HIGHSCORE}"))

		def LoadSecondWindow(self):
			SecondWindow = QtWidgets.QMainWindow()
			ui = Ui_SecondWindow()
			ui.setupUi(SecondWindow)
			SecondWindow.show()

		def win_update(self):
			self.update()
			
	class Ui_SecondWindow(object):
		def setupUi(self, store_window):
			store_window.setObjectName("store_window")
			store_window.setFixedSize(997, 903) # Prende tamanho da janela
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(store_window.sizePolicy().hasHeightForWidth())
			store_window.setSizePolicy(sizePolicy)
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(getdir("Assets\\icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			store_window.setWindowIcon(icon)
			self.centralwidget = QtWidgets.QWidget(store_window)
			self.centralwidget.setObjectName("centralwidget")
			self.label_2 = QtWidgets.QLabel(self.centralwidget)
			self.label_2.setGeometry(QtCore.QRect(230, 40, 55, 16))
			self.label_2.setText("")
			self.label_2.setObjectName("label_2")
			self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
			self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 941, 821))
			self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
			self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
			self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
			self.verticalLayout_2.setObjectName("verticalLayout_2")
			self.verticalLayout_3 = QtWidgets.QVBoxLayout()
			self.verticalLayout_3.setObjectName("verticalLayout_3")
			self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_7.setObjectName("horizontalLayout_7")
			self.img1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img1.setText("")
			self.img1.setPixmap(QtGui.QPixmap(getdir("Assets/bird1.png")))
			self.img1.setScaledContents(True)
			self.img1.setObjectName("img1")
			self.horizontalLayout_7.addWidget(self.img1)
			spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_7.addItem(spacerItem)
			self.img2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img2.setText("")
			self.img2.setPixmap(QtGui.QPixmap(getdir("Assets/bird2.png")))
			self.img2.setScaledContents(True)
			self.img2.setObjectName("img2")
			self.horizontalLayout_7.addWidget(self.img2)
			spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_7.addItem(spacerItem1)

			self.img3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img3.setText("")
			self.img3.setPixmap(QtGui.QPixmap(getdir("Assets/bird3.png")))
			self.img3.setScaledContents(True)
			self.img3.setObjectName("img3")
			self.horizontalLayout_7.addWidget(self.img3)
			spacerItem2 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_7.addItem(spacerItem2)

			self.img4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img4.setText("")
			self.img4.setPixmap(QtGui.QPixmap(getdir("Assets/bird4.png")))
			self.img4.setScaledContents(True)
			self.img4.setObjectName("img4")
			self.horizontalLayout_7.addWidget(self.img4)
			spacerItem3 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_7.addItem(spacerItem3)

			self.img5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img5.setText("")
			self.img5.setPixmap(QtGui.QPixmap(getdir("Assets/bird5.png")))
			self.img5.setScaledContents(True)
			self.img5.setObjectName("img5")
			self.horizontalLayout_7.addWidget(self.img5)
			self.verticalLayout_3.addLayout(self.horizontalLayout_7)
			self.verticalLayout_2.addLayout(self.verticalLayout_3)
			self.verticalLayout = QtWidgets.QVBoxLayout()
			self.verticalLayout.setObjectName("verticalLayout")
			self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_2.setObjectName("horizontalLayout_2")
			self.buy1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy1.sizePolicy().hasHeightForWidth())
			self.buy1.setSizePolicy(sizePolicy)
			self.buy1.setMaximumSize(QtCore.QSize(250, 70))
		   
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy1.setFont(font)
			self.buy1.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy1.setObjectName("buy1")
			self.horizontalLayout_2.addWidget(self.buy1)
			spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_2.addItem(spacerItem4)
			self.buy2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy2.sizePolicy().hasHeightForWidth())
			self.buy2.setSizePolicy(sizePolicy)
			self.buy2.setMaximumSize(QtCore.QSize(250, 70))
			
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy2.setFont(font)
			self.buy2.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy2.setObjectName("buy2")
			self.horizontalLayout_2.addWidget(self.buy2)
			spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_2.addItem(spacerItem5)
			self.buy3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy3.sizePolicy().hasHeightForWidth())
			self.buy3.setSizePolicy(sizePolicy)
			self.buy3.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy3.setFont(font)
			self.buy3.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy3.setObjectName("buy3")
			self.horizontalLayout_2.addWidget(self.buy3)
			spacerItem6 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_2.addItem(spacerItem6)
			self.buy4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy4.sizePolicy().hasHeightForWidth())
			self.buy4.setSizePolicy(sizePolicy)
			self.buy4.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy4.setFont(font)
			self.buy4.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy4.setObjectName("buy4")
			self.horizontalLayout_2.addWidget(self.buy4)
			spacerItem7 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_2.addItem(spacerItem7)
			self.buy5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy5.sizePolicy().hasHeightForWidth())
			self.buy5.setSizePolicy(sizePolicy)
			self.buy5.setMaximumSize(QtCore.QSize(250, 70))
		
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy5.setFont(font)
			self.buy5.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy5.setObjectName("buy5")
			self.horizontalLayout_2.addWidget(self.buy5)
			self.verticalLayout.addLayout(self.horizontalLayout_2)
			self.verticalLayout_2.addLayout(self.verticalLayout)
			spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
			self.verticalLayout_2.addItem(spacerItem8)
			self.verticalLayout_5 = QtWidgets.QVBoxLayout()
			self.verticalLayout_5.setObjectName("verticalLayout_5")
			self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_9.setObjectName("horizontalLayout_9")
			self.img6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img6.setMaximumSize(QtCore.QSize(70, 150))
			self.img6.setText("")
			self.img6.setPixmap(QtGui.QPixmap(getdir("Assets/pipe1.png")))
			self.img6.setScaledContents(True)
			self.img6.setObjectName("img6")
			self.horizontalLayout_9.addWidget(self.img6)
			spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_9.addItem(spacerItem9)
			self.img7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img7.setMaximumSize(QtCore.QSize(70, 150))
			self.img7.setText("")
			self.img7.setPixmap(QtGui.QPixmap(getdir("Assets/pipe2.png")))
			self.img7.setScaledContents(True)
			self.img7.setObjectName("img7")
			self.horizontalLayout_9.addWidget(self.img7)
			spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_9.addItem(spacerItem10)
			self.img8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img8.setMaximumSize(QtCore.QSize(70, 150))
			self.img8.setText("")
			self.img8.setPixmap(QtGui.QPixmap(getdir("Assets/pipe3.png")))
			self.img8.setScaledContents(True)
			self.img8.setObjectName("img8")
			self.horizontalLayout_9.addWidget(self.img8)
			spacerItem11 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_9.addItem(spacerItem11)
			self.img9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img9.setMaximumSize(QtCore.QSize(70, 150))
			self.img9.setText("")
			self.img9.setPixmap(QtGui.QPixmap(getdir("Assets/pipe4.png")))
			self.img9.setScaledContents(True)
			self.img9.setObjectName("img9")
			self.horizontalLayout_9.addWidget(self.img9)
			spacerItem12 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_9.addItem(spacerItem12)
			self.img10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img10.setMaximumSize(QtCore.QSize(70, 150))
			self.img10.setText("")
			self.img10.setPixmap(QtGui.QPixmap(getdir("Assets/pipe5.png")))
			self.img10.setScaledContents(True)
			self.img10.setObjectName("img10")
			self.horizontalLayout_9.addWidget(self.img10)
			self.verticalLayout_5.addLayout(self.horizontalLayout_9)
			self.verticalLayout_2.addLayout(self.verticalLayout_5)
			self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_4.setObjectName("horizontalLayout_4")
			self.buy6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy6.sizePolicy().hasHeightForWidth())
			self.buy6.setSizePolicy(sizePolicy)
			self.buy6.setMaximumSize(QtCore.QSize(250, 70))
	  
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy6.setFont(font)
			self.buy6.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy6.setObjectName("buy6")
			self.horizontalLayout_4.addWidget(self.buy6)
			spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_4.addItem(spacerItem13)
			self.buy7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy7.sizePolicy().hasHeightForWidth())
			self.buy7.setSizePolicy(sizePolicy)
			self.buy7.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy7.setFont(font)
			self.buy7.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy7.setObjectName("buy7")
			self.horizontalLayout_4.addWidget(self.buy7)
			spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_4.addItem(spacerItem14)
			self.buy8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy8.sizePolicy().hasHeightForWidth())
			self.buy8.setSizePolicy(sizePolicy)
			self.buy8.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy8.setFont(font)
			self.buy8.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy8.setObjectName("buy8")
			self.horizontalLayout_4.addWidget(self.buy8)
			spacerItem15 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_4.addItem(spacerItem15)
			self.buy9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy9.sizePolicy().hasHeightForWidth())
			self.buy9.setSizePolicy(sizePolicy)
			self.buy9.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy9.setFont(font)
			self.buy9.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy9.setObjectName("buy9")
			self.horizontalLayout_4.addWidget(self.buy9)
			spacerItem16 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_4.addItem(spacerItem16)
			self.buy10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy10.sizePolicy().hasHeightForWidth())
			self.buy10.setSizePolicy(sizePolicy)
			self.buy10.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy10.setFont(font)
			self.buy10.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy10.setObjectName("buy10")
			self.horizontalLayout_4.addWidget(self.buy10)
			self.verticalLayout_2.addLayout(self.horizontalLayout_4)
			spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
			self.verticalLayout_2.addItem(spacerItem17)
			self.verticalLayout_6 = QtWidgets.QVBoxLayout()
			self.verticalLayout_6.setObjectName("verticalLayout_6")
			self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_10.setObjectName("horizontalLayout_10")
			self.img11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img11.setMaximumSize(QtCore.QSize(80, 150))
			self.img11.setText("")
			self.img11.setPixmap(QtGui.QPixmap(getdir("Assets/sky2.png")))
			self.img11.setScaledContents(True)
			self.img11.setObjectName("img11")
			self.horizontalLayout_10.addWidget(self.img11)
			spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_10.addItem(spacerItem18)
			self.img12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img12.setMaximumSize(QtCore.QSize(80, 150))
			self.img12.setText("")
			self.img12.setPixmap(QtGui.QPixmap(getdir("Assets/sky3.png")))
			self.img12.setScaledContents(True)
			self.img12.setObjectName("img12")
			self.horizontalLayout_10.addWidget(self.img12)
			spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_10.addItem(spacerItem19)
			self.img13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img13.setMaximumSize(QtCore.QSize(80, 150))
			self.img13.setText("")
			self.img13.setPixmap(QtGui.QPixmap(getdir("Assets/sky1.xpm")))
			self.img13.setScaledContents(True)
			self.img13.setObjectName("img13")
			self.horizontalLayout_10.addWidget(self.img13)
			spacerItem20 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_10.addItem(spacerItem20)
			self.img14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img14.setMaximumSize(QtCore.QSize(80, 150))
			self.img14.setText("")
			self.img14.setPixmap(QtGui.QPixmap(getdir("Assets/sky4.xpm")))
			self.img14.setScaledContents(True)
			self.img14.setObjectName("img14")
			self.horizontalLayout_10.addWidget(self.img14)
			spacerItem21 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_10.addItem(spacerItem21)
			self.img15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
			self.img15.setMaximumSize(QtCore.QSize(80, 150))
			self.img15.setText("")
			self.img15.setPixmap(QtGui.QPixmap(""))
			self.img15.setScaledContents(True)
			self.img15.setObjectName("img15")
			self.horizontalLayout_10.addWidget(self.img15)
			self.verticalLayout_6.addLayout(self.horizontalLayout_10)
			self.verticalLayout_2.addLayout(self.verticalLayout_6)
			self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
			self.horizontalLayout_5.setObjectName("horizontalLayout_5")
			self.buy11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy11.sizePolicy().hasHeightForWidth())
			self.buy11.setSizePolicy(sizePolicy)
			self.buy11.setMaximumSize(QtCore.QSize(250, 70))

			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy11.setFont(font)
			self.buy11.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy11.setObjectName("buy11")
			self.horizontalLayout_5.addWidget(self.buy11)
			spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_5.addItem(spacerItem22)
			self.buy12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy12.sizePolicy().hasHeightForWidth())
			self.buy12.setSizePolicy(sizePolicy)
			self.buy12.setMaximumSize(QtCore.QSize(250, 70))
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy12.setFont(font)
			self.buy12.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy12.setObjectName("buy12")
			self.horizontalLayout_5.addWidget(self.buy12)
			spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_5.addItem(spacerItem23)
			self.buy13 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy13.sizePolicy().hasHeightForWidth())
			self.buy13.setSizePolicy(sizePolicy)
			self.buy13.setMaximumSize(QtCore.QSize(250, 70))
			
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy13.setFont(font)
			self.buy13.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy13.setObjectName("buy13")
			self.horizontalLayout_5.addWidget(self.buy13)
			spacerItem24 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_5.addItem(spacerItem24)
			self.buy14 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy14.sizePolicy().hasHeightForWidth())
			self.buy14.setSizePolicy(sizePolicy)
			self.buy14.setMaximumSize(QtCore.QSize(250, 70))
			
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy14.setFont(font)
			self.buy14.setStyleSheet("background-color: rgb(255, 206, 26);")
			self.buy14.setObjectName("buy14")
			self.horizontalLayout_5.addWidget(self.buy14)
			spacerItem25 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
			self.horizontalLayout_5.addItem(spacerItem25)
			self.buy15 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
			sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.buy15.sizePolicy().hasHeightForWidth())
			self.buy15.setSizePolicy(sizePolicy)
			self.buy15.setMaximumSize(QtCore.QSize(250, 70))
			
			font = QtGui.QFont()
			font.setFamily("Arial")
			font.setPointSize(15)
			font.setBold(True)
			font.setWeight(75)
			self.buy15.setFont(font)
			self.buy15.setStyleSheet("background-color: rgb(255, 160, 26);")
			self.buy15.setObjectName("buy15")
			self.horizontalLayout_5.addWidget(self.buy15)
			self.verticalLayout_2.addLayout(self.horizontalLayout_5)
			self.label_31 = QtWidgets.QLabel(self.centralwidget)
			self.label_31.setGeometry(QtCore.QRect(1010, 630, 55, 16))
			self.label_31.setText("")
			self.label_31.setObjectName("label_31")
			self.label = QtWidgets.QLabel(self.centralwidget)
			self.label.setGeometry(QtCore.QRect(0, -10, 1001, 921))
			self.label.setText("")
			self.label.setPixmap(QtGui.QPixmap(getdir("Assets\\sky0.png")))
			self.label.setScaledContents(True)
			self.label.setObjectName("label")
			self.Back_Label = QtWidgets.QLabel(self.centralwidget)
			self.Back_Label.setGeometry(QtCore.QRect(360, 840, 281, 51))
			font = QtGui.QFont()
			font.setPointSize(15)
			font.setBold(False)
			font.setWeight(50)
			self.Back_Label.setFont(font)
			self.Back_Label.setObjectName("Back_Label")
			self.label.raise_()
			self.label_2.raise_()
			self.verticalLayoutWidget_2.raise_()
			self.label_31.raise_()
			self.Back_Label.raise_()
			store_window.setCentralWidget(self.centralwidget)

			self.retranslateUi(store_window)
			QtCore.QMetaObject.connectSlotsByName(store_window)


			####### Skins buy controll


			def buy(s):
				with open(getdir("Assets\\stored_info.txt"),"r") as f:
					stored_info = f.read().split(",")
					HIGHSCORE = int(stored_info[0])
					COIN_VAULT = int(stored_info[1])

				with open(getdir("Assets\\skin_info.txt"),"r") as f:
					skins_list = f.read().split(",")

				bird_skins = skins_list[:skins_list.index("Xbird0")+1]
				pipe_skins = skins_list[skins_list.index("Xbird0")+1:skins_list.index("Xpipe0")+1]
				sky_skins = skins_list[skins_list.index("Xpipe0")+1:]

				bird_skins_buy = list(filter(lambda x: not "X" in x,bird_skins))
				pipe_skins_buy = list(filter(lambda x: not  "X" in x,pipe_skins))
				sky_skins_buy = list(filter(lambda x: not  "X" in x,sky_skins))

				if s in bird_skins_buy:
					if COIN_VAULT >=10:
						bird_skins_buy.remove(s)
						skins_list[skins_list.index(s)]="X" + s
						COIN_VAULT -=10
						with open(getdir("Assets\\skin_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in skins_list])))
						with open(getdir("Assets\\stored_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in [HIGHSCORE,COIN_VAULT]])))


				if s in pipe_skins_buy:
					if COIN_VAULT >=15:
						pipe_skins_buy.remove(s)
						skins_list[skins_list.index(s)]="X" + s
						COIN_VAULT -=15
						with open(getdir("Assets\\skin_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in skins_list])))
						with open(getdir("Assets\\stored_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in [HIGHSCORE,COIN_VAULT]])))



				if s in sky_skins_buy:
					if COIN_VAULT >=40:
						sky_skins_buy.remove(s)
						skins_list[skins_list.index(s)]="X" + s
						COIN_VAULT -=40
						with open(getdir("Assets\\skin_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in skins_list])))
						with open(getdir("Assets\\stored_info.txt"),"w") as f:
							f.write(str(",".join([str(i) for i in [HIGHSCORE,COIN_VAULT]])))
						
				_translate = QtCore.QCoreApplication.translate
				if "bird1" in bird_skins_buy:
					self.buy1.setText(_translate("store_window", "10 $ "))
					if COIN_VAULT<10:
						self.buy1.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy1.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy1.setText(_translate("store_window", "Owned"))
					self.buy1.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "bird2" in bird_skins_buy:
					self.buy2.setText(_translate("store_window", "10 $ "))
					if COIN_VAULT<10:
						self.buy2.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy2.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy2.setText(_translate("store_window", "Owned"))
					self.buy2.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "bird3" in bird_skins_buy:
					self.buy3.setText(_translate("store_window", "10 $ "))
					if COIN_VAULT<10:
						self.buy3.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy3.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy3.setText(_translate("store_window", "Owned"))
					self.buy3.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "bird4" in bird_skins_buy:
					self.buy4.setText(_translate("store_window", "10 $ "))
					if COIN_VAULT<10:
						self.buy4.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy4.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy4.setText(_translate("store_window", "Owned"))
					self.buy4.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "bird5" in bird_skins_buy:
					self.buy5.setText(_translate("store_window", "10 $ "))
					if COIN_VAULT<10:
						self.buy5.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy5.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy5.setText(_translate("store_window", "Owned"))
					self.buy5.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "pipe1" in pipe_skins_buy:
					self.buy6.setText(_translate("store_window", "15 $ "))
					if COIN_VAULT<15:
						self.buy6.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy6.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy6.setText(_translate("store_window", "Owned"))
					self.buy6.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "pipe2" in pipe_skins_buy:
					self.buy7.setText(_translate("store_window", "15 $ "))
					if COIN_VAULT<15:
						self.buy7.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy7.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy7.setText(_translate("store_window", "Owned"))
					self.buy7.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "pipe3" in pipe_skins_buy:
					self.buy8.setText(_translate("store_window", "15 $ "))
					if COIN_VAULT<15:
						self.buy8.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy8.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy8.setText(_translate("store_window", "Owned"))
					self.buy8.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "pipe4" in pipe_skins_buy:
					self.buy9.setText(_translate("store_window", "15 $ "))
					if COIN_VAULT<15:
						self.buy9.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy9.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy9.setText(_translate("store_window", "Owned"))
					self.buy9.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "pipe5" in pipe_skins_buy:
					self.buy10.setText(_translate("store_window", "15 $ "))
					if COIN_VAULT<15:
						self.buy10.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy10.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy10.setText(_translate("store_window", "Owned"))
					self.buy10.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "sky1" in sky_skins_buy:
					self.buy11.setText(_translate("store_window", "40 $ "))
					if COIN_VAULT<40:
						self.buy11.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy11.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy11.setText(_translate("store_window", "Owned"))
					self.buy11.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "sky2" in sky_skins_buy:
					self.buy12.setText(_translate("store_window", "40 $ "))
					if COIN_VAULT<40:
						self.buy12.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy12.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy12.setText(_translate("store_window", "Owned"))
					self.buy12.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "sky3" in sky_skins_buy:
					self.buy13.setText(_translate("store_window", "40 $ "))
					if COIN_VAULT<40:
						self.buy13.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy13.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy13.setText(_translate("store_window", "Owned"))
					self.buy13.setStyleSheet("background-color: rgb(120, 200, 40);")
				if "sky4" in sky_skins_buy:
					self.buy14.setText(_translate("store_window", "40 $ "))
					if COIN_VAULT<40:
						self.buy14.setStyleSheet("background-color: rgb(190, 40, 40);")
					else:
						self.buy14.setStyleSheet("background-color: rgb(255, 206, 26);")
				else:
					self.buy14.setText(_translate("store_window", "Owned"))
					self.buy14.setStyleSheet("background-color: rgb(120, 200, 40);")
				self.buy15.setText(_translate("store_window", f" Coins :{COIN_VAULT} "))
				

			self.buy1.clicked.connect(lambda: buy("bird1"))
			self.buy2.clicked.connect(lambda: buy("bird2"))
			self.buy3.clicked.connect(lambda: buy("bird3"))
			self.buy4.clicked.connect(lambda: buy("bird4"))
			self.buy5.clicked.connect(lambda: buy("bird5"))
			self.buy6.clicked.connect(lambda: buy("pipe1"))
			self.buy7.clicked.connect(lambda: buy("pipe2"))
			self.buy8.clicked.connect(lambda: buy("pipe3"))
			self.buy9.clicked.connect(lambda: buy("pipe4"))
			self.buy10.clicked.connect(lambda: buy("pipe5"))
			self.buy11.clicked.connect(lambda: buy("sky1"))
			self.buy12.clicked.connect(lambda: buy("sky2"))  
			self.buy13.clicked.connect(lambda: buy("sky3"))
			self.buy14.clicked.connect(lambda: buy("sky4"))  

			####### Skins buy controll
			
		def retranslateUi(self, store_window):
			with open(getdir("Assets\\stored_info.txt"),"r") as f:
				stored_info = f.read().split(",")
				COIN_VAULT = int(stored_info[1])

			with open(getdir("Assets\\skin_info.txt"),"r") as f:
				skins_list = f.read().split(",")

			bird_skins = skins_list[:skins_list.index("Xbird0")+1]
			pipe_skins = skins_list[skins_list.index("Xbird0")+1:skins_list.index("Xpipe0")+1]
			sky_skins = skins_list[skins_list.index("Xpipe0")+1:]

			bird_skins_buy = list(filter(lambda x: not "X" in x,bird_skins))
			pipe_skins_buy = list(filter(lambda x: not  "X" in x,pipe_skins))
			sky_skins_buy = list(filter(lambda x: not  "X" in x,sky_skins))

			_translate = QtCore.QCoreApplication.translate
			store_window.setWindowTitle(_translate("store_window", "Flappy Bird - Store"))
			self.buy15.setText(_translate("store_window", f" Coins :{COIN_VAULT} "))

			if "bird1" in bird_skins_buy:
				self.buy1.setText(_translate("store_window", "10 $ "))
				if COIN_VAULT<10:
					self.buy1.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy1.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy1.setText(_translate("store_window", "Owned"))
				self.buy1.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "bird2" in bird_skins_buy:
				self.buy2.setText(_translate("store_window", "10 $ "))
				if COIN_VAULT<10:
					self.buy2.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy2.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy2.setText(_translate("store_window", "Owned"))
				self.buy2.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "bird3" in bird_skins_buy:
				self.buy3.setText(_translate("store_window", "10 $ "))
				if COIN_VAULT<10:
					self.buy3.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy3.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy3.setText(_translate("store_window", "Owned"))
				self.buy3.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "bird4" in bird_skins_buy:
				self.buy4.setText(_translate("store_window", "10 $ "))
				if COIN_VAULT<10:
					self.buy4.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy4.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy4.setText(_translate("store_window", "Owned"))
				self.buy4.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "bird5" in bird_skins_buy:
				self.buy5.setText(_translate("store_window", "10 $ "))
				if COIN_VAULT<10:
					self.buy5.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy5.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy5.setText(_translate("store_window", "Owned"))
				self.buy5.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "pipe1" in pipe_skins_buy:
				self.buy6.setText(_translate("store_window", "15 $ "))
				if COIN_VAULT<15:
					self.buy6.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy6.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy6.setText(_translate("store_window", "Owned"))
				self.buy6.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "pipe2" in pipe_skins_buy:
				self.buy7.setText(_translate("store_window", "15 $ "))
				if COIN_VAULT<15:
					self.buy7.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy7.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy7.setText(_translate("store_window", "Owned"))
				self.buy7.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "pipe3" in pipe_skins_buy:
				self.buy8.setText(_translate("store_window", "15 $ "))
				if COIN_VAULT<15:
					self.buy8.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy8.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy8.setText(_translate("store_window", "Owned"))
				self.buy8.setStyleSheet("background-color: rgb(120, 200, 40);")

			if "pipe4" in pipe_skins_buy:
				self.buy9.setText(_translate("store_window", "15 $ "))
				if COIN_VAULT<15:
					self.buy9.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy9.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy9.setText(_translate("store_window", "Owned"))
				self.buy9.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "pipe5" in pipe_skins_buy:
				self.buy10.setText(_translate("store_window", "15 $ "))
				if COIN_VAULT<15:
					self.buy10.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy10.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy10.setText(_translate("store_window", "Owned"))
				self.buy10.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "sky1" in sky_skins_buy:
				self.buy11.setText(_translate("store_window", "40 $ "))
				if COIN_VAULT<40:
					self.buy11.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy11.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy11.setText(_translate("store_window", "Owned"))
				self.buy11.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "sky2" in sky_skins_buy:
				self.buy12.setText(_translate("store_window", "40 $ "))
				if COIN_VAULT<40:
					self.buy12.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy12.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy12.setText(_translate("store_window", "Owned"))
				self.buy12.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "sky3" in sky_skins_buy:
				self.buy13.setText(_translate("store_window", "40 $ "))
				if COIN_VAULT<40:
					self.buy13.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy13.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy13.setText(_translate("store_window", "Owned"))
				self.buy13.setStyleSheet("background-color: rgb(120, 200, 40);")
			if "sky4" in sky_skins_buy:
				self.buy14.setText(_translate("store_window", "40 $ "))
				if COIN_VAULT<40:
					self.buy14.setStyleSheet("background-color: rgb(190, 40, 40);")
				else:
					self.buy14.setStyleSheet("background-color: rgb(255, 206, 26);")
			else:
				self.buy14.setText(_translate("store_window", "Owned"))
				self.buy14.setStyleSheet("background-color: rgb(120, 200, 40);")
																																										

			
	class Controller:

		def __init__(self):
			pass

		def Show_FirstWindow(self):

			self.FirstWindow = QtWidgets.QMainWindow()
			self.ui = Ui_FirstWindow()
			self.ui.setupUi(self.FirstWindow)
			self.ui.store_button.clicked.connect(self.Show_SecondWindow)

			self.FirstWindow.show()

		def Show_SecondWindow(self):
			
			self.SecondWindow = QtWidgets.QMainWindow()
			self.ui = Ui_SecondWindow()
			self.ui.setupUi(self.SecondWindow)
			self.SecondWindow.show()



	app = QtWidgets.QApplication(sys.argv)
	Controller = Controller()
	Controller.Show_FirstWindow()
	sys.exit(app.exec_())

game_GUI()