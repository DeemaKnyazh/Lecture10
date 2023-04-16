from keepAliveServ import keep_alive
import requests
from bs4 import BeautifulSoup
import csv_processor
import html5lib
import datetime


def run(url, fname):
    currentDateTime = datetime.datetime.now() # Get current time

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    content = soup.body.find_all(attrs={"class":"product-details-wrapper"})

    products = [["Brand", "Product", "Price", "Sizes"]]

    def scrapeBrand(tag):
        if tag.has_attr("class") and tag["class"] == ["product-card-brand"]:
            return True
        return False

    def scrapeName(tag):
        if tag.has_attr("class") and tag["class"] == ["product-card-name"]:
            return True
        return False

    def scrapePrice(tag):
        if tag.has_attr("class") and tag["class"] == ["product-price"]:
            return True
        return False

    def getContents(tag):
        return tag.contents[0].strip()

    for tag in content:
        products.append([getContents(tag.find(scrapeBrand)), getContents(tag.find(scrapeName)), getContents(tag.find(scrapePrice)).replace(',','')])

    csv_processor.save_csv(products, f"{fname}-{currentDateTime.year}-{currentDateTime.month}-{currentDateTime.day} {currentDateTime.hour}{currentDateTime.minute}.csv")