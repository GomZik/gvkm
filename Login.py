from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Login(QWebView):
    
    login_link = "http://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=popup&response_type=token"
    redirect_link = "http://oauth.vk.com/blank.html"
    app_id = "2930771"
    scope = "audio"
    logged_in = pyqtSignal(QString)
    need_to_show = pyqtSignal()
    
    def __init__(self, parent = None):
        QWebView.__init__(self, parent)
        self.setWindowTitle("gvkm")
        self.loadFinished.connect(self.on_page_load)
    
    def login(self):
        self.load(
            QUrl(
                self.login_link % (self.app_id, self.scope, self.redirect_link)
            )
        )
    
    def on_page_load(self, ok):
        if ok:
            url_parts = self.url().toString().split('#')
            if len(url_parts) > 1:
                if url_parts[0] == self.redirect_link:
                    self.hide()
                    self.logged_in.emit(url_parts[1])
                    return
        self.show()