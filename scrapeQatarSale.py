from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
from joblib import Parallel, delayed
import multiprocessing
import time
import pickle
import itertools

qatarSale = pd.DataFrame()
qatarSale['url'] = pd.Series()
qatarSale.set_index('url',inplace=True)
start = time.time()
ranges = 'idList.txt'

def parallelScraping(i):
    print('i: {}'.format(i))
    url = 'http://www.qatarsale.com/mycar_e.aspx?carid={}'.format(i)
    qatarSale = pd.DataFrame()
    qatarSale['url'] = pd.Series()
    qatarSale.set_index('url',inplace=True)
    

    z = 0

    uClient = uReq(url)
    pageHTML = uClient.read()
    uClient.close()
    page_soup = soup(pageHTML,"html.parser")

    test = page_soup.findAll(text = re.compile('Sorry but this car is no longer available'))

    if not test:
        sold = page_soup.find('span',{"id": "ad_stats"}).text
        if sold == 'Advertise Date':
            z = i
            print("z: {}".format(z))

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

        else:
            pass
    else:
        pass
    return (qatarSale, z)

try:
    with open(ranges, 'rb') as f:
        k = pickle.load(ranges)
        print('file found')

    finalRange = list(range(max(k)+1,300000))
    listRange = k + finalRange
except Exception as e:
    listRange = list(range(90000,300000))
    print('file not found')




num_cores = multiprocessing.cpu_count()
listData = Parallel(n_jobs=num_cores)(delayed(parallelScraping)(i) for i in listRange)
p = [x[0] for x in listData if not x[0].empty]
z = [x[1] for x in listData if x[1]>0]
print('reached')

qatarSale = pd.concat(p)

with open(ranges, 'wb') as f:
    pickle.dump(z, f)

qatarSale.to_csv('scrapedData.csv')
end = time.time()
print('Elapsed time: {} hours'.format((end-start)*0.000277777778))