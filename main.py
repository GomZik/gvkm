from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from App import App
from Login import Login
from Settings import Settings

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    settings = Settings()
    app_logic = App(login, settings)
    
    app_logic.run()
    app.exec_()