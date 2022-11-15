
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title


tables = soup.findAll('tr')
    
for row in tables[1:6]:

    td = row.findAll("td")
    
    rank = td[0].text
    movie = td[1].text
    totgross = td[7].text
    dis = td[9].text
    numt = float(td[6].text.replace(",",""))

    totgross_for = float(td[7].text.replace("$","").replace(',',""))
    calc = round(totgross_for/numt)

    print("_________________________________________")
    print(f"Rank of movie: {rank}")
    print(f"Movie name: {movie}")
    print(f"Gross amount per theater: {calc:,.2f}")
    print(f"Total gross: {totgross}")
    print(f"Distribution: {dis}")
  










#print(title.text)
##
##
##
##

