import urllib2
from xml.dom import minidom
import datetime
import codecs

def getCardinal(angle):
	directions = 8
	degree = 360 / directions
	angle = angle + degree/2
	if angle >= (0 * degree) and angle < (1 * degree):
		return "N"
	if angle >= (1 * degree) and angle < (2 * degree):
		return "NE"
	if angle >= (2 * degree) and angle < (3 * degree):
		return "E"
	if angle >= (3 * degree) and angle < (4 * degree):
		return "SE"
	if angle >= (4 * degree) and angle < (5 * degree):
		return "S"
	if angle >= (5 * degree) and angle < (6 * degree):
		return "SW"
	if angle >= (6 * degree) and angle < (7 * degree):
		return "W"
	if angle >= (7 * degree) and angle < (8 * degree):
		return "NW"
	return "N"

#Code of my city
CODE = "2972"
#Change to false if you want Fahrenheit and mph
METRIC = True
if METRIC:
     weather_xml = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=' + CODE + '&u=c&d=9').read()
else:
     weather_xml = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=' + CODE + '&u=f&d=9').read()

dom = minidom.parseString(weather_xml)

#Get weather Tags
xml_current = dom.getElementsByTagName('yweather:condition')
xml_temperatures = dom.getElementsByTagName('yweather:forecast')
xml_wind = dom.getElementsByTagName('yweather:wind')
xml_location = dom.getElementsByTagName('yweather:location')
xml_atmos = dom.getElementsByTagName('yweather:atmosphere')
xml_units = dom.getElementsByTagName('yweather:units')
xml_astron = dom.getElementsByTagName('yweather:astronomy')
#Get today Tag
current = xml_current[0]
today = xml_temperatures[4]
wind = xml_wind[0]
location = xml_location[0]
atmos = xml_atmos[0]
units = xml_units[0]
astron = xml_astron[0]
#Get info
status = current.getAttribute('text')
image = current.getAttribute('code')
date = current.getAttribute('date')
concisedates = date.split()
concisedate = ' '.join([concisedates[2],concisedates[1].lstrip("0")])
concisetime = ' '.join([concisedates[4],concisedates[5]])

temp = current.getAttribute('temp')
low = today.getAttribute('low')
high = today.getAttribute('high')
chill = wind.getAttribute('chill')
direction = wind.getAttribute('direction')
speed = wind.getAttribute('speed')
humidity = atmos.getAttribute('humidity')
pressure = atmos.getAttribute('pressure')
pressureunit = units.getAttribute('pressure')
city = location.getAttribute('city')
sunset = astron.getAttribute('sunset')
sunrise = astron.getAttribute('sunrise')
image_url = 'assets/' + image + '.png'

# Open SVG to process
output = codecs.open('template.svg', 'r', encoding='utf-8').read()


# Insert icons and temperatures
output = output.replace('TODAY',concisedate)
output = output.replace('TIME',concisetime)
output = output.replace('CITY',city)
output = output.replace('HUMID',humidity)
output = output.replace('ICON_ONE',image_url)
output = output.replace('HIGH_ONE',temp)

output = output.replace('LOW_ONE',chill)
output = output.replace('SUNSET',sunset.rstrip(' pm'))
output = output.replace('SUNRISE',sunrise.rstrip(' am'))

output = output.replace('STATUS',status)
if chill==temp:
     output = output.replace('black','white')
     output = output.replace('TEMPYCOORD','310')
else:
     output = output.replace('TEMPYCOORD','270')


output = output.replace('SPEED',str(int(round(float(speed)))))
output = output.replace('NESW',getCardinal(float(direction)))
if METRIC:
    output = output.replace('UNIT','km/h')
else:
    output = output.replace('UNIT','mph')
# Write output
codecs.open('weather-processed.svg', 'w', encoding='utf-8').write(output)
