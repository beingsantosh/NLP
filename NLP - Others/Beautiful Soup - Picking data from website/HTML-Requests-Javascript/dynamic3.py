from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
chrome_path = "C:/Users/Mein Pc/Downloads/chromedriver_win32/chromedriver"

base_url3 = 'https://economictimes.indiatimes.com/archivelist/year-2020,month-3,starttime-43916.cms'

def fetch_headlines(halfurl):
    driver3 = webdriver.Chrome(chrome_path)

    base_url3 = 'https://economictimes.indiatimes.com/archivelist/'+halfurl
    driver3.get(base_url3)


    data3=driver3.page_source

    soup = BeautifulSoup(data3,'html.parser')

    tab = soup.find_all('table')

    link = tab[1].find_all('a')

    text = [i.text for i in link]

    driver3.quit()
    text = np.array(text)
    # print(len(link))
    # print((text))
    return (text)





#print(fetch_headlines('year-2020,month-3,starttime-43916.cms'))