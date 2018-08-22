from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIps(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: " +historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"html.parser")

    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress)
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')  #此网站需要验证码，目前没解决
    except HTTPError:
        return None
    responseJson  = json.loads(response)
    return responseJson["region_name"]

links = getLinks("/wiki/Python_(programming_language)")

while(len(links)>0):
    for link in links:
        print("-----------------------")
        historyIps = getHistoryIps(link.attrs["href"])
        for historyIp in historyIps:
            country = getCountry(historyIp)
            if country is not None:
                print(historyIP+ "is from" +country)

    newlink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newlink)
