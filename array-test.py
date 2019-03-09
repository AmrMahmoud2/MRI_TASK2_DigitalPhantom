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

# class MRI(QDialog):
#     def __init__(self):
#         super(MRI,self).__init__()
#         loadUi('MRI-Phantom.ui',self)
#         self.setWindowTitle('MRI-Phantom')
#         self.b1.clicked.connect(self.on_click)
#
#     def on_click(self):
#             try:
#                 name = QFileDialog()  # class provides a dialog that allow users to select files or directories
#                 imgPath = name.getOpenFileName(self, 'open file', '','Image files (*.jpg *.png *.jpeg)')  # displays the contents of the "/home/jana" directory, and displays files matching the patterns given in the string
#                 self.checkimage(imgPath[0])  # Provides 2D context for shapes on a Canvas item
#             except:
#                 QMessageBox.about(self, "Error", "Sorry That is not an image")
#
#     def checkimage(self,path):
#         im = Image.open(path) # Open an image file
#         width, height = im.size
#         if width != 225 or height != 225:
#             print('invalid pic')
#             QMessageBox.about(self,"Error","Wrong Image Size")
#         else:
#
#              self.path = path
#              self.openimage(path) #void Function to display img on the GUI Label
#
#     def openimage(self,imagePath):
#         pixmap = QPixmap(imagePath) #QPixmap is designed and optimized for showing images on screen
#         pixmap = pixmap.scaled(self.l1.width(), self.l1.height(), QtCore.Qt.KeepAspectRatio)
#         self.l1.setPixmap(pixmap)


def Construct3DArray (Array2d):
    d1 = [[[1 for col in range(4)]for row in range(len(Array2d))] for x in range(len(Array2d))]
    for x in range(len(d1)):
        for y in range(len(d1)):
            d1[x][y][0] = Array2d[x][y]
        #print(d1[x])
    return d1

def Return (original_array,index):
    d2=np.empty((len(original_array),len(original_array)))
   #print(original_array.shape)
    for l in range(len(original_array)):
        for m in range(len(original_array)):
          d2[l][m]=original_array[l][m][index]
        return d2



a = np.array([[49, 49, 12, 90, 42, 13, 12, 12, 12, 3],
              [91, 58, 92, 16, 78, 13, 12, 12, 12, 3],
              [97, 19, 58, 84, 84, 13, 12, 12, 12, 3],
              [86, 31, 80, 78, 69, 13, 12, 12, 12, 3],
              [29, 95, 38, 51, 92, 13, 12, 12, 12, 3],
              [29, 95, 38, 51, 92, 13, 12, 12, 12, 3],
              [29, 95, 38, 51, 101, 13, 12, 12, 12,3],
              [29, 95, 38, 51, 92, 13, 12, 12, 12, 3],
              [29, 95, 38, 51, 92, 13, 12, 12, 12, 3],
              [29, 95, 38, 51, 92, 13, 12, 12, 12, 3]])

b=np.array(Construct3DArray(a))
# u=removeDuplicates(b)
# for x in range(len(u)):
#   print(u[x])
# print("unique")
# for x in range(len(b)):
#     print(b[x])
# print("sorted")
# c=sorted(b, key=lambda b: b[1],reverse=True)
# #c=np.sort(b, axis=0)
# for x in range(len(c)):
#     print(c[x])

print(b.shape[2])
print(len(b))
#c=np.array((removeDuplicates(a)))
c=np.unique(a)
print(c)


# def main():
#     app = QApplication(sys.argv)
#     widget = MRI()
#     widget.show()
#     sys.exit(app.exec_())
# main()



#not working

# def removeDuplicates(listofElements):
#     # Create an empty list to store unique elements
#     uniqueList=np.empty((len(listofElements),len(listofElements)))
#
#     # Iterate over the original list and for each element
#     # add it to uniqueList, if its not already there.
#     for x in range(len(listofElements)):
#         for y in range(len(listofElements)):
#              if ((listofElements[x][y] not in uniqueList[:])):
#                 uniqueList[x]=listofElements[x][y]
#     return uniqueList