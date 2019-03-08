import sys
from copy import deepcopy
from PyQt5.QtWidgets import QInputDialog,QFileDialog,QMessageBox
from PIL import Image
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qimage2ndarray import gray2qimage
import time

class MRI(QDialog):
    def __init__(self):
        super(MRI,self).__init__()
        loadUi('MRI-Phantom.ui',self)
        self.setWindowTitle('MRI-Phantom')
        self.b1.clicked.connect(self.on_click)

    def on_click(self):
            try:
                name = QFileDialog()  # class provides a dialog that allow users to select files or directories
                imgPath = name.getOpenFileName(self, 'open file', '','Image files (*.jpg *.png *.jpeg)')  # displays the contents of the "/home/jana" directory, and displays files matching the patterns given in the string
                self.checkimage(imgPath[0])  # Provides 2D context for shapes on a Canvas item
            except:
                QMessageBox.about(self, "Error", "Sorry That is not an image")

    def checkimage(self,path):
        im = Image.open(path) # Open an image file
        width, height = im.size
        if width != 225 or height != 225:
            print('invalid pic')
            QMessageBox.about(self,"Error","Wrong Image Size")
        else:

             self.path = path
             self.openimage(path) #void Function to display img on the GUI Label

    def openimage(self,imagePath):
        pixmap = QPixmap(imagePath) #QPixmap is designed and optimized for showing images on screen
        pixmap = pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
        self.l1.setPixmap(pixmap)

    def Construct3DArray (Array2d):
       d1 = [[[1 for col in range(3)]for row in range(6)] for x in range(6)]
       for x in range(len(d1)):
           for y in range(6):
              d1[x][y][0] = 1
              d1[x][y][1] = 2
              d1[x][y][2] = 3
       print(d1[x])

    def Return (original_array,index):
      d2=np.empty((len(original_array),len(original_array)))
       #print(original_array.shape)
      for l in range(len(original_array)):
        for m in range(len(original_array)):
          d2[l][m]=original_array[l][m][index]
        return d2



def main():
    app = QApplication(sys.argv)
    widget = MRI()
    widget.show()
    sys.exit(app.exec_())
main()