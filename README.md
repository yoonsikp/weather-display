# weather-display
A customizable script to display Yahoo weather data as a portable image.
![alt text](https://raw.githubusercontent.com/yoonsikp/weather-display/master/weather-script-output.png "Logo Title Text 1")

## Server Installation
First, install DejaVu Fonts.

Next install imagemagick and pngcrush.
```
apt-get install imagemagick pngcrush
```
Configure imagemagick so that it can find the DejaVu fonts.

Then use pip to install the required dependencies.
```
pip install myql dom
```
Insert the script `launch.sh` into your crontab.

Finally, install the web server of your choice and allow the port through your firewall.

## Client Installation
Unzip the contents of `kindleweatherfiles.zip` into the root directory of your Kindle.
Install the jailbreak, and USBNetworking.

Finally, add `/mnt/us/weather/display-weather.sh` to the cron file on the Kindle.

## Troubleshooting
if imagemagick can't find your fonts:
Copy fonts to a directory of your choice

Determine the directory of your imagemagick configuration type.xml

In my case, it was `/usr/local/Cellar/imagemagick/6.9.7-0/etc/ImageMagick-6`
```
cd /usr/local/Cellar/imagemagick/6.9.7-0/etc/ImageMagick-6

wget http://www.imagemagick.org/Usage/scripts/imagick_type_gen -O script.pl

find /Users/username/your_font_directory -name '*Deja*' |./script.pl -f - > ./type-morefonts.xml
```
Finally edit `type.xml`
```
nano type.xml
```
Near the end of the file between `<typemap>` and `</typemap>`, add `<include file="type-morefonts.xml" />`

