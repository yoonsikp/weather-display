# weather-display
A customizable script to display Yahoo weather data as a portable image


###Server Installation
```
Install DejaVu Fonts

apt-get install imagemagick pngcrush

Configure imagemagick so that it can find the DejaVu fonts:


pip install myql dom

Insert into your crontab 




In a pinch (only if imagemagick can't find your fonts):

Copy fonts to a directory of your choice

Determine the directory of your imagemagick configuration type.xml

In my case, it was "/usr/local/Cellar/imagemagick/6.9.7-0/etc/ImageMagick-6"

cd /usr/local/Cellar/imagemagick/6.9.7-0/etc/ImageMagick-6

wget http://www.imagemagick.org/Usage/scripts/imagick_type_gen -O script.pl

find /Users/username/your_font_directory -name '*Deja*' |./script.pl -f - > ./type-morefonts.xml

nano type.xml

Near the end of the file between <typemap> and </typemap>, add <include file="type-morefonts.xml" />
```
