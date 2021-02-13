from datetime import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup

base_url2 = 'https://economictimes.indiatimes.com/archive/year-2001,month-1.cms'

chrome_path = "C:/Users/Mein Pc/Downloads/chromedriver_win32/chromedriver"




def direct_to_headlines_from_date(url1):
    driver2 = webdriver.Chrome(chrome_path)

    base_url2 = 'https://economictimes.indiatimes.com/'+url1
    driver2.get(base_url2)

    data2 = driver2.page_source

    soup = BeautifulSoup(data2,'html.parser')
    # new_td = soup.find_all('span', class_='normtxt')
    new_td = soup.find_all('table', id = 'calender')

    # soup.find_all('table', id = 'calender')[0].find_all('a')


    # new_td = soup.find_all('td')

    #print(len(new_td))

    # j=0
    date_link = {}
    for i in new_td[0].find_all('a'):
        if len(i) > 0:
            #print(i)
            url = i.attrs['href']
            url_text = i.text
            if (len(url_text) <=2) and (len(url_text) != 0 ) : # only actual date should be included.
                #             print(j)
                date_link[url_text] = url
        #     j+=1
    #print(date_link)

    driver2.quit()
    return date_link

def save_data(data):
    t=open("D:/DataWorld/My Code/git/MyProjects/Predicting the Stock Market with News Articles/Data/File.txt", "w")
    t.write(str(data))
    t.close()

def log_data(counter, filename):

    t=open("D:/DataWorld/My Code/git/MyProjects/Predicting the Stock Market with News Articles/Data/"+filename+".txt", "a")
    if counter == 0:

        t.write(f'Time stamp:{datetime.now()}... web scrapping started...\n\n' )
        t.close()
    else:
        t.write(f'Time stamp:{datetime.now()} and total {counter} headlines are saved till now.\n\n')
        t.close()


def save_dataframe(df,filename):
    df.to_csv("D:/DataWorld/My Code/git/MyProjects/Predicting the Stock Market with News Articles/logs/"+filename+"_df.csv"  )


# file = direct_to_headlines_from_date('/archive/year-2001,month-1.cms')
# print(file)