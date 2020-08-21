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
import pickle,sys
from os import path,system,name
from time import sleep 
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize,Qt,QTimer
from PyQt5.QtGui import QPixmap,QFont,QMovie,QPainter,QCursor,QGuiApplication
from PIL import Image
#####################################################################################################################
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,550,500)
        self.setWindowTitle("ESTATE App")
        self.UI()
        

    def UI(self):
        screen = QGuiApplication.screenAt(QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())
        self.show()



#####################################################################################################################
def main():
    App1= QApplication(sys.argv)
    image = QLabel()
    movie = QMovie("images/welcome.gif")
    image.setMovie(movie)
    movie.start()
    # image.setPixmap(QPixmap('images/home_graphic.jpg'))
    image.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    image.move(585,350)
    image.show()
    sleep(5)
    image.close()
    App2 = QApplication(sys.argv)
    Window = window()
    sys.exit(App2.exec_())

if __name__ == '__main__':
    main()
#####################################################################################################################

