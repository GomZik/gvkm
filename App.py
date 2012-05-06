# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
import sys
import os
from Login import Login
from Settings import Settings
from SyncThread import SyncThread
import pickle

class App(QObject):
    
    show_settings = pyqtSignal()
    
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        
        self.config = {}
        self.config['browser'] = {}
        self.config['browser']['cookies'] = {}
        self.config['path'] = ''
        if os.path.exists('.config'):
            config = open('.config', 'rb')
            self.config = pickle.loads(config.read())
            print self.config
            config.close()
        
        self.tray = QSystemTrayIcon(QIcon('images/default_icon.png'))
        self.tray.show()
        
        self.login = Login()
        if self.config['browser']['cookies']:
            print self.config['browser']['cookies']
            cookies = []
            for name in self.config['browser']['cookies']:
                cookies.append(
                    QNetworkCookie(name, self.config['browser']['cookies'][name])
                )
            self.login.page().networkAccessManager().cookieJar().setCookiesFromUrl(cookies, QUrl(self.login.base_link))
        
        self.settings = Settings()
        #--- Connections
        self.login.logged_in.connect(self.on_logged_in)
        self.show_settings.connect(self.settings.show)
        self.settings.ui.sync_button.clicked.connect(self.on_sync_button_clicked)
    
    def on_logged_in(self, params):
        self.config['browser']['cookies'] = {}
        for cookie in self.login.page().networkAccessManager().cookieJar().cookiesForUrl(QUrl(self.login.base_link)):
            self.config['browser']['cookies'][cookie.name()] = cookie.value()
        self.save_settings()
        params_list = params.split('&')
        token = params_list[0].split('=')
        print(token[1])
        self.token = token[1]
        if self.config['path']:
            self.settings.ui.path_to_folder.setText(self.config['path'])
            self.on_sync_button_clicked()
        else:
            self.show_settings.emit()
        
    def on_sync_button_clicked(self):
        self.settings.hide()
        self.config['path'] = self.settings.ui.path_to_folder.text()
        self.save_settings()
        self.prg = QProgressDialog(u"Получение списка файлов", u"Отмена", 0, 99)
        self.prg.setWindowTitle("gvkm")
        self.prg.setValue(50)
        path = self.settings.ui.path_to_folder.text()
        
        self.sync = SyncThread(self.token, path)
        self.sync.change_status.connect(self.on_sync_status_changed)
        self.sync.sync_complete.connect(self.on_sync_complete)
        self.sync.start()
    
    def run(self):
        self.login.login()
        
    def on_sync_status_changed(self, label, progress):
        self.prg.setLabelText(label)
        self.prg.setValue(progress)
        
    def on_sync_complete(self):
        self.prg.hide()
        
    def save_settings(self):
        config = open('.config', 'wb')
        config.write(pickle.dumps(self.config))
        config.close()