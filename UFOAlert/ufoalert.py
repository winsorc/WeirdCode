import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

url = "https://wordpress-969990-4143009.cloudwaysapps.com/subndx/?id=all" 

PrevVersion = ""
FirstRun = True
while True:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    soup = BeautifulSoup(response.text, "lxml")

    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()

    if PrevVersion != soup:
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            print ("Phoning Home "+ str(datetime.now()))
        else:
            print ("Sighting reported at https://wordpress-969990-4143009.cloudwaysapps.com/subndx/?id=all2023-12-26 : "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            # compares versions and highlight changes using difflib
            d = difflib.Differ()
            diff = difflib.context_diff(OldPage,NewPage,n=10)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
            PrevVersion = soup
    else:
        print( "Sky is quiet... "+ str(datetime.now()))
    time.sleep(30)
    continue