# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
from add import hi,hello
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def control(x):
    return x

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def hi():
        return "hi"
    def forward(self):
       print(control(1))
    def backward(self):
        print(control(2))
    def right (self):
        print(control(3))
    def left(self):
        print(control(4))

    def open_controller(self):
        self.stackedWidget.setCurrentIndex(1)
    def open_shape(self):
        self.stackedWidget.setCurrentIndex(0)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 800)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 0, 741, 811))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label.setObjectName("label")
        self.label.setText("Circles")

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 55, 16))
        self.label_2.setObjectName("label_5")
        self.label_2.setText("f")

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Squares")

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("f")

        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Triangles")


        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(100, 70, 55, 16))
        self.label_5.setObjectName("label_3")
        self.label_5.setText("f")


        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.label_6.setObjectName("label_3")
        self.label_6.setText("Stars")

        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(100, 100, 55, 16))
        self.label_7.setObjectName("label")
        self.label_7.setText("f")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(500, 10, 55, 16))
        self.label_8.setObjectName("label_5")
        self.label_8.setText("Blue")

        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(600, 10, 55, 16))
        self.label_9.setObjectName("label_3")
        self.label_9.setText("f")

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(500, 40, 55, 16))
        self.label_10.setObjectName("label_3")
        self.label_10.setText("Red")

        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(600, 40, 55, 16))
        self.label_11.setObjectName("label_4")
        self.label_11.setText("f")


        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(500, 70, 55, 16))
        self.label_12.setObjectName("label_3")
        self.label_12.setText("Green")


        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(600, 70, 55, 16))
        self.label_13.setObjectName("label_3")
        self.label_13.setText("f")

        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(500, 100, 55, 16))
        self.label_14.setObjectName("label_5")
        self.label_14.setText("Yellow")

        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(600, 100, 55, 16))
        self.label_15.setObjectName("label_3")
        self.label_15.setText("f")

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(500, 130, 55, 16))
        self.label_10.setObjectName("label_3")
        self.label_10.setText("Pink")

        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(600, 130, 55, 16))
        self.label_11.setObjectName("label_4")
        self.label_11.setText("f")


        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(500, 160, 55, 16))
        self.label_12.setObjectName("label_3")
        self.label_12.setText("Purple")


        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(600, 160, 55, 16))
        self.label_13.setObjectName("label_3")
        self.label_13.setText("f")


        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(500, 190, 55, 16))
        self.label_14.setObjectName("label_3")
        self.label_14.setText("Black")


        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(600, 190, 55, 16))
        self.label_15.setObjectName("label_3")
        self.label_15.setText("f")

        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(500, 220, 55, 16))
        self.label_16.setObjectName("label_3")
        self.label_16.setText("Black")


        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(600, 220, 55, 16))
        self.label_17.setObjectName("label_3")
        self.label_17.setText("f")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 560, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.open_controller)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")


        self.VBL = QtWidgets.QVBoxLayout(self.page_2)
       
        self.FeedLabel = QtWidgets.QLabel(self.page_2)
        self.FeedLabel.setGeometry(0, 0, 800, 400)

        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(80, 420, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.forward)

        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 700, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.right)

        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 700, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.left)

        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 420, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.backward)


        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 560, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_shape)
        
        
        
        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.page_2.setLayout(self.VBL)
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidget.setCurrentIndex(0)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.label.setText(_translate("Form", "circles"))
        # self.label_5.setText(_translate("Form", "TextLabel"))
        # self.label_3.setText(_translate("Form", "squares"))
        # self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton_6.setText(_translate("Form", "switch to controller"))
        self.pushButton.setText(_translate("Form", "forward"))
        self.pushButton_3.setText(_translate("Form", "right"))
        self.pushButton_4.setText(_translate("Form", "left"))
        self.pushButton_2.setText(_translate("Form", "backward"))
        self.pushButton_5.setText(_translate("Form", "switch to shape"))
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        # Capture=cv2.VideoCapture('http://192.168.1.9:4747/video')
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(800, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
