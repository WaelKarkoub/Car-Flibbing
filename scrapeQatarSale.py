from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

qatarSale = pd.DataFrame()
qatarSale['url'] = pd.Series()
qatarSale.set_index('url',inplace=True)
for i in range(93959,300000):
    print(i)
    url = 'http://www.qatarsale.com/mycar_e.aspx?carid={}'.format(i)

    uClient = uReq(url)
    pageHTML = uClient.read()
    uClient.close()
    page_soup = soup(pageHTML,"html.parser")

    test = page_soup.findAll(text = re.compile('Sorry but this car is no longer available'))

    if not test:
        sold = page_soup.find('span',{"id": "ad_stats"}).text
        if sold == 'Advertise Date':
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
            continue
    else:
        continue
qatarSale.to_csv('scrapedData.csv')