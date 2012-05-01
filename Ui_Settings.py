# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue May  1 22:08:33 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(240, 103)
        self.verticalLayout = QtGui.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Settings)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.path_to_folder = QtGui.QLineEdit(Settings)
        self.path_to_folder.setObjectName(_fromUtf8("path_to_folder"))
        self.horizontalLayout.addWidget(self.path_to_folder)
        self.browse_button = QtGui.QPushButton(Settings)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout.addWidget(self.browse_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sync_button = QtGui.QPushButton(Settings)
        self.sync_button.setObjectName(_fromUtf8("sync_button"))
        self.verticalLayout.addWidget(self.sync_button)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "gvkm", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "Папка для музыки", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_button.setText(QtGui.QApplication.translate("Settings", "Выбрать", None, QtGui.QApplication.UnicodeUTF8))
        self.sync_button.setText(QtGui.QApplication.translate("Settings", "Синхронизация", None, QtGui.QApplication.UnicodeUTF8))

