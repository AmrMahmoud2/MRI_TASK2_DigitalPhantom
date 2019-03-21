
import sys
from copy import deepcopy

from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QSizePolicy,QVBoxLayout, QSizePolicy
from PIL import Image
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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



class MRI(QDialog):
    def __init__(self):
        super(MRI,self).__init__()
        loadUi('MRI-Phantom.ui',self)
        self.setWindowTitle('MRI-Phantom')
        #self.b1.clicked.connect(self.on_click)
        self.cb.activated[str].connect(self.temp_var)
        #self.graphicsView = pg.PlotWidget()
        #self.m = PlotCanvas(self, width=15, height=6)
        #self.m.move(168, 410)
        self.m=DynamicPlotter(sampleinterval=0.05, timewindow=20.)

        self.current_width=self.l1.width()
        #self.setAcceptHoverEvents(True)



    @pyqtSlot()
    #browse Btn
    # def on_click(self):
    #     array=self.Phantom()
    #     img=self.convertArrayToImage(array)
    #     self.ShowImage(img)
    #     self.setTime(img)



    def Display(self,model_no,size):
        array = self.Phantom(model_no,size)
        img = self.convertArrayToImage(array)
        pixmap=self.ShowImage(img)
        self.l1.setPixmap(pixmap)
        #Mouse Event
        self.l1.mousePressEvent = self.getPixel
        array_with_time=self.setTime(img)
        # construct t1 image
        self.array_t1=self.Return(array_with_time,1)
        img_t1=self.convertArrayToImage(self.array_t1)
        pixmap_t1=self.ShowImage(img_t1)
        #self.l2.setPixmap(pixmap_t1)
        #construct t2 image
        self.array_t2 = self.Return(array_with_time, 2)
        img_t2 = self.convertArrayToImage(self.array_t2)
        pixmap_t2 = self.ShowImage(img_t2)
        self.l3.setPixmap(pixmap_t2)
        #highlight trial
        # highlight_arry=self.convertImageToArray(img)
        # highlight_img_RGB = Image.fromarray(highlight_arry).convert('RGB')
        # test_array=self.convertImageToArray(highlight_img_RGB)
        # test_array=np.array(test_array)
        # test_array[:, :3] = [255, 128, 0]
        # highlight_img=self.convertArrayToImage(test_array)
        # pixmap_test=self.ShowImage(highlight_img)
        # self.l3_2.setPixmap(pixmap_test)
        I = np.dstack([img, img, img])
        x = 73
        y = 75
        I[x, y, :] = [255, 128, 0]
        highlight_img= Image.fromarray(I).convert('RGB')
        pixmap_test=self.ShowImage(highlight_img)
        self.l2.setPixmap(pixmap_test)











    def temp_var(self):
        cur_txt = self.cb.currentText()
        if cur_txt == "Shepp-Logan phantom":
            self.Display(14,self.current_width)
        else:
            self.l1.hide()

    def Phantom(self,model,size):
     model =model
     sizeN = 1080
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
        if self.current_width != self.l1.width():
            self.current_width = self.l1.width()
            self.Display(14,self.current_width)
        self.x = event.pos().x()
        self.y = event.pos().y()
        print("t1",self.array_t1[self.y][self.x])
        print("t2",self.array_t2[self.y][self.x])
        print(self.x,self.y)
        # plotting
        #self.m.plot(self.array_t1[self.y][self.x], self.array_t2[self.y][self.x])
        print(self.l1.width())
    #
    # def hoverEnterEvent(self, event):
    #     self.setBrush(Qt.yellow)
    #     QDialog.hoverEnterEvent(self, event)






    def Filters(self, array, value):
        for i in range(len(array)):
            for j in range(len(array)):
                if (array[i][j] == value).all():
                    array2 = np.delete(array, array[i][j])
        return array2


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=5, dpi=50):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor='black')


        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.parentWindow = parent

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def plot(self,T1,T2):
         #T1 plotting
         fig = plt.figure(facecolor=bg_color, edgecolor=fg_color)

         x = np.linspace(0, 10000, 100)
         y = 1.5*(1-(np.exp((-x)/T1)))
         ax = self.figure.add_subplot(121)
         ax.patch.set_facecolor(bg_color)
         ax.xaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
         ax.yaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
         for spine in ax.spines.values():
             spine.set_color(fg_color)
         ax.plot(x, y,'cyan', axes=ax)
         plt.xlabel('Time', color=fg_color)
         plt.ylabel('T1', color=fg_color)
         ax.set_title('T1',color=fg_color)
         #T2 Plotting
         x2 = np.linspace(0, 10000, 100)
         y2 = 1.5*(np.exp((-x2)/T2))
         ax2 = self.figure.add_subplot(122)
         ax2.patch.set_facecolor(bg_color)
         ax2.xaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
         ax2.yaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
         for spine in ax2.spines.values():
             spine.set_color(fg_color)
         ax2.plot(x2, y2)
         plt.xlabel('Time', color=fg_color)
         plt.ylabel('T2', color=fg_color)

         ax2.set_title('T2',color=fg_color)
         self.draw()


class DynamicPlotter():

    def __init__(self, sampleinterval=1, timewindow=100., size=(600,350)):
        # Data stuff
        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
        self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.x = np.linspace(timewindow, 0.0, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)

        # PyQtGraph stuff
        self.app = QtGui.QApplication([])
        self.window=pg.GraphicsWindow(title="Basic plotting examples")
        self.window.resizeEvent(size)
        self.plt = self.window.addPlot(title="Basic array plotting")
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
        self.curve = self.plt.plot(self.x, self.y, pen=(255, 0, 0))
        ##plt2
        self.plt2 = self.window.addPlot(title="Multiple curves")
        self.plt2.showGrid(x=True, y=True)
        self.plt2.setLabel('left', 'amplitude', 'V')
        self.plt2.setLabel('bottom', 'time', 's')
        self.curve2 = self.plt2.plot(self.x, self.y, pen=(255, 0, 0))
        self.curve2 = self.plt2.plot(self.x, self.y, pen=(255, 0, 0))



        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)

    def getdata(self):
        frequency = 0.5
        noise = random.normalvariate(0., 1.)
        new = 10.*math.tan(time.time()*frequency*2*math.pi) + noise
        return new

    def updateplot(self):
        self.databuffer.append( self.getdata() )
        self.y[:] = self.databuffer
        self.curve.setData(self.x, self.y)
        self.curve2.setData(self.x, self.y)
        self.app.processEvents()




















def main():
     app = QApplication(sys.argv)
     widget = MRI()
     widget.show()
     sys.exit(app.exec_())
main()