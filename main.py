from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from App import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app_logic = App()
    
    app_logic.run()
    app.exec_()