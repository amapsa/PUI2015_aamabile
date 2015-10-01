import sys
import urllib2
import json

## I first import the data through the API

if __name__=='__main__':
    MTA_KEY = sys.argv[1]
    BUS_LINE = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s' % (MTA_KEY, BUS_LINE)
    request = urllib2.urlopen(url)
    bus_data = json.loads(request.read())

## I save a "shortcut" to access the lower layers of the JSON file more rapidly
    
    vehicles = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

## I print the desired output
    
    print 'Bus Line :', BUS_LINE
    print 'Number of Active Buses :', len(vehicles)

    number = 0
    for v in vehicles:
        print 'Bus', number, 'is at latitude', v['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 'and longitude', v['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        number = number + 1
