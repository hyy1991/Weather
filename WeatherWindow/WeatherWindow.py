from PyQt4 import QtCore, QtDeclarative, QtGui
import time, _thread

class WeatherWindow(QtCore.QObject):
    imgSourceChanged = QtCore.pyqtSignal()
    infoTextChanged = QtCore.pyqtSignal()
    
    def __init__(self):
        super(WeatherWindow, self).__init__()
        self._imgSource = 'img/20.gif'
        self._infoText = ''

    @QtCore.pyqtProperty(str, notify=imgSourceChanged)
    def imgSource(self):
        return self._imgSource

    @imgSource.setter
    def imgSource(self, imgSource):
        self._imgSource = imgSource
        self.imgSourceChanged.emit()

    @QtCore.pyqtProperty(str, notify=infoTextChanged)
    def infoText(self):
        return self._infoText

    @infoText.setter
    def infoText(self, infoText):
        self._infoText = infoText
        self.infoTextChanged.emit()

    '''
    def change(self):
        index = 0
        while True:
            index += 1
            self.imgSource = 'img/' + str(index) + '.gif'
            print(self.imgSource)
            time.sleep(10)

    def thread(self):
        _thread.start_new_thread(self.change())
    '''

    
if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    canvas = QtDeclarative.QDeclarativeView()
    engine = canvas.engine()

    window = WeatherWindow()

    engine.rootContext().setContextObject(window)
    canvas.setSource(QtCore.QUrl.fromLocalFile('WeatherWindow.qml'))

    canvas.setGeometry(QtCore.QRect(100, 100, 450, 450))
    canvas.show()
    window.thread()
    sys.exit(app.exec_())
    
    

