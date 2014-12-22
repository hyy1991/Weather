import QtQuick 1.0

Item {
    id : weatherWindow
    property int itemWidth : 30
    property int itemHeight : 20
    width : weatherWindow.itemWidth*10; height : weatherWindow.itemHeight*10
    Column {
	spacing : 2
	Image {
	    id : weatherImg
	    source : "../../front.png"
	    width : weatherWindow.itemWidth * 10
	    height : weatherWindow.itemHeight * 6
	}
	Text {
	    text : "Hello World!"
	    font.family : "Helvetica"
	    color : "red"
	    contentHeight : weatherWindow.itemHeight * 3
	}
    }
}
