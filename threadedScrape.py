from urllib.request import urlopen as uReq
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import time
import pickle
import itertools
from threading import Thread
import requests
from http.client import HTTPException
from socket import timeout
from lxml.html import fromstring
from queue import Queue
import numpy as np 


q = Queue(maxsize=0)
qatarSale = pd.DataFrame()
qatarSale['url'] = pd.Series()
qatarSale.set_index('url',inplace=True)
start = time.time()
ranges = 'idList.txt'

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def populateURL(i):
    urlList=list()
    for num in i:
        url = 'http://www.qatarsale.com/mycar_e.aspx?carid={}'.format(num)
        urlList.append(url)
    return urlList


def scraping(q,result):
    while not q.empty():
        work = q.get()
        url = work[1]
        i = int(url.replace('http://www.qatarsale.com/mycar_e.aspx?carid=',''))
        qatarSale = pd.DataFrame()
        qatarSale['url'] = pd.Series()
        qatarSale.set_index('url',inplace=True)
        z = 0 
        # proxies = np.array(proxies)
        # proxy = np.random.choice(proxies.flatten())
        while True:
            time.sleep(0.8)
            try:
                uClient = uReq(url)
                pageHTML = uClient.read()
                uClient.close()
                break
            except (HTTPError, URLError):
                print("HTTP/URL Error....url: {}".format(url))

                continue
            except timeout:
                print("Timeout Error....url: {}".format(url))

                continue
            except HTTPException:
                print("HTTP exception Error....url: {}".format(url))
                continue
            except Exception as e:
                print(e,'   ','url: {}'.format(url))
                continue
        
        page_soup = soup(pageHTML,"html.parser")

        test = page_soup.findAll(text = re.compile('Sorry but this car is no longer available'))

        if not test:
            sold = page_soup.find('span',{"id": "ad_stats"}).text
            if sold == 'Advertise Date':
                z = i

                carName = page_soup.find('span',{"id": "d_carname"}).text
                className = page_soup.find('span',{"id": "d_classname"}).text
                modelName = page_soup.find('span',{"id": "d_modelname"}).text
                color = page_soup.find('span',{"id": "d_outcolor"}).text
                year = page_soup.find('span',{"id": "d_year"}).text
                gear = page_soup.find('span',{"id": "d_gear"}).text
                cylinders = page_soup.find('span',{"id": "d_cylinder"}).text
                driveTrain = page_soup.find('span',{"id": "d_DriveTrain"}).text
                insideColor = page_soup.find('span',{"id": "d_insidecolor"}).text
                seatsType = page_soup.find('span',{"id": "d_insidetype"}).text
                slideRoof = page_soup.find('span',{"id": "d_slideroof"}).text
                parkSensors = page_soup.find('span',{"id": "d_Sensors"}).text
                camera = page_soup.find('span',{"id": "d_Camera"}).text
                dvd = page_soup.find('span',{"id": "d_dvd"}).text
                cd = page_soup.find('span',{"id": "d_cd"}).text
                bluetooth = page_soup.find('span',{"id": "d_Bluetooth"}).text
                gps = page_soup.find('span',{"id": "d_gps"}).text
                mileage = page_soup.find('span',{"id": "d_km"}).text
                price = page_soup.find('span',{"id": "d_price"}).text
                warranty = page_soup.find('span',{"id": "d_bank"}).text
                advertiseDate = page_soup.find('span',{"id": "ad_date"}).text
                contact = page_soup.find('span',{"id": "d_contact1"}).text

                if page_soup.find('span',{"id": "d_seller4"}):
                    owner = page_soup.find('span',{"id": "d_seller4"}).text
                else:
                    owner = 'Showroom'

                qatarSale.ix[url,'carName'] = carName
                qatarSale.ix[url,'className'] = className
                qatarSale.ix[url,'modelName'] = modelName
                qatarSale.ix[url,'color'] = color
                qatarSale.ix[url,'year'] = year
                qatarSale.ix[url,'gear'] = gear
                qatarSale.ix[url,'cylinders'] = cylinders
                qatarSale.ix[url,'driveTrain'] = driveTrain
                qatarSale.ix[url,'insideColor'] = insideColor
                qatarSale.ix[url,'seatsType'] = seatsType
                qatarSale.ix[url,'slideRoof'] = slideRoof
                qatarSale.ix[url,'parkSensors'] = parkSensors
                qatarSale.ix[url,'camera'] = camera
                qatarSale.ix[url,'dvd'] = dvd
                qatarSale.ix[url,'cd'] = cd
                qatarSale.ix[url,'bluetooth'] = bluetooth
                qatarSale.ix[url,'gps'] = gps
                qatarSale.ix[url,'mileage'] = mileage
                qatarSale.ix[url,'price'] = price
                qatarSale.ix[url,'warranty'] = warranty
                qatarSale.ix[url,'advertiseDate'] = advertiseDate
                qatarSale.ix[url,'contact'] = contact
                qatarSale.ix[url,'owner'] = owner
                print('done: found car {}'.format(z))
                result[work[0]] = (qatarSale, z)

            else:
                print('done: No car found {}'.format(i))
                result[work[0]] = (None,None)
        else:
            print('done: No car found {}'.format(i))
            result[work[0]] = (None,None)
        q.task_done()
    return True

try:
    with open(ranges, 'rb') as f:
        k = pickle.load(f)
        print('file found')

    finalRange = list(range(max(k)+1,300000))
    listRange = k + finalRange
except Exception as e:
    listRange = list(range(93000,300000))
    print('file not found')

urls = populateURL(listRange)
proxies = get_proxies()
num_theads =  min(75,len(urls))
results = [{} for x in urls]

for i in range(len(urls)):
    q.put((i,urls[i]))

for i in range(num_theads):
    worker = Thread(target=scraping, args=(q,results))
    worker.setDaemon(True)
    worker.start()

q.join()

p = [x[0] for x in results if x[0] is not None]
z = [x[1] for x in results if x[1] is not None]

qatarSale = pd.concat(p)

with open(ranges, 'wb') as f:
    pickle.dump(z, f)

qatarSale.to_csv('scrapedData.csv')

end = time.time()
print()
print('Elapsed time: {} hours'.format((end-start)*0.000277777778))