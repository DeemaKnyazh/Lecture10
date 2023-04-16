from keepAliveServ import keep_alive
import requests
from bs4 import BeautifulSoup
import csv_processor
import datetime
import time
import html5lib

URL = "https://shop.havenshop.com/collections/cav-empt"

# Schduled for noon and 6 pm
schedule = [12, 18]

# Start the server, which will keep the below loop alive as long as it is active
keep_alive()

# Web Scraping Loop
while(True):
    currentDateTime = datetime.datetime.now() # Get current time
    currentTime = datetime.timedelta(hours=(currentDateTime.hour), minutes=(currentDateTime.minute))
    timeDiff = []

    # Calculate time until execution
    for aTime in schedule:
        today = datetime.timedelta(hours=aTime)
        delta = today - currentTime

        # Only add positive time differences
        if delta.total_seconds() >= 0:
            timeDiff.append(delta.total_seconds())
    
    # If there are any positive time differences
    if len(timeDiff) > 0:
        # Wait for the smallest time difference and then run
        time.sleep(min(timeDiff))

        r = requests.get(URL)

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
            products.append([getContents(tag.find(scrapeBrand)), getContents(tag.find(scrapeName)), getContents(tag.find(scrapePrice))])
        
        csv_processor.save_csv(products, f"WebScrape{currentDateTime.year}-{currentDateTime.month}-{currentDateTime.day} {currentDateTime.hour}{currentDateTime.minute}.csv")
    else:
        # Wait 4 hours before checking again
        time.sleep(14400)