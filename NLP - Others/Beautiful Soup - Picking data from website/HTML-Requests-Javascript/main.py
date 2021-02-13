from requests_html import HTMLSession, HTML

import requests

session = HTMLSession()

base_url = 'https://economictimes.indiatimes.com/archive/year-2001,month-1.cms'

r = session.get(base_url)

html1 = HTML(html=r.content)

print('before', len(html1.find('a')))
print('before', len(html1.find('td')))
divs = html1.find('div')
links = html1.find('a')
urls = html1.absolute_links
td = html1.find('td')
tr = html1.find('#calenderdiv')

html1.render()

print('after', len(html1.find('a')))
new_divs = html1.find('div')
new_links = html1.find('a')
new_urls = html1.absolute_links
new_td = html1.find('td')
new_tr = html1.find('#calenderdiv')

print(len(divs), len(new_divs), len(links), len(new_links), len(urls), len(new_urls),len(tr),len(new_tr))

new_td = html1.find('td')
print('after', len(html1.find('td')))

# j=0
date_link = {}
for i in new_td:
    if len(i.find('a')) > 0:
#        print(i)
        url = i.find('a')[0].attrs['href']
        url_text = i.text
        if (len(url_text) <=2) and (len(url_text) != 0 ) : # only actual date should be included.
#             print(j)
            date_link[url_text] = url
#     j+=1
print(date_link)

session.close()