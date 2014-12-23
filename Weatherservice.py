from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
import re

url= "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl"
imp= Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add("http://WebXml.com.cn/")
d= ImportDoctor(imp)
client= Client(url,doctor=d)
pattern = re.compile(r'(.*)\s\((.*)\)')


def getWeather(cityName = 58367):
    result= client.service.getWeatherbyCityName(theCityName = cityName)
    #print(type(result))
    #print(help(type(result)))
    return (result[0][5],result[0][8])

def getSupportCity():
    result = client.service.getSupportCity(byProvinceName = 'All')
    print(type(result[0]))
    print(len(result[0]))
    match = pattern.match(result[0][1])
    print(match.groups())
    return result

if __name__ == "__main__":
    print(getWeather())
    print(getSupportCity())
