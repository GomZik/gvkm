from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_Settings import Ui_Settings

class Settings(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        #--- Connections
        self.ui.browse_button.clicked.connect(self.browse_button_clicked)
        
    def browse_button_clicked(self):
        self.ui.path_to_folder.setText(QFileDialog.getExistingDirectory())