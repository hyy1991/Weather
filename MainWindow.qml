import QtQuick 1.0
import "WeatherWindow" 1.0

Item {
    id : mainWindow
    width : 120; height : 80
    Column {
	Rectangle {
		color : "red"
		height : 20 
		width : 120
		MouseArea {
		    anchors.fill : parent
		    onClicked : {refresh()}
		}
	}
	Repeater {
		id : repeater
		model : weatherWindow
		delegate : WeatherWindow {itemWidth : 8; itemHeight : 7}
	}
	
	Timer {
		id : timer
		triggeredOnStart : true
		running :true
		repeat: true
		interval : 1 * 60 * 60 * 1000 
		onTriggered : {
			refresh()
		}
	}
    }
}
