! pip install beautifulsoup4 
! pip install requests

import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd


try:
    page=requests.get('https://www.moneycontrol.com/stocks/marketinfo/marketcap.php?optex=BSE')
    
except Exceptions as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('error for link',url)
    print (error_type, 'Line:', error_info.tb_lineno)
time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class':'FL'})

page

soup

for i in links:
    print(i.text)
    print("\n")
