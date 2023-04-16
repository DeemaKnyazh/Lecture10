from keepAliveServ import keep_alive
import datetime
import havenScrapeBot
from threading import Thread
import time

# Start the keepalive server
keep_alive()

processSchedules = [
    {
        "Schedule": [datetime.timedelta(hours=12), datetime.timedelta(hours=18)],
        "Process": havenScrapeBot.run,
        "Args" : ["https://shop.havenshop.com/collections/cav-empt", "Cav Empt"],
        "Name": "Cav Empt Scrape"
    },
    {
        "Schedule": [datetime.timedelta(hours=14), datetime.timedelta(hours=20)],
        "Process": havenScrapeBot.run,
        "Args" : ["https://shop.havenshop.com/collections/kapital", "Kapital"],
        "Name": "Kapital Scrape"
    }
]

def getTimeTilRun(schedule):
    currentDateTime = datetime.datetime.now() # Get current time
    currentTime = datetime.timedelta(hours=currentDateTime.hour, minutes=currentDateTime.minute)
    timeDiff = []
    # Calculate time until execution
    for aTime in schedule:
        delta = aTime - currentTime

        # Only add positive time differences
        if delta.total_seconds() >= 0:
            timeDiff.append(delta.total_seconds())
    return timeDiff


while(True):
    for processSchedule in processSchedules:
        timeDiff = getTimeTilRun(processSchedule["Schedule"])
        if len(timeDiff) > 0 and min(timeDiff) < 60:
            print(f"Running Process {processSchedule['Name']}")
            t = Thread(target=processSchedule["Process"], args=processSchedule["Args"])
            t.start()
    time.sleep(60)
