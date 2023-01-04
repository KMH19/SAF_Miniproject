import xmlParser
import csv

def getWait(data, csv_file):
    ''' 
    Function for reading the provided csv file with processing times.
    Based on stationId and CarrierId
    '''
    xml = xmlParser.parseXml(data)
    stationId = int(xml.station)
    carrierId = int(xml.carrier)
    
    if stationId < 10:
        stationId = "Station#0" + str(stationId)
    else:
        stationId = "Station#" + str(stationId)
        
    carrierId = "Carrier#" + str(carrierId)
    y = None
    csv_reader = csv.reader(csv_file, delimiter=';')
    
    for row in csv_reader:
        if y == None:
            for x in range(len(row)):
                if row[x] == stationId:
                    y = x
        
        if row[0] == carrierId:
            with open('log.txt', 'a') as log:
                log.write(" - Wait time:%s \n"%(row[y]))
                print("Wait: %s\n"%(row[y]))
            return(row[y])
                


