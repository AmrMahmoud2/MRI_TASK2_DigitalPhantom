
import sys
from copy import deepcopy

from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QSizePolicy, QVBoxLayout, QSizePolicy,QDockWidget,QMainWindow
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
        loadUi('MRI-Phantom2.ui',self)
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
        if cur_txt == "Shepp-Logan phantom":
            self.Display(14,self.l1.width())
        else:
            self.l1.hide()










    def Display(self,model_no,size):
        array = self.Phantom(model_no, size)
        self.img = self.convertArrayToImage(array)
        pixmap = self.ShowImage(self.img)
        self.l1.setPixmap(pixmap)
        # Mouse Event
        self.l1.mousePressEvent = self.getPixel
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
        print(self.l1.width())
        # I = np.dstack([img, img, img])
        # x = 73
        # y = 75
        # I[x, y, :] = [255, 128, 0]
        # highlight_img= Image.fromarray(I).convert('RGB')
        # pixmap_test=self.ShowImage(highlight_img)
        # self.l2.setPixmap(pixmap_test)


    def Phantom(self,model,size):
     model =model
     sizeN = 256
     #This will generate 256x256 phantom from the model
     self.phantom = TomoP2D.Model(model, sizeN,'/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
     angles_num = int(0.5*np.pi*sizeN) # angles number
     angles = np.linspace(0,180,angles_num,dtype='float32')
     angles_rad = angles*(np.pi/180)
     P = int(np.sqrt(2)*sizeN) #detectors
     #This will generate a sinogram of the model
     sino_an = TomoP2D.ModelSino(model, sizeN, P, angles, '/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
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
                if (Array_3d[x][y][0] ==Max_value) :
                    Array_3d[x][y][1]=1090
                else:
                    if (Array_3d[x][y][0]==Min_Value):
                        Array_3d[x][y][1]=0
                    else:
                        Array_3d[x][y][1]=int(0+(Array_3d[x][y][0]*1090)/Max_value)
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
                    Array_3d[x][y][2]=0
                else:
                    if (Array_3d[x][y][0]==Min_Value):
                        Array_3d[x][y][2]=1090
                    else:
                        Array_3d[x][y][2]=int(1090-((Array_3d[x][y][0]*1090)/Max_value))
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
        print('before',self.x, self.y)
        self.ratio = 256 / self.l1.width()
        if(self.x>256):

            self.x=int(self.ratio*self.x)

        if (self.y > 256):
            self.y = int(self.ratio * self.y)

        print("t1",self.array_t1[self.y][self.x])
        print("t2",self.array_t2[self.y][self.x])
        print(self.x,self.y)
        if(self.i<5):
          self.plotting(self.array_t1[self.y][self.x],self.array_t2[self.y][self.x])
          self.tabWidget.setCurrentIndex(1)
        print(self.l1.width())


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