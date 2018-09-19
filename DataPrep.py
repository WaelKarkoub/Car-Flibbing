import pandas as pd 
import re
df = pd.read_csv('SampleData.csv',index_col=0) 
data = pd.DataFrame()
data[['carName','className','modelName']] = df[['carName','className','modelName']]

colors = ['blue','yellow','white','red','brown','black','bronze','beige','gold','silver','grey','gray','copper','green','marooon','orange','sonic titanium','violet','purple']
grey = ['silver','grey','gray','sonic titanium']
red = ['red','maroon','orange']
blue = ['blue']
yellow = ['yellow','gold']
brown = ['brown','bronze','biege','copper']
orange = ['orange']
purple = ['purple','violet']
white = ['white']
black = ['black']
green = ['green']
finish = ['matte','metallic','pearl']

for k,i in df.color.iteritems():
    new_set = i.replace('&', ' ').replace('and', '')
    j = new_set.split()
    j = [word.lower() for word in j]
    j = list(filter(lambda x: x in colors+finish, j))
    print(j)
    counter = 0
    length = len(j)

    for index,clr in enumerate(j):
        if clr in colors:
            counter += 1
        else:
            continue
    
    print(counter, length)
    if counter == 1 and length == counter:
        data.ix[k,'finish'] = 'metallic'
        data.ix[k,'secondColor'] = 0

        if j[length-1] in grey:
            data.ix[k,'firstColor'] = 'grey'
        
        if j[length-1] in red:
            data.ix[k,'firstColor'] = 'red'
        
        if j[length-1] in blue:
            data.ix[k,'firstColor'] = 'blue'

        if j[length-1] in yellow:
            data.ix[k,'firstColor'] = 'yellow'

        if j[length-1] in brown:
            data.ix[k,'firstColor'] = 'brown'

        if j[length-1] in orange:
            data.ix[k,'firstColor'] = 'orange'
        
        if j[length-1] in purple:
            data.ix[k,'firstColor'] = 'purple'
        
        if j[length-1] in white:
            data.ix[k,'firstColor'] = 'white'
        
        if j[length-1] in black:
            data.ix[k,'firstColor'] = 'black'
        
        if j[length-1] in green:
            data.ix[k,'firstColor'] = 'green'
    
    if counter == 1 and length == counter+1:
        data.ix[k,'secondColor'] = 0

        if j[length-2] in grey:
            data.ix[k,'firstColor'] = 'grey'
        
        if j[length-2] in red:
            data.ix[k,'firstColor'] = 'red'
        
        if j[length-2] in blue:
            data.ix[k,'firstColor'] = 'blue'

        if j[length-2] in yellow:
            data.ix[k,'firstColor'] = 'yellow'

        if j[length-2] in brown:
            data.ix[k,'firstColor'] = 'brown'

        if j[length-2] in orange:
            data.ix[k,'firstColor'] = 'orange'
        
        if j[length-2] in purple:
            data.ix[k,'firstColor'] = 'purple'
        
        if j[length-2] in white:
            data.ix[k,'firstColor'] = 'white'
        
        if j[length-2] in black:
            data.ix[k,'firstColor'] = 'black'
        
        if j[length-2] in green:
            data.ix[k,'firstColor'] = 'green'
        
        if j[length-1] in finish:
            data.ix[k,'finish'] = j[length-1]


    
    if counter == 2 and length == counter:
        data.ix[k,'finish'] = 'metallic'

        if j[length-2] in grey:
            data.ix[k,'firstColor'] = 'grey'

        if j[length-2] in red:
            data.ix[k,'firstColor'] = 'red'
        
        if j[length-2] in blue:
            data.ix[k,'firstColor'] = 'blue'

        if j[length-2] in yellow:
            data.ix[k,'firstColor'] = 'yellow'

        if j[length-2] in brown:
            data.ix[k,'firstColor'] = 'brown'

        if j[length-2] in orange:
            data.ix[k,'firstColor'] = 'orange'
        
        if j[length-2] in purple:
            data.ix[k,'firstColor'] = 'purple'
        
        if j[length-2] in white:
            data.ix[k,'firstColor'] = 'white'
        
        if j[length-2] in black:
            data.ix[k,'firstColor'] = 'black'
        
        if j[length-2] in green:
            data.ix[k,'firstColor'] = 'green'

        if j[length-1] in grey:
            data.ix[k,'secondColor'] = 'grey'
            
        if j[length-1] in red:
            data.ix[k,'secondColor'] = 'red'
        
        if j[length-1] in blue:
            data.ix[k,'secondColor'] = 'blue'

        if j[length-1] in yellow:
            data.ix[k,'secondColor'] = 'yellow'

        if j[length-1] in brown:
            data.ix[k,'secondColor'] = 'brown'

        if j[length-1] in orange:
            data.ix[k,'secondColor'] = 'orange'
        
        if j[length-1] in purple:
            data.ix[k,'secondColor'] = 'purple'
        
        if j[length-1] in white:
            data.ix[k,'secondColor'] = 'white'
        
        if j[length-1] in black:
            data.ix[k,'secondColor'] = 'black'
        
        if j[length-1] in green:
            data.ix[k,'secondColor'] = 'green'

    if counter == 2 and length == counter+1:
        print(j[length-3])
        data.ix[k,'finish'] = 'metallic'

        if j[length-3] in grey:
            data.ix[k,'firstColor'] = 'grey'

        if j[length-3] in red:
            data.ix[k,'firstColor'] = 'red'
        
        if j[length-3] in blue:
            data.ix[k,'firstColor'] = 'blue'

        if j[length-3] in yellow:
            data.ix[k,'firstColor'] = 'yellow'

        if j[length-3] in brown:
            data.ix[k,'firstColor'] = 'brown'

        if j[length-3] in orange:
            data.ix[k,'firstColor'] = 'orange'
        
        if j[length-3] in purple:
            data.ix[k,'firstColor'] = 'purple'
        
        if j[length-3] in white:
            data.ix[k,'firstColor'] = 'white'
        
        if j[length-3] in black:
            data.ix[k,'firstColor'] = 'black'
        
        if j[length-3] in green:
            data.ix[k,'firstColor'] = 'green'

        if j[length-2] in grey:
            data.ix[k,'secondColor'] = 'grey'
            
        if j[length-2] in red:
            data.ix[k,'secondColor'] = 'red'
        
        if j[length-2] in blue:
            data.ix[k,'secondColor'] = 'blue'

        if j[length-2] in yellow:
            data.ix[k,'secondColor'] = 'yellow'

        if j[length-2] in brown:
            data.ix[k,'secondColor'] = 'brown'

        if j[length-2] in orange:
            data.ix[k,'secondColor'] = 'orange'
        
        if j[length-2] in purple:
            data.ix[k,'secondColor'] = 'purple'
        
        if j[length-2] in white:
            data.ix[k,'secondColor'] = 'white'
        
        if j[length-2] in black:
            data.ix[k,'secondColor'] = 'black'
        
        if j[length-2] in green:
            data.ix[k,'secondColor'] = 'green'

        if j[length-1] in finish:
            data.ix[k,'finish'] = j[length-1]


for k,i in df.insideColor.iteritems():
    new_set = i.replace('&', ' ').replace('and', '')
    j = new_set.split()
    j = [word.lower() for word in j]
    j = list(filter(lambda x: x in colors, j))
    print(j)
    counter = 0
    length = len(j)

    for index,clr in enumerate(j):
        if clr in colors:
            counter += 1
        else:
            continue
    
    print(counter, length)
    if counter == 1:
        data.ix[k,'secondSeatColor'] = 0

        if j[counter-1] in grey:
            data.ix[k,'firstSeatColor'] = 'grey'
        
        if j[counter-1] in red:
            data.ix[k,'firstSeatColor'] = 'red'
        
        if j[counter-1] in blue:
            data.ix[k,'firstSeatColor'] = 'blue'

        if j[counter-1] in yellow:
            data.ix[k,'firstSeatColor'] = 'yellow'

        if j[counter-1] in brown:
            data.ix[k,'firstSeatColor'] = 'brown'

        if j[counter-1] in orange:
            data.ix[k,'firstSeatColor'] = 'orange'
        
        if j[counter-1] in purple:
            data.ix[k,'firstSeatColor'] = 'purple'
        
        if j[counter-1] in white:
            data.ix[k,'firstSeatColor'] = 'white'
        
        if j[counter-1] in black:
            data.ix[k,'firstSeatColor'] = 'black'
        
        if j[counter-1] in green:
            data.ix[k,'firstSeatColor'] = 'green'

    
    if counter == 2:
        if j[counter-2] in grey:
            data.ix[k,'firstSeatColor'] = 'grey'

        if j[counter-2] in red:
            data.ix[k,'firstSeatColor'] = 'red'
        
        if j[counter-2] in blue:
            data.ix[k,'firstSeatColor'] = 'blue'

        if j[counter-2] in yellow:
            data.ix[k,'firstSeatColor'] = 'yellow'

        if j[counter-2] in brown:
            data.ix[k,'firstSeatColor'] = 'brown'

        if j[counter-2] in orange:
            data.ix[k,'firstSeatColor'] = 'orange'
        
        if j[counter-2] in purple:
            data.ix[k,'firstSeatColor'] = 'purple'
        
        if j[counter-2] in white:
            data.ix[k,'firstSeatColor'] = 'white'
        
        if j[counter-2] in black:
            data.ix[k,'firstSeatColor'] = 'black'
        
        if j[counter-2] in green:
            data.ix[k,'firstSeatColor'] = 'green'

        if j[counter-1] in grey:
            data.ix[k,'secondSeatColor'] = 'grey'
            
        if j[counter-1] in red:
            data.ix[k,'secondSeatColor'] = 'red'
        
        if j[counter-1] in blue:
            data.ix[k,'secondSeatColor'] = 'blue'

        if j[counter-1] in yellow:
            data.ix[k,'secondSeatColor'] = 'yellow'

        if j[counter-1] in brown:
            data.ix[k,'secondSeatColor'] = 'brown'

        if j[counter-1] in orange:
            data.ix[k,'secondSeatColor'] = 'orange'
        
        if j[counter-1] in purple:
            data.ix[k,'secondSeatColor'] = 'purple'
        
        if j[counter-1] in white:
            data.ix[k,'secondSeatColor'] = 'white'
        
        if j[counter-1] in black:
            data.ix[k,'secondSeatColor'] = 'black'
        
        if j[counter-1] in green:
            data.ix[k,'secondSeatColor'] = 'green'

    
def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True

def yesNo(series):
    return {
        'YES': 1,
        'NO':0
    }[series]

def transmision(series):
    return {
        'Automatic':1,
        'automatic':1,
        'Manual':0,
        'manual':0
    }[series]

def seatMaterial(series):
    return {
        'Leather':1,
        'leather':1,
        'cloth':0,
        'Cloth':0
    }[series]

def removeString(series):
    ans = ''
    for k,i in series.iteritems():
        for char in i:
            if is_int(char):
                ans = ans + char
    
    return int(ans)



data['slideRoof'] = df.slideRoof.apply(yesNo)
data['parkSensors'] = df.parkSensors.apply(yesNo)
data['camera'] = df.camera.apply(yesNo)
data['dvd'] = df.dvd.apply(yesNo)
data['cd'] = df.cd.apply(yesNo)
data['bluetooth'] = df.bluetooth.apply(yesNo)
data['gps'] = df.gps.apply(yesNo)
data['warranty'] = df.warranty.apply(yesNo)
data['gear']=df.gear.apply(transmision)
data['seatLeather']=df.seatsType.apply(seatMaterial)


for k,i in df.mileage.iteritems():
    ans = ''
    for char in i:
        if is_int(char):
            ans = ans + char
    ans = int(ans)
    data.ix[k,'mileage'] = ans

for k,i in df.price.iteritems():
    ans = ''
    for char in i:
        if is_int(char):
            ans = ans + char
    ans = int(ans)
    data.ix[k,'price'] = ans 


print(data)