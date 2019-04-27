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


cpdef  K_Space(tr, te,theta,num,array_t1,array_t2):

   # self.tr = 100*np.average(self.array_t1)
        # self.te = 300
      k_space = np.zeros((num, num), dtype=np.complex)
      signal =np.ones((num,num))
      signalx =np.ones((num,num))

      #startup Cycle
      for i in range(5):
          signal = signal * np.exp(-te / array_t2)
          signal = (1 - np.exp(-tr / array_t1))

      #tagging Preparation
      for n in range (0,num) :
        for m in range (0,num,4):
            signal[n][m]=signal[n][m]*np.sin(((np.pi)/num)*n)
            print(signal)

        #K-space
        signal =signal*np.sin(theta*(np.pi/180))
        for kspacerow in range(num):
            QApplication.processEvents()
            signal = signal * np.exp(-te / array_t2)

            for kspacecol in range(num):
                GX = 2 * np.pi * kspacerow / num
                GY = 2 * np.pi * kspacecol / num
                QApplication.processEvents()
                for i in range(num):
                    for j in range(num):
                        total_theta = (GX * i + GY * j)
                        k_space[kspacerow, kspacecol] += signal[i, j] * np.exp(-1j * total_theta)
                        QApplication.processEvents()
            #print("signal",signal)
            signal = 1 - np.exp(-tr / array_t1)
        return k_space





