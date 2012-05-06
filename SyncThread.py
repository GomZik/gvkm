#-*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import urllib2, json

class SyncThread(QThread):
    
    api_link = "https://api.vk.com/method/"
    
    change_status = pyqtSignal(QString, int)
    sync_complete = pyqtSignal()
    
    def __init__(self, token, path, parent = None):
        QThread.__init__(self, parent)
        self.token = token
        self.path = path

    def run(self):
        response = urllib2.urlopen("%saudio.get?access_token=%s" % (self.api_link, self.token), "r")
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
        self.sync_complete.emit()