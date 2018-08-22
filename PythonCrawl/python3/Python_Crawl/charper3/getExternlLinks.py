from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if(link.attrs["href"].startswith("/")):
                internalLinks.append(includeUrl+link.attrs["href"])
            else:
                internalLinks.append(link.attrs["href"])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("没有外链接，循环查找一个")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链接："+externalLink)
    followExternalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    bsObj =  BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, domain)
    externalLinks = getExternalLinks(bsObj, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

#followExternalOnly("http://oreilly.com")
#followExternalOnly("http://www.baidu.com")

allIntLinks.add("http://www.baidu.com")
getAllExternalLinks("http://www.baidu.com")

