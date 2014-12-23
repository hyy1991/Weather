from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
import re

url= "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl"
imp= Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add("http://WebXml.com.cn/")
d= ImportDoctor(imp)
client= Client(url,doctor=d)
pattern = re.compile(r'(.*)\s\((.*)\)')

class WeatherService():
    def __init__(self):
        self._cityId = 58367

    def setCurrentCity(self, cityId):
        self._cityId = cityId

    def getWeather(self):
        result= client.service.getWeatherbyCityName(theCityName = self._cityId)
        return (result[0][5],result[0][8])

    def getAllSupportCity(self):
        result = client.service.getSupportCity(byProvinceName = 'All')
        return result[0]

if __name__ == "__main__":
    service = WeatherService()
    print(service.getWeather())
    print(service.getAllSupportCity())
