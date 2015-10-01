import sys
import urllib2
import json
import csv

## I first import the data through the API                                                     

if __name__=='__main__':
    MTA_KEY = sys.argv[1]
    BUS_LINE = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s' % (MTA_KEY, BUS_LINE)
    request = urllib2.urlopen(url)
    bus_data = json.loads(request.read())

## I save a "shortcut" to access the lower layers of the JSON file more rapidly                

    vehicles = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

## I start to export the data to a csv file

    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

## I use the fields StopPointName and PresentableDistance, as metadata suggests that information is stored there (OnwardCalls field is always empty in the test run)

        for v in vehicles:
            busLat = v['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            busLon = v['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

            if v['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'] != {}:
                busStopName = v['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
                busStopStatus = v['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']

            else:
                busStopName = "N/A"
                busStopStatus = "N/A"

            writer.writerow([busLat, busLon, busStopName, busStopStatus])

