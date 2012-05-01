from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Login(QWebView):
    
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
                "http://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=http://oauth.vk.com/blank.html&display=popup&response_type=token" % (self.app_id, self.scope)
            )
        )
    
    def on_page_load(self, ok):
        if ok:
            url_parts = self.url().toString().split('#')
            if len(url_parts) > 1:
                if url_parts[0] == "http://oauth.vk.com/blank.html":
                    self.hide()
                    self.logged_in.emit(url_parts[1])
                    return
        self.show()