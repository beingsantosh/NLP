### This code helps to scrap the headlines from Economictimes website.
###

from selenium import webdriver
from bs4 import BeautifulSoup
import dynamic2, dynamic3
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd

# initiating the timer
t1 = datetime.now()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.headless = True

driver = webdriver.Chrome("C:/Users/Mein Pc/Downloads/chromedriver_win32/chromedriver")

base_url = 'https://economictimes.indiatimes.com/archive.cms'

driver.get(base_url )

data = driver.page_source



soup = BeautifulSoup(data,'html.parser')


span = soup.find_all('span', class_='normtxt')

all_month_link_dict = {}
all_year_link_dict = {}
y = 2001
for i in span[0].find_all('a'):
    link_s = i.attrs['href']
    month_s = i.text
    year_s = (link_s[14:18])

    if len(month_s)>0:
        if year_s == y:

            all_month_link_dict[month_s] = link_s
            all_year_link_dict[year_s] = all_month_link_dict
        else:
            all_month_link_dict = {}
            all_month_link_dict[month_s] = link_s
            all_year_link_dict[year_s] = all_month_link_dict
            y = year_s
#print(all_year_link_dict)
driver.quit()


## for loop to fetch info

year_month_date_link = {}

year_s = ['2016']
month_s = ['May', 'June', 'July','August', 'September', 'October', 'November', 'December']
date_s = ['1']

counter = 0

# log file name:
t = datetime.now()

filename = str(t.year)+'_'+str(t.month)+'_'+str(t.day)+'_'+str(t.hour)+'_'+str(t.minute)+'_'+str(t.second)
dynamic2.log_data(counter, filename)

# dataframe

df = pd.DataFrame(columns=['Year','Month','Day','Headlines'])


for y, d in all_year_link_dict.items():
    if y in year_s:
        month_date_link ={}
        for month, link in d.items():
            #month_date_link[month] = dynamic2.direct_to_headlines_from_date(link)
            if month in month_s: # or True:
                links_to_date = dynamic2.direct_to_headlines_from_date(link)

                date_to_headlines = {}                         # everytime for new date, it should be cleaned

                for date,link_date in links_to_date.items():
                    if date in date_s or True: # specify the date or it will take everything as 'True'
                        lst_dict = []
                        headlines = dynamic3.fetch_headlines(link_date[13:])
                        date_to_headlines[date] = headlines[:10]
                        counter +=10
                        #lst = [y,month,date,headlines[:10]]
                        #l=len(df)
                        lst_dict.append({'Year': y, 'Month': month, 'Day': date, 'Headlines':headlines[:10]})

                        # df['Year'] = y
                        # df['month'] = month
                        # df['day'] = date
                        # df['headlines'] = headlines[:10]
                        df = df.append(lst_dict)
                        dynamic2.log_data(counter, filename)
                        dynamic2.save_dataframe(df, filename)
                month_date_link[month] = date_to_headlines
        year_month_date_link[y] = month_date_link

        dynamic2.save_data(year_month_date_link)
        dynamic2.log_data(counter, filename)
        dynamic2.save_dataframe(df,filename)

        #print(d)

#print(year_month_date_link)



total = 0
for k, v in year_month_date_link.items():
    #     print(k,v)
    for k1, v1 in v.items():
        #         print(k,k1,v1)
        for k2, v2 in v1.items():
            #print(k, k1, k2, v2)
            total = total + len(v2)


print('Total items in dictionary: ', total)
print('Total time taken : ', datetime.now()-t1)


