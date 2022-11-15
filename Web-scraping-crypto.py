


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import csv

url = 'https://www.investing.com/crypto/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')



table_rows = soup.findAll("tr")


for row in table_rows[1:6]:
    td = row.findAll("td")

    name = (td[2].text.strip())

    sym = (td[3].text.strip())

    price = (td[4].text)

    change = (td[8].text.strip())


    priceform = float(td[4].text.replace(",",""))

    change_calc = float(td[8].text.replace("+","").replace("%","")) / 100


    calc_price = round((priceform+(priceform * change_calc)),4)



    print(f"Crypto Name: {name}")
    print(f"Symbol: {sym}")
    print(f"Current Price: ${price}")
    print(f"Price Changed Over 24 Hours (%): {change}")
    print(f"Corresponding Price: ${calc_price}")
    print()





import keys
from twilio.rest import Client
client = Client(keys.accountsSID,keys.authToken)
TwilioNumber = "+14633454319"
myCellPhone = "+12147998257"





for row in table_rows[1:6]:
    td = row.findAll("td")
    name = (td[2].text.strip())
    curprice = float(td[4].text.replace(",",""))



    if name == "Bitcoin" and curprice < 40000:
        txt = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="Bitcoin has fallen below $40,000")


    if name == "Ethereum" and curprice < 3000:
        txt = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="Ethereum has fallen below $3,000")

