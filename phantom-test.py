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
        self.b1.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        array=self.Phantom()
        img=self.convertArrayToImage(array)
        self.ShowImage(img)


    def Phantom(self):
     model = 13
     sizeN = 256
     #This will generate 256x256 phantom from model no.1
     self.phantom = TomoP2D.Model(model, sizeN,'/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
     angles_num = int(0.5*np.pi*sizeN) # angles number
     angles = np.linspace(0,180,angles_num,dtype='float32')
     angles_rad = angles*(np.pi/180)
     P = int(np.sqrt(2)*sizeN) #detectors
     #This will generate a sinogram of model no.1
     sino_an = TomoP2D.ModelSino(model, sizeN, P, angles, '/home/sohila/Documents/BIO-MATERIALS/Third-Year/Second-Term/MRI/Task2-MRI/phantoms/TomoPhantom/PhantomLibrary/models/Phantom2DLibrary.dat')
     return self.phantom

    def ShowImage(self, img):
     qimage = ImageQt(img)
     pixmap = QPixmap.fromImage(qimage)
     pixmap = QPixmap(pixmap)
     pixmap = pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
     self.l1.setPixmap(pixmap)

    def convertArrayToImage(self,arr):
        #img = gray2qimage(arr)
        #min_nonzero = np.min(arr[np.nonzero(arr)])
        #arr[arr == 0] = min_nonzero
        img = np.abs(20*np.log(arr))
        img_back = Image.fromarray(img).convert('RGB')
        return img_back

def main():
     app = QApplication(sys.argv)
     widget = MRI()
     widget.show()
     sys.exit(app.exec_())
main()