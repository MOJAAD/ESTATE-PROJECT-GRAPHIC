#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT   OF  ESTATE                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/29/5                                                    #
#                                                                                                                   #
#                                                                                                                   #
#################################################### MODULES ########################################################
import pickle
from os import path,system,name
from time import sleep 
from sys import exit,argv
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap,QFont,QMovie,QPainter
from PIL import Image
#####################################################################################################################
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,100,750,500)
        self.setWindowTitle("ESTATE App")
        self.UI()
        self.show()

    def UI(self):
        pass



#####################################################################################################################
def main():
    App = QApplication(argv)
    Window = window()
    exit(App.exec_())

if __name__ == '__main__':
    main()
#####################################################################################################################

