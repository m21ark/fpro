from PyQt5 import QtCore, QtGui, QtWidgets
import pygame,os,sys
from pygame.locals import *
from random import randint as rand
from random import choice
from game_core import game
from store_win import Ui_SecondWindow
from start_win import Ui_FirstWindow


def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)# Garante que import de imagens funciona

def game_GUI():																																										
	class Controller:
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