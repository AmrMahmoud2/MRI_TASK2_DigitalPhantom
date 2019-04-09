
import sys
from copy import deepcopy

from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QSizePolicy, QVBoxLayout, QSizePolicy,QDockWidget,QMainWindow,QScroller
from PIL import Image
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget
from qimage2ndarray import gray2qimage
import sys
import numpy as np
from tomophantom import TomoP2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pyqtgraph as pg
import collections
import random
import time
import math

bg_color = 'black'
fg_color = 'white'



class MRI(QMainWindow ):
    def __init__(self):
        super(MRI,self).__init__()
        loadUi('MRI-Phantom.ui',self)
        self.setWindowTitle('MRI-Phantom')
        #self.b1.clicked.connect(self.on_click)
        self.cb.activated[str].connect(self.temp_var)
        self.GraphicsView()
        # self.r=255
        # self.g=0
        # self.b=0
        self.colors =self.get_spaced_colors(5)
        print(self.colors)
        self.i=0



        #self.setAcceptHoverEvents(True)



    @pyqtSlot()
    #browse Btn
    # def on_click(self):
    #     array=self.Phantom()
    #     img=self.convertArrayToImage(array)
    #     self.ShowImage(img)
    #     self.setTime(img)





    def temp_var(self):
        cur_txt = self.cb.currentText()
        self.num, ok = QInputDialog.getInt(self, "integer input dialog", "enter a number")
        if cur_txt == "Shepp-Logan phantom" and self.num!=0 and ok :
            self.Display(2,self.num)
        else:
            self.l1.hide()










    def Display(self,model_no,size):
        array = self.Phantom(model_no, size)
        self.img = self.convertArrayToImage(array)
        self.img.save('img.png')
        qimage = ImageQt(self.img)
        pixmap = QPixmap.fromImage(qimage)
        self.pixmap = QPixmap(pixmap)
        pixmap = self.pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
        self.l1.setPixmap(pixmap)
        # Mouse Event
        self.l1.mouseDoubleClickEvent = self.getPixel
        self.l1.mouseMoveEvent=self.mouseMoveEvent
        self.l1.paintEvent = self.paintEvent
        self.l1.mousePressEvent = self.getpixels
        self.i = 1


        #self.l1.mousePressEvent=self.wheelEvent
        array_with_time = self.setTime(self.img)
        # construct t1 image
        self.array_t1 = self.Return(array_with_time, 1)
        img_t1 = self.convertArrayToImage(self.array_t1)
        pixmap_t1 = self.ShowImage(img_t1)
        self.l2.setPixmap(pixmap_t1)
        # construct t2 image
        self.array_t2 = self.Return(array_with_time, 2)
        img_t2 = self.convertArrayToImage(self.array_t2)
        pixmap_t2 = self.ShowImage(img_t2)
        self.l3.setPixmap(pixmap_t2)
        # I = np.dstack([img, img, img])
        # x = 73
        # y = 75
        # I[x, y, :] = [255, 128, 0]
        # highlight_img= Image.fromarray(I).convert('RGB')
        # pixmap_test=self.ShowImage(highlight_img)
        # self.l2.setPixmap(pixmap_test)
        K_array=self.K_Space()
        img_K = self.convertArrayToImage(K_array)
        pixmap_k = self.ShowImage(img_K)
        self.l4.setPixmap(pixmap_k)



    def Phantom(self,model,size):
     model =model
     sizeN = size
     #This will generate 256x256 phantom from the model
     self.phantom = TomoP2D.Model(model, sizeN,'/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
     angles_num = int(0.5*np.pi*sizeN) # angles number
     angles = np.linspace(0,180,angles_num,dtype='float32')
     angles_rad = angles*(np.pi/180)
     P = int(np.sqrt(2)*sizeN) #detectors
     #This will generate a sinogram of the model
     sino_an = TomoP2D.ModelSino(model, sizeN, P, angles, '/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
     # pp = {'Obj': TomoP2D.Objects2D.RECTANGLE,
     #       'C0': 9.00,
     #       'x0': 0.3,
     #       'y0': -0.25,
     #       'a': 0.5,
     #       'b': 0.8,
     #       'phi': 90.0}
     # G=TomoP2D.Object(256, pp)
     return self.phantom

    def convertArrayToImage(self, arr):
        # to get rid of dividing bt zero
        # min_nonzero = np.min(arr[np.nonzero(arr)])
        # arr[arr == 0] = min_nonzero

        img = np.abs(20 * np.log(arr))
        img_back = Image.fromarray(img).convert('L')
        return img_back


    def convertImageToArray(self,img):
         arr = np.asarray(img)
         print('this is image pixel function')
         return arr

    def ShowImage(self, img):
     qimage = ImageQt(img)
     pixmap = QPixmap.fromImage(qimage)
     pixmap = QPixmap(pixmap)
     pixmap = pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
     return pixmap

    def Construct3DArray(self,Array2d,index):
        d1 = [[[1 for col in range(4)] for row in range(len(Array2d))] for x in range(len(Array2d))]
        for x in range(len(d1)):
            for y in range(len(d1)):
                d1[x][y][index] = Array2d[x][y]
            # print(d1[x])
        return d1

    def Set_T1(self,Array_3d,Max_value,Min_Value):
        for x in range(len(Array_3d)):
            for y in range(len(Array_3d)):
                if (Array_3d[x][y][0]==Max_value) :
                    Array_3d[x][y][1]=4250
                else:
                    if (Array_3d[x][y][0]==Min_Value):
                        Array_3d[x][y][1]=250
                    else:
                        Array_3d[x][y][1]=int(250+((Array_3d[x][y][0]*4000)/Max_value))
        return Array_3d

    def setTime(self,image):
        Pixels_Array = np.asarray(image)
        self.Pixels_Array_Filterd=self.Filters(Pixels_Array,255)
        Unique_Pixels_values= np.unique(Pixels_Array)
        Max_value=np.max(Unique_Pixels_values)
        Min_Value=np.min(Unique_Pixels_values)
        Array_3d_With_intensity=self.Construct3DArray(Pixels_Array,0)
        Array_3d_With_T1=self.Set_T1(Array_3d_With_intensity,Max_value,Min_Value)
        Array_3d_With_T2 = self.Set_T2(Array_3d_With_T1, Max_value, Min_Value)
        return (Array_3d_With_T2)


    def Set_T2(self,Array_3d,Max_value,Min_Value):
        for x in range(len(Array_3d)):
            for y in range(len(Array_3d)):
                if (Array_3d[x][y][0] ==Max_value) :
                    Array_3d[x][y][2]=2000
                else:
                    if (Array_3d[x][y][0]==Min_Value):
                        Array_3d[x][y][2]=5
                    else:
                        Array_3d[x][y][2]=int(5+((Array_3d[x][y][0]*2000)/Max_value))
        return Array_3d

    def Return(self,original_array, index):
        d2 = np.empty((len(original_array), len(original_array)))
        # print(original_array.shape)
        for l in range(len(original_array)):
            for m in range(len(original_array)):
                d2[l][m] = original_array[l][m][index]
        return d2

    def getPixel (self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        print('real x, y',self.x, self.y)
        print("width",self.l1.width())
        print("width", self.l1.height())
        #mapping for painting
        self.xratio = self.num / self.l1.width()
        self.yratio = self.num / self.l1.height()
        self.x_map= self.xratio * self.x
        self.y_map = self.yratio * self.y
        self.x_paint = self.x_map
        self.y_paint = self.y_map
        self.x_T = int(self.x_map)
        self.y_T = int(self.y_map)
        # #mapping for time
        # if(self.x>=self.num):
        #     self.x_T = int(self.xratio * self.x)
        # else:
        #     self.x_T=self.x
        #
        # if (self.y >= self.num):
        #       self.y_T = int(self.yratio * self.y)
        # else:
        #     self.y_T = self.y


        print('paint x, y', self.x_paint, self.y_paint)

        print("time index",self.x_T,self.y_T)
        print("t1",self.array_t1[self.y_T][self.x_T])
        print("t2",self.array_t2[self.y_T][self.x_T])
        print("after ratio)",self.x,self.y)
        if(self.i<5):
          self.plotting(self.array_t1[self.y_T][self.x_T],self.array_t2[self.y_T][self.x_T])
          self.tabWidget.setCurrentIndex(1)
          self.Paint()



    def getpixels (self,event):
            self.x_single = event.pos().x()
            self.y_single = event.pos().y()
            print('single', self.x_single, self.y_single)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if x in range(self.x_single - 10, self.x_single + 10) and y < self.y_single and y > 0 :
            self.i = self.i + 0.1
            self.Enhancer(self.i)
        elif x in range(self.x_single - 10, self.x_single + 10) and y> self.y_single and y< self.l1.height():
            self.i = self.i - 0.1
            self.Enhancer(self.i)


    def Enhancer(self,i):
        enhancer = ImageEnhance.Brightness(self.img)
        self.enhanced_im = enhancer.enhance(self.i)
        qimage = ImageQt(self.enhanced_im)
        pixmap = QPixmap.fromImage(qimage)
        self.pixmap = QPixmap(pixmap)
        #pixmap = self.pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
        self.l1.setPixmap(pixmap)


        print(self.i)
        # elif self.yy in range(y - 10, y + 10) and self.xx > x:
        #     self.j = self.j + 10
        # elif self.yy in range(y - 10, y + 10) and self.xx < x:
        #     self.j = self.j - 10

        #text = "x: {0},  y: {1}".format(x, y)
        #print(text)

    def plotting(self,T1,T2):
        # define the data
        self.x = np.linspace(0, 1000, 400)
        self.x2 = np.linspace(0, 1000, 400)
        self.y = 1 - np.exp((-self.x) / T1)
        self.y2 = np.exp((-self.x2) / T2)
        # plot
        self.c = self.plt.plot(self.x, self.y, pen=self.colors[self.i], name=('pixel'))
        self.c2 = self.plt2.plot(self.x2, self.y2, pen=self.colors[self.i], name='pixel')
        self.i=self.i+1
    def get_spaced_colors(self,n):
        max_value = 16581375  # 255**3
        interval = int(max_value / n)
        colors = [hex(I)[2:].zfill(6) for I in range(200, max_value, interval)]

        return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]


    def Paint(self):
        #trial 1
        # draw = ImageDraw.Draw(img)
        # print("x,y",type(x),type(y),x,y)
        # if(x>self.num):
        #
        #     x=int(self.ratio*x)
        #
        # if (y > self.num):
        #     y = int(self.ratio * y)
        #
        # draw.rectangle(((x-2, y++-2), (x+2, y+2)), outline="#ff8888")
        # del draw
        # self.pixmap = self.ShowImage(img)
        # self.l1.setPixmap(self.pixmap)
        #trial 2
        # QApplication.processEvents()
        # self.painterInstance = QPainter(self.pixmap)  # b3mel opject
        # self.painterInstance.begin(self)
        # self.penRectangle = QPen(QtCore.Qt.red)  # yehdd el elon
        # self.penRectangle.setWidth(1)
        # self.penPoint = QPen(QtCore.Qt.blue)
        # self.penPoint.setWidth(1)  #
        # self.painterInstance.setPen(self.penPoint)  # apply el lon
        # self.painterInstance.drawRect(self.y_test, self.x_test, 1, 1)
        # self.painterInstance.setPen(self.penRectangle)
        # self.painterInstance.drawRect(self.y_test-1, self.x_test-1, 2, 2)
        # self.painterInstance.end()
        # print(self.x_test,self.y_test)
        # result =self.pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)  # scale 3la elabel
        # self.l1.setPixmap(result)
        # self.painterInstance.end()
        #trial3
        QApplication.processEvents()
        # convert image file into pixmap
        #self.pixmap_image = QtGui.QPixmap('img.png')

        # create painter instance with pixmap

        self.painterInstance = QtGui.QPainter(self.pixmap)
        self.painterInstance.begin(self)

        # set rectangle color and thickness
        self.penRectangle = QtGui.QPen(QtCore.Qt.green)
        self.penRectangle.setWidth(1)
        self.penPoint = QtGui.QPen(QtCore.Qt.blue)
        self.penRectangle.setWidth(1)
        self.painterInstance.setPen(self.penPoint)
        self.painterInstance.drawPoint(int(self.x_paint), int(self.y_paint))


        # draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(self.x_paint-2.5, self.y_paint-2.5, 5, 5)
        print("test",self.x_paint,self.y_paint)
        # set pixmap onto the label widget

        pixmap_image = self.pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
        self.l1.setPixmap(pixmap_image)
        self.l1.show()
        self.painterInstance.end()

    def GraphicsView (self):
        # create plot
        self.plt = pg.PlotItem()
        self.plt2 = pg.PlotItem()
        self.plt.showGrid(x=True, y=True)
        self.plt.addLegend()
        self.plt2.showGrid(x=True, y=True)
        self.plt2.addLegend()

        # set properties
        self.plt.setLabel('left', 'Value', units='MZ')
        self.plt.setLabel('bottom', 'Time', units='s')
        self.plt.setTitle('T1 Recovery')
        self.plt2.setLabel('left', 'Value', units='MZ')
        self.plt2.setLabel('bottom', 'Time', units='s')
        self.plt2.setTitle('T2 Decay')

        # set Graphics View

        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView.setCentralItem(self.plt)
        self.graphicsView_2.setCentralItem(self.plt2)




    def K_Space(self):


        tr = 3*np.average(self.array_t1)
        te = 150
        k_space = np.zeros((30, 30), dtype=np.complex)

        signal = np.ones(30)*np.sin(45*(np.pi/180))

        for kspacerow in range(30):

            signal = signal * np.exp(-te / self.array_t2)

            for kspacecol in range(30):
                GX = 2 * np.pi * kspacerow / 30
                GY = 2 * np.pi * kspacecol / 30

                for i in range(30):
                    for j in range(30):
                        total_theta = (GX * i + GY * j)
                        k_space[kspacerow, kspacecol] += signal[i, j] * np.exp(-1j * total_theta)

            signal = 1 - np.exp(-tr / self.array_t1)

        test1 = np.absolute(np.fft.ifft2(k_space))
        return test1



    def Filters(self, array, value):
        for i in range(len(array)):
            for j in range(len(array)):
                if (array[i][j] == value).all():
                    array2 = np.delete(array, array[i][j])
        return array2





























def main():
     app = QApplication(sys.argv)
     widget = MRI()
     widget.show()
     sys.exit(app.exec_())
main()