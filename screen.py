# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Screen(object):
    def setupUi(self, Screen):
        Screen.setObjectName("Screen")
        Screen.resize(300, 450)
        Screen.setMinimumSize(QtCore.QSize(300, 450))
        Screen.setMaximumSize(QtCore.QSize(300, 450))
        self.centralwidget = QtWidgets.QWidget(Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.image_holder = QtWidgets.QLabel(self.centralwidget)
        self.image_holder.setGeometry(QtCore.QRect(20, 10, 250, 400))
        self.image_holder.setMinimumSize(QtCore.QSize(250, 400))
        self.image_holder.setMaximumSize(QtCore.QSize(250, 400))
        self.image_holder.setText("")
        self.image_holder.setAlignment(QtCore.Qt.AlignCenter)
        self.image_holder.setObjectName("image_holder")
        Screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        Screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Screen)
        self.statusbar.setObjectName("statusbar")
        Screen.setStatusBar(self.statusbar)

        self.retranslateUi(Screen)
        QtCore.QMetaObject.connectSlotsByName(Screen)

    def retranslateUi(self, Screen):
        _translate = QtCore.QCoreApplication.translate
        Screen.setWindowTitle(_translate("Screen", "Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Screen = QtWidgets.QMainWindow()
    ui = Ui_Screen()
    ui.setupUi(Screen)
    Screen.show()
    sys.exit(app.exec_())
