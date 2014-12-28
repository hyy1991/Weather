from WeatherService import WeatherService
from PyQt4 import QtCore, QtDeclarative, QtGui
from WeatherWindow import WeatherWindow

class MainWindow(QtCore.QObject):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self._weatherWindow=[]
        self._weatherWindow.append( WeatherWindow.WeatherWindow())
        self._service = WeatherService()

    @QtCore.pyqtProperty(QtDeclarative.QPyDeclarativeListProperty, constant=True)
    def weatherWindow(self):
        return QtDeclarative.QPyDeclarativeListProperty(self, self._weatherWindow)

    @QtCore.pyqtSlot()
    def refresh(self):
        print("refreshed")
        result = self._service.getWeather()
        print(result)
        self._weatherWindow[0].imgSource = 'img/' + result[1]
        self._weatherWindow[0].infoText = result[0]
    
if __name__ == '__main__':
    import sys
    
    app = QtGui.QApplication(sys.argv)
    canvas = QtDeclarative.QDeclarativeView()
    engine = canvas.engine()

    main = MainWindow()

    engine.rootContext().setContextObject(main)
    canvas.setSource(QtCore.QUrl.fromLocalFile('MainWindow.qml'))
    engine.quit.connect(app.quit)

    canvas.setGeometry(QtCore.QRect(100, 100, 200, 200))
    canvas.show()

    sys.exit(app.exec_())
