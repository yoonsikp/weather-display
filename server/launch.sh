#!/bin/sh

cd "$(dirname "$0")"

#Parse Weather and replace placeholder text in the svg template file
python parse_weather.py

#convert svg to png, and rotate 90 degrees for horizontal view
convert -depth 8 -rotate 90 weather-processed.svg weather-processed.png

#We optimize the image (necessary for viewing on the kindle)
pngcrush -q -c 0 weather-processed.png weather-script-output.png > /dev/null 2>&1

#We move the image where it needs to be (the webserver directory)
rm /var/www/weather-script-output.png
mv weather-script-output.png /var/www/weather-script-output.png

#garbage cleanup
rm weather-processed.svg
rm weather-processed.png

