import requests 
import json
from bs4 import BeautifulSoup as Soup
import csv 

url = "https://pointstreak.com/prostats/scoringleaders.html?leagueid=794&seasonid=19243"
stats = requests.get(url)

soup = Soup(stats.text, "lxml")

souptable = soup.findAll('table')[2]
souptr = souptable.findAll('tr')[2:-1]

def parse_tr(souptr):
    table_datas = souptr.findAll('td')
    v = [td.getText() for td in table_datas]
    return {
        "RK": v[0].strip(),
    	"PLAYER":v[1],
        "TEAM":v[2],
        "POS":v[3],
        "GP":v[4],
        "G":v[5],
        "A":v[6],
        "PTS":v[7],
        "PIM":v[8],	
        "PPG":v[9],	
        "PPA":v[10],	
        "SHG":v[11],	
        "SHA":v[12],	
        "GWG":v[13],	
        "LB":v[14],	
        "FO":v[15],
    }
data = [parse_tr(souptr) for souptr in souptr]
keynames = data[0].keys()

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keynames)
    writer.writeheader()   
    for datum in data:
        writer.writerow(datum) 



#RK	PLAYER	TEAM	POS	GP	G	A	PTS	PIM	PPG	PPA	SHG	SHA	GWG	LB	FO