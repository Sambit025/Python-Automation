import requests
from bs4 import BeautifulSoup

def getcurrency(in_curr,out_curr,amt=1):
    url = f'https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount={amt}'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    #content > div:nth-child(1) > div > div:nth-child(1) > div > div > span.ccOutputRslt
    curr =float(soup.find('span',class_ = 'ccOutputRslt').get_text()[0:-4])
    print(f'{amt} {in_curr} = {curr} {out_curr}')
    

def getSource(any_url):
    content = requests.get(any_url).text
    with open('source.txt','w',encoding='utf-8') as file:
        file.write(content)



getcurrency('GBP','USD')
# getSource('https://www.x-rates.com/calculator/?from=GBP&to=INR&amount=1')
