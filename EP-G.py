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
# from time import sleep 
# import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize,Qt,QTimer
from PyQt5.QtGui import QPixmap,QFont,QMovie,QCursor,QGuiApplication,QImage,QPalette,QBrush
# from PIL import Image
################################################# DEFINE CLASSES #################################################### 
class estate:
    area=0
    address=''
    price=0
    description=''
    type_presentation=''

    def __init__(self,area,address,price,description='',type_presentation=''):
        self.area = area
        self.address = address
        self.price = price
        self.description = description
        self.type_presentation = type_presentation

    # def __del__(self,area,address,price,description,type_presentation):
    #     self.area=0
    #     self.address=''
    #     self.price=0
    #     self.description=''
    #     self.type_presentation=''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class farming(estate):
    water_period=0
    def __init__(self,area,address,price,description,type_presentation,water_period=0):
        estate.__init__(self,area,address,price,description,type_presentation)
        self.water_period = water_period

    # def __del__(self,area,address,price,description,type_presentation,water_period):
    #     estate.__del__(self,area,adderss,price,description,type_presentation)
    #     self.water_period=0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class garden(farming):
    def __init__(self,area,address,price,description,type_presentation,water_period,type_garden='',wall=False,bower=False):
        farming.__init__(self,area,address,price,description,type_presentation,water_period)
        self.type_garden = type_garden
        self.wall = wall
        self.bower = bower

    # def showclass(self):
    #     print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
    #     print("TYPE OF GARDEN : {}   WATER PERIOD : {}   WALL : {}   BOWER : {}".format(self.type_garden,self.water_period,self.wall,self.bower))
    #     print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
    #     print("DESCRIPTION : {}".format(self.description))
    #     print("|___________________________________________________________________________________________|")

    # def editclass(self):
    #     while True:
    #         cls()
    #         print("\t\t\t ______________________________________")
    #         print("\t\t\t|   PLEASE SELECT BY NUMBER TO EDIT :  |")
    #         print("\t\t\t|   1) AREA          2) ADDRESS        |")
    #         print("\t\t\t|   3) PRICE         4) TYPE OF GARDEN |")
    #         print("\t\t\t|   5) WATER PERIOD  6) WALL           |")
    #         print("\t\t\t|   7) BOWER         8) DESCRIPTION    |")
    #         print("\t\t\t|   9) TYPE OF PRESENTATION            |")
    #         __selector=input("\t\t\t|______________________________________|")
    #         try:
    #             if __selector=='1':
    #                 __newone=input("\t\t\t| ENTER NEW AREA : ")
    #                 self.area=int(__newone)
    #             elif __selector=='2':
    #                 __newone=input("\t\t\t| ENTER NEW ADDRESS : ")
    #                 self.address=str(__newone)
    #             elif __selector=='3':
    #                 __newone=input("\t\t\t| ENTER NEW PRICE : ")
    #                 self.price=int(__newone)
    #             elif __selector=='4':
    #                 __newone=input("\t\t\t| ENTER NEW TYPE OF GARDEN : ")
    #                 self.type_garden=str(__newone)
    #             elif __selector=='5':
    #                 __newone=input("\t\t\t| ENTER NEW WATER PERIOD : ")
    #                 self.water_period=int(__newone)
    #             elif __selector=='6':
    #                 __newone=input("\t\t\t| HAVE WALL? 1)True Other)False ")
    #                 if __newone=='1':
    #                     self.wall=True
    #                 else :
    #                     self.wall=False
    #             elif __selector=='7':
    #                 __newone=input("\t\t\t| HAVE BOWER? 1)True Other)False ")
    #                 if __newone=='1':
    #                     self.bower=True
    #                 else :
    #                     self.bower=False
    #             elif __selector=='8':
    #                 __newone=input("\t\t\t| ENTER NEW DESCRIPTION :  ")
    #                 self.description=str(__newone)
    #             elif __selector=='9':
    #                 __newone=input("\t\t\t|     ENTER TYPE OF PRESENTATION?     |\n\t\t\t| 1)FOR BUY AND SALE\n\t\t\t| Other)FOR MORTGAGE AND RENT ")            
    #                 if __newone=='1':
    #                     self.type_presentation="FOR BUY AND SELL"
    #                 else :
    #                     self.type_presentation="FOR MORTGAGE AND RENT"
    #             wait()
    #             print("\t\t\t|    GARDEN MODIFIED SUCCESSFULLY !    |")
    #             print("\t\t\t|     press any key to continue...     |")
    #             input("\t\t\t|______________________________________|")
    #             break
    #         except ValueError:
    #             cls()
    #             print("\n\n\t\t\tPLEASE TRY AGAIN!")
    #             hossein.sleep(1)

    # def __del__(area,address,price,description,type_presentation,water_period,type_garden,wall,bower):
    #     farming.__del__(area,adderss,price,description,type_presentation,water_period)
    #     self.type_garden = ''
    #     self.wall = False
    #     self.bower = False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class field(farming):
    def __init__(self,area,address,price,description,type_presentation,water_period,bower=False):
        farming.__init__(self,area,address,price,description,type_presentation,water_period)
        self.bower = bower

    # def showclass(self):
    #     print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
    #     print("WATER PERIOD : {}   BOWER : {}".format(self.water_period,self.bower))
    #     print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
    #     print("DESCRIPTION : {}".format(self.description))
    #     print("|___________________________________________________________________________________________|")

    # def editclass(self):
    #     while True:
    #         cls()
    #         print("\t\t\t ______________________________________")
    #         print("\t\t\t|   PLEASE SELECT BY NUMBER TO EDIT :  |")
    #         print("\t\t\t|   1) AREA          2) ADDRESS        |")
    #         print("\t\t\t|   3) PRICE         4) WATER PERIOD   |")
    #         print("\t\t\t|   5) BOWER         6) DESCRIPTION    |")
    #         print("\t\t\t|   7) TYPE OF PRESENTATION            |")
    #         __selector=input("\t\t\t|______________________________________|")
    #         try:
    #             if __selector=='1':
    #                 __newone=input("\t\t\t| ENTER NEW AREA : ")
    #                 self.area=int(__newone)
    #             elif __selector=='2':
    #                 __newone=input("\t\t\t| ENTER NEW ADDRESS : ")
    #                 self.address=str(__newone)
    #             elif __selector=='3':
    #                 __newone=input("\t\t\t| ENTER NEW PRICE : ")
    #                 self.price=int(__newone)
    #             elif __selector=='4':
    #                 __newone=input("\t\t\t| ENTER NEW WATER PERIOD : ")
    #                 self.water_period=int(__newone)
    #             elif __selector=='5':
    #                 __newone=input("\t\t\t| HAVE BOWER? 1)True Other)False ")
    #                 if __newone=='1':
    #                     self.bower=True
    #                 else :
    #                     self.bower=False
    #             elif __selector=='6':
    #                 __newone=input("\t\t\t| ENTER NEW DESCRIPTION :  ")
    #                 self.description=str(__newone)
    #             elif __selector=='7':
    #                 __newone=input("\t\t\t|     ENTER TYPE OF PRESENTATION?     |\n\t\t\t| 1)FOR BUY AND SALE\n\t\t\t| Other)FOR MORTGAGE AND RENT ")            
    #                 if __newone=='1':
    #                     self.type_presentation="FOR BUY AND SELL"
    #                 else :
    #                     self.type_presentation="FOR MORTGAGE AND RENT"
    #             wait()
    #             print("\t\t\t|     FIELD MODIFIED SUCCESSFULLY!    |")
    #             print("\t\t\t|     press any key to continue...     |")
    #             input("\t\t\t|______________________________________|")
    #             break
    #         except ValueError:
    #             cls()
    #             print("\n\n\t\t\tPLEASE TRY AGAIN!")
    #             hossein.sleep(1)
    
    # def __del__(self,area,address,price,description,type_presentation,water_period,bower):
    #     farming.__del__(self,area,adderss,price,description,type_presentation,water_period)
    #     self.bower = bower
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class building(estate):
    construction_year = 0
    def __init__(self,area,address,price,description,type_presentation,construction_year=0):
        estate.__init__(self,area,address,price,description,type_presentation)
        self.construction_year = construction_year

    # def __del__(self,area,address,price,description,type_presentation,construction_year):
    #     estate.__del__(self,area,address,price,description,type_presentation)
    #     self.construction_year = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class residential(building):
    def __init__(self,area,address,price,description,type_presentation,construction_year,residential_type,number_of_rooms,parking,des1,des2,des3):
        building.__init__(self,area,address,price,description,type_presentation,construction_year)
        self.residential_type = residential_type
        self.number_of_rooms = number_of_rooms
        self.parking = parking
        self.des1 = des1 #floor or yard
        self.des2 = des2 #unit or porch
        self.des3 = des3 #elevator or furnished

    # def showclass(self):
    #     print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
    #     print("CONSTRUCTION YEAR : {}   RESIDENTIAL TYPE : {}   NUMBER OF ROOMS : {}".format(self.construction_year,self.residential_type,self.number_of_rooms))
    #     if self.residential_type=='APARTMENT':
    #         print("FLOOR : {}   UNIT : {}   ELEVATOR : {}".format(self.des1,self.des2,self.des3))
    #     elif self.residential_type=='HOUSE' or self.residential_type=='VILLA':
    #         print("YARD : {}   PORCH : {}   FURNISHED : {}".format(self.des1,self.des2,self.des3))    
    #     print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
    #     print("DESCRIPTION : {}".format(self.description))
    #     print("|___________________________________________________________________________________________|")

    # def editclass(self):
    #     while True:
    #         cls()
    #         print("\t\t\t _______________________________________________")
    #         print("\t\t\t|      PLEASE SELECT BY NUMBER TO EDIT :        |")
    #         print("\t\t\t| 1) AREA               2) ADDRESS              |")
    #         print("\t\t\t| 3) PRICE              4) CONSTRUCTION YEAR    |")
    #         print("\t\t\t| 5) RESIDENTIAL TYPE   6) NUMBER OF ROOMS      |")
    #         print("\t\t\t| 7) DESCRIPTION        8) TYPE OF PRESENTATION |")
    #         if self.residential_type=='APARTMENT':
    #             print("\t\t\t| 9) FLOOR       10) UNIT         11) ELEVATOR  |")
    #         elif self.residential_type=='HOUSE' or self.residential_type=='VILLA':
    #             print("\t\t\t| 9) YARD        10) PORCH        11) FURNISHED |")
    #         __selector=input("\t\t\t|_______________________________________________|")
    #         try:
    #             if __selector=='1':
    #                 __newone=input("\t\t\t| ENTER NEW AREA : ")
    #                 self.area=int(__newone)
    #             elif __selector=='2':
    #                 __newone=input("\t\t\t| ENTER NEW ADDRESS : ")
    #                 self.address=str(__newone)
    #             elif __selector=='3':
    #                 __newone=input("\t\t\t| ENTER NEW PRICE : ")
    #                 self.price=int(__newone)
    #             elif __selector=='4':
    #                 __newone=input("\t\t\t| ENTER NEW CONSTRUCTION YEAR : ")
    #                 self.construction_year=int(__newone)
    #             elif __selector=='5':
    #                 __newone=input("\t\t\t| ENTER NEW RESIDENTIAL TYPE: 1)APARTMENT 2)HOUSE 3)VILLA ")
    #                 if __newone=='1':
    #                     __newone='APARTMENT'
    #                 elif __newone=='2':
    #                     __newone='HOUSE'
    #                 elif __newone=='3':
    #                     __newone='VILLA'
    #                 if self.residential_type != __newone :
    #                     self.residential_type=__newone
    #                     if __newone=='APARTMENT':
    #                         self.des1=int(input("\t\t\t| ENTER NEW FLOOR : "))
    #                         self.des2=int(input("\t\t\t| ENTER NEW UNIT : "))
    #                         __newone=input("\t\t\t| HAVE ELEVATOR? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des3=True
    #                         else :
    #                             self.des3=False
    #                     elif __newone=='HOUSE' or __newone=='VILLA':
    #                         __newone=input("\t\t\t| HAVE YARD? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des1=True
    #                         else :
    #                             self.des1=False
    #                         __newone=input("\t\t\t| HAVE PORCH? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des2=True
    #                         else :
    #                             self.des2=False
    #                         __newone=input("\t\t\t| HAVE FURNISHED? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des3=True
    #                         else :
    #                             self.des3=False
    #             elif __selector=='6':
    #                 __newone=input("\t\t\t| ENTER NEW NUMBER OF ROOMS : ")
    #                 self.number_of_rooms=int(__newone)
    #             elif __selector=='7':
    #                 __newone=input("\t\t\t| ENTER NEW DESCRIPTION :  ")
    #                 self.description=str(__newone)
    #             elif __selector=='8':
    #                 __newone=input("\t\t\t|     ENTER TYPE OF PRESENTATION?     |\n\t\t\t| 1)FOR BUY AND SALE\n\t\t\t| Other)FOR MORTGAGE AND RENT ")            
    #                 if __newone=='1':
    #                     self.type_presentation="FOR BUY AND SELL"
    #                 else :
    #                     self.type_presentation="FOR MORTGAGE AND RENT"
    #             elif __selector=='9':
    #                 if self.residential_type=='APARTMENT':
    #                     __newone=input("\t\t\t| ENTER NEW FLOOR : ")
    #                     self.des1=int(__newone)
    #                 elif self.residential_type=='HOUSE' or self.residential_type=='VILLA':
    #                     __newone=input("\t\t\t| HAVE YARD? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des1=True
    #                     else :
    #                         self.des1=False
    #             elif __selector=='10':
    #                 if self.residential_type=='APARTMENT':
    #                     __newone=input("\t\t\t| ENTER NEW UNIT : ")
    #                     self.des2=int(__newone)
    #                 elif self.residential_type=='HOUSE' or self.residential_type=='VILLA':
    #                     __newone=input("\t\t\t| HAVE PORCH? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des2=True
    #                     else :
    #                         self.des2=False
    #             elif __selector=='11':
    #                 if self.residential_type=='APARTMENT':
    #                     __newone=input("\t\t\t| HAVE ELEVATOR? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des3=True
    #                     else :
    #                         self.des3=False
    #                 elif self.residential_type=='HOUSE' or self.residential_type=='VILLA':
    #                     __newone=input("\t\t\t| HAVE FURNISHED? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des3=True
    #                     else :
    #                         self.des3=False
    #             wait()
    #             print("\t\t\t|  RESIDENTIAL MODIFIED SUCCESSFULLY!  |")
    #             print("\t\t\t|     press any key to continue...     |")
    #             input("\t\t\t|______________________________________|")
    #             break
    #         except ValueError:
    #             cls()
    #             print("\n\n\t\t\tPLEASE TRY AGAIN!")
    #             hossein.sleep(1)


    # def __del__(self,area,address,price,description,type_presentation,construction_year,residential_type,number_of_rooms,parking,des1,des2,des3):
    #     building.__del__(self,area,address,price,description,type_presentation,construction_year)
    #     self.number_of_rooms = 0
    #     self.parking = False
    #     self.residential_type = ''
    #     self.des1 = 0
    #     self.des2 = 0
    #     self.des3 = False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class commercial(building):
    def __init__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1=0,des2=0,des3=0,des4=0):
        building.__init__(self,area,address,price,description,type_presentation,construction_year)
        self.commercial_type = commercial_type
        self.des1 = des1 #number_of_rooms          or floor           or number of rooms
        self.des2 = des2 #Administrative document  or elevator        or Administrative document
        self.des3 = des3 #                         or storeroom       or
        self.des4 = des4 #                         or number of rooms or

    # def showclass(self):
    #     print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
    #     print("CONSTRUCTION YEAR : {}   COMMERCIAL TYPE : {}   ".format(self.construction_year,self.commercial_type))
    #     if self.commercial_type=='INDUSTRIAL' or self.commercial_type=='SHOP':
    #         print("NUMBER OF ROOMS : {}   ADMINISTRATIVE DOCUMENT: {}".format(self.des1,self.des2))
    #     elif self.commercial_type=='OFFICE':
    #         print("FLOOR : {}   ELEVATOR : {}   STOREROOM : {}   NUMBER OF ROOMS : {}".format(self.des1,self.des2,self.des3,self.des4)) 
    #     print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
    #     print("DESCRIPTION : {}".format(self.description))
    #     print("|___________________________________________________________________________________________|")

    # def editclass(self):
    #     while True:
    #         cls()
    #         print("\t\t\t _______________________________________________")
    #         print("\t\t\t|      PLEASE SELECT BY NUMBER TO EDIT :        |")
    #         print("\t\t\t| 1) AREA               2) ADDRESS              |")
    #         print("\t\t\t| 3) PRICE              4) CONSTRUCTION YEAR    |")
    #         print("\t\t\t| 5) COMMERCIAL TYPE    6) DESCRIPTION          |")
    #         print("\t\t\t| 7) TYPE OF PRESENTATION                       |")
    #         if self.commercial_type=='INDUSTRIAL' or self.commercial_type=='SHOP':
    #             print("\t\t\t| 8) NUMBER OF ROOMS  9) ADMINISTRATIVE DOCUMENT|")
    #         elif self.commercial_type=='OFFICE':
    #             print("\t\t\t| 8) FLOOR               9) ELEVATOR            |")
    #             print("\t\t\t|10) STOREROOM          11) NUMBER OF ROOMS     |")
    #         __selector=input("\t\t\t|_______________________________________________|")
    #         try:
    #             if __selector=='1':
    #                 __newone=input("\t\t\t| ENTER NEW AREA : ")
    #                 self.area=int(__newone)
    #             elif __selector=='2':
    #                 __newone=input("\t\t\t| ENTER NEW ADDRESS : ")
    #                 self.address=str(__newone)
    #             elif __selector=='3':
    #                 __newone=input("\t\t\t| ENTER NEW PRICE : ")
    #                 self.price=int(__newone)
    #             elif __selector=='4':
    #                 __newone=input("\t\t\t| ENTER NEW CONSTRUCTION YEAR : ")
    #                 self.construction_year=int(__newone)
    #             elif __selector=='5':
    #                 __newone=input("\t\t\t| ENTER NEW COMMERCIAL TYPE: 1)INDUSTRIAL 2)OFFICE 3)SHOP ")
    #                 if __newone=='1':
    #                     __newone='INDUSTRIAL'
    #                 elif __newone=='2':
    #                     __newone='OFFICE'
    #                 elif __newone=='3':
    #                     __newone='SHOP'
    #                 if self.commercial_type != __newone :
    #                     self.commercial_type=__newone
    #                     if __newone=='INDUSTRIAL' or __newone=='SHOP':
    #                         self.des1=int(input("\t\t\t| ENTER NEW NUMBER OF ROOMS : "))
    #                         __newone=input("\t\t\t| HAVE ADMINISTRATIVE DOCUMENT? 1)True Other)False ")
    #                         if __newone=='1':
    #                             self.des2=True
    #                         else :
    #                             self.des2=False
    #                     elif __newone=='OFFICE':
    #                         __newone=input("\t\t\t| ENTER NEW FLOOR : ")    
    #                         self.des1=int(__newone)
    #                         __newone=input("\t\t\t| HAVE ELEVATOR? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des2=True
    #                         else :
    #                             self.des2=False
    #                         __newone=input("\t\t\t| HAVE STOREROOM? 1)True Other)False ")    
    #                         if __newone=='1':
    #                             self.des3=True
    #                         else :
    #                             self.des3=False
    #                         __newone=input("\t\t\t| ENTER NEW NUMBER OF ROOMS : ")    
    #                         self.des4=int(__newone)
    #             elif __selector=='6':
    #                 __newone=input("\t\t\t| ENTER NEW DESCRIPTION :  ")
    #                 self.description=str(__newone)
    #             elif __selector=='7':
    #                 __newone=input("\t\t\t|     ENTER TYPE OF PRESENTATION?     |\n\t\t\t| 1)FOR BUY AND SALE\n\t\t\t| Other)FOR MORTGAGE AND RENT ")            
    #                 if __newone=='1':
    #                     self.type_presentation="FOR BUY AND SELL"
    #                 else :
    #                     self.type_presentation="FOR MORTGAGE AND RENT"
    #             elif __selector=='8':
    #                 if self.commercial_type=='INDUSTRIAL' or self.commercial_type=='SHOP':
    #                     __newone=input("\t\t\t| ENTER NEW NUMBER OF ROOMS : ")
    #                     self.des1=int(__newone)
    #                 elif self.commercial_type=='OFFICE':
    #                     __newone=input("\t\t\t| ENTER NEW FLOOR : ")
    #                     self.des1=__newone
    #             elif __selector=='9':
    #                 if self.commercial_type=='INDUSTRIAL' or self.commercial_type=='SHOP':
    #                     __newone=input("\t\t\t| HAVE ADMINISTRATIVE DOCUMENT? 1)True Other)Fase ")
    #                     if __newone=='1':
    #                         self.des2=True
    #                     else :
    #                         self.des2=False
    #                 elif self.commercial_type=='OFFICE':
    #                     __newone=input("\t\t\t| HAVE ELEVATOR? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des2=True
    #                     else :
    #                         self.des2=False
    #             elif __selector=='10' and self.commercial_type=='OFFICE':
    #                     __newone=input("\t\t\t| HAVE STOREROOM? 1)True Other)False ")
    #                     if __newone=='1':
    #                         self.des3=True
    #                     else :
    #                         self.des3=False
    #             elif __selector=='11' and self.commercial_type=='OFFICE':
    #                 __newone=input("\t\t\t| ENTER NUMBER OF ROOMS : ")
    #                 self.des4=int(__newone)        
    #             wait()
    #             print("\t\t\t|  COMMERCIAL MODIFIED SUCCESSFULLY !  |")
    #             print("\t\t\t|     press any key to continue...     |")
    #             input("\t\t\t|______________________________________|")
    #             break
    #         except ValueError:
    #             cls()
    #             print("\n\n\t\t\tPLEASE TRY AGAIN!")
    #             hossein.sleep(1)

    
    # def __del__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1,des2,des3,des4):
    #     building.__del__(self,area,address,price,description,type_presentation,construction_year)
    #     self.commercial_type=''
    #     self.des1 = 0
    #     self.des2 = 0 
    #     self.des3 = 0 
    #     self.des4 = 0 

#####################################################################################################################
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,800,400)
        self.setWindowTitle("ESTATE App")
        self.back = QImage("images/background.png")
        sImage = self.back.scaled(QSize(1400,720))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(sImage))                        
        self.setPalette(palette)
        screen = QGuiApplication.screenAt(QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())
        self.mainmenu=QVBoxLayout()
        self.UI()
        self.show()
        
    def UI(self):
        self.upmenu=QLabel('خوش آمدید\nلطفاً انتخاب کنید:\n')
        self.upmenu.setStyleSheet('font-size:20pt;font-family:Times Bold;')
        self.upmenu.setAlignment(Qt.AlignCenter)
        # self.addbutton=QPushButton('افزودن ملک',self)
        # self.addbutton.clicked.connect(self.adding)
        # self.showbutton=QPushButton('نمایش املاک (مرتب شده)',self)
        # self.editbutton=QPushButton('ویرایش املاک و  پروفایل ادمین',self)
        # self.searchbutton=QPushButton('جست و جو',self)
        self.comeinbutton=QPushButton('ورود',self)
        # self.comeinbutton.clicked.connect(self.comin)
        self.usbutton=QPushButton('درباره ی ما',self)
        self.usbutton.clicked.connect(self.aboutus)
        self.exitbutton=QPushButton('خروج',self)
        self.exitbutton.clicked.connect(self.exiting)
        # self.mainmenu.addWidget(self.upmenu)
        # self.mainmenu.addWidget(self.addbutton)
        # self.mainmenu.addWidget(self.showbutton)
        # self.mainmenu.addWidget(self.editbutton)
        self.mainmenu.addWidget(self.comeinbutton)
        self.mainmenu.addWidget(self.usbutton)
        self.mainmenu.addWidget(self.exitbutton)
        self.mainmenu.setContentsMargins(250,150,250,150)
        self.setStyleSheet('font-size: 14pt;font-family:Arial Bold;')
        # self.setStyleSheet('background-repeat: no-repeat; background-position: center;')
        self.setLayout(self.mainmenu)
        
    def aboutus(self):
        self.clearLayout(self.mainmenu)
        # self.about = QVBoxLayout()
        self.us = QLabel('برنامه ی مدیریت املاک\nکمپانی: MOJAAD\n تابستان 99')
        self.us.setAlignment(Qt.AlignCenter)
        self.goback = QPushButton('برگشت به صفحه ی اصلی',self)
        self.mainmenu.addWidget(self.us)
        self.mainmenu.addWidget(self.goback)
        self.mainmenu.setContentsMargins(250,150,250,150)
        self.setStyleSheet('font-size: 14pt;font-family:Arial Bold;')
        self.setLayout(self.mainmenu)
        self.goback.clicked.connect(self.call)
        
    def call(self): 
        self.clearLayout(self.mainmenu)
        self.UI()

    def exiting(self):
        result = QMessageBox.question(self,'Warning','از خروج مطمئن هستید؟',QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel , QMessageBox.Cancel,'font-size:12pt;')
        # QMessageBox.setStyleSheet('font-size:12pt;font-family:Times')
        if result == QMessageBox.Yes:
            sys.exit()

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


#####################################################################################################################
def main():
    # App1= QApplication(sys.argv)
    # image = QLabel()
    # movie = QMovie("images/welcome.gif")
    # image.setMovie(movie)
    # movie.start()
    # # image.setPixmap(QPixmap('images/home_graphic.jpg'))
    # image.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    # image.move(585,350)
    # image.show()
    # sleep(3)
    # image.close()
    App2 = QApplication(sys.argv)
    Window = window()
    sys.exit(App2.exec_())

if __name__ == '__main__':
    main()
#####################################################################################################################

