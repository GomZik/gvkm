# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import urllib2, json
import sys, os

class DownloaderThread(QThread):
    
    change_status = pyqtSignal(QString, int)
    download_complete = pyqtSignal()
    
    def __init__(self, token, path, parent = None):
        QThread.__init__(self, parent)
        self.token = token
        self.path = path

    def run(self):
        response = urllib2.urlopen("https://api.vk.com/method/audio.get?access_token=%s" % self.token, "r")
        audios = json.loads(response.read())
        audios = audios['response']
        i = 1
        for audio in audios:
            self.change_status.emit(u"Скачивание файла %d \ %d" % (i, len(audios)), round(float(i) / float(len(audios)) * 100))
            filename = "%s/%s - %s.mp3" % (self.path, audio['artist'][:25], audio['title'][:25])
            if not os.path.exists(filename):
                mp3 = open(filename,'wb')
                remote_mp3 = urllib2.urlopen(audio['url'])
                mp3.write(remote_mp3.read())
                mp3.close()
            i += 1
        self.download_complete.emit()

class App(QObject):
    
    show_settings = pyqtSignal()
    
    def __init__(self, login, settings, parent = None):
        QObject.__init__(self, parent)
        self.login = login
        self.settings = settings
        #--- Connections
        self.login.logged_in.connect(self.on_logged_in)
        self.show_settings.connect(self.settings.show)
        self.settings.ui.sync_button.clicked.connect(self.on_sync_button_clicked)
    
    def on_logged_in(self, params):
        params_list = params.split('&')
        token = params_list[0].split('=')
        print(token[1])
        self.token = token[1]
        self.show_settings.emit()
        
    def on_sync_button_clicked(self):
        self.settings.hide()
        self.prg = QProgressDialog(u"Получение списка файлов", u"Отмена", 0, 99)
        self.prg.setWindowTitle("gvkm")
        self.prg.setValue(50)
        path = self.settings.ui.path_to_folder.text()
        
        self.downloader = DownloaderThread(self.token, path)
        self.downloader.change_status.connect(self.on_download_status_changed)
        self.downloader.download_complete.connect(self.on_download_complete)
        self.downloader.start()
    
    def run(self):
        self.login.login()
        
    def on_download_status_changed(self, label, progress):
        self.prg.setLabelText(label)
        self.prg.setValue(progress)
        
    def on_download_complete(self):
        sys.exit()