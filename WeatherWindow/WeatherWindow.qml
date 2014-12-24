import QtQuick 1.0

Item {
    id : weatherWindow
    property int itemWidth : 30
    property int itemHeight : 30
    width : weatherWindow.itemWidth*10; height : weatherWindow.itemHeight*10
    Column {
	spacing : 2
	Image {
	    id : weatherImg
	    source : imgSource
	    width : weatherWindow.itemWidth * 10
	    height : weatherWindow.itemHeight * 6
	}
	Text {
	    id : weatherInfo
	    property int fonSize : 15
	    property string detail : "hehe"
	    text : weatherInfo.detail
	    color : "red"
	    elide : Text.ElideRight
	    font.pixelSize : weatherInfo.fontSize
	}
    }
    /*
    states : State {
    	name : "weatherChange"
	when : weatherChanged
	PropertyChanges : {target : weatherImg; source : imgSource}
    }*/
}
