import sys
from copy import deepcopy

from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QInputDialog,QFileDialog,QMessageBox
from PIL import Image
import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qimage2ndarray import gray2qimage
import time
import sys
import numpy as np
from tomophantom import TomoP2D

class MRI(QDialog):
    def __init__(self):
        super(MRI,self).__init__()
        loadUi('MRI-Phantom.ui',self)
        self.setWindowTitle('MRI-Phantom')
        #self.b1.clicked.connect(self.on_click)
        self.cb.activated[str].connect(self.temp_var)

    @pyqtSlot()
    #browse Btn
    # def on_click(self):
    #     array=self.Phantom()
    #     img=self.convertArrayToImage(array)
    #     self.ShowImage(img)
    #     self.setTime(img)

    def temp_var(self, text):
        cur_txt = text
        if cur_txt == 'Shepp-Logan phantom':
            self.Display(1)
        else:
            self.l1.hide()

    def Display(self,model_no):
        array = self.Phantom(model_no)
        img = self.convertArrayToImage(array)
        self.ShowImage(img)
        self.setTime(img)


    def Phantom(self,model):
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

    def ShowImage(self, img):
     qimage = ImageQt(img)
     pixmap = QPixmap.fromImage(qimage)
     pixmap = QPixmap(pixmap)
     pixmap = pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
     self.l1.setPixmap(pixmap)

    def convertArrayToImage(self,arr):
        #to get rid of dividing bt zero
        # min_nonzero = np.min(arr[np.nonzero(arr)])
        # arr[arr == 0] = min_nonzero

        img = np.abs(20*np.log(arr))
        img_back = Image.fromarray(img).convert('L')
        return img_back

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
                        Array_3d[x][y][1]=787
                    else:
                        Array_3d[x][y][1]=int(1090-(Array_3d[x][y][0]*((1090-787)/Max_value)))
        return Array_3d

    def Set_T2(self,Array_3d,Max_value,Min_Value):
        for x in range(len(Array_3d)):
            for y in range(len(Array_3d)):
                if (Array_3d[x][y][0] ==Max_value) :
                    Array_3d[x][y][2]=113
                else:
                    if (Array_3d[x][y][0]==Min_Value):
                        Array_3d[x][y][2]=121
                    else:
                        Array_3d[x][y][1]=int(121-(Array_3d[x][y][0]*((121-113)/Max_value)))
        return Array_3d


    def setTime(self,image):
        Pixels_Array = np.asarray(image)
        Unique_Pixels_values= np.unique(Pixels_Array)
        Max_value=np.max(Unique_Pixels_values)
        Min_Value=np.min(Unique_Pixels_values)
        Array_3d_With_intensity=self.Construct3DArray(Pixels_Array,0)
        Array_3d_With_T1=self.Set_T1(Array_3d_With_intensity,Max_value,Min_Value)
        Array_3d_With_T2 = self.Set_T2(Array_3d_With_T1, Max_value, Min_Value)
        print(Array_3d_With_T2)








def main():
     app = QApplication(sys.argv)
     widget = MRI()
     widget.show()
     sys.exit(app.exec_())
main()