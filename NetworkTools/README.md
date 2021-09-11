# Network Traffic Visualization

Network Traffic visualization using the Python, Wireshark and Google Map

# Prerequisites

## GeoLiteCity

First of you will need to download the GeoLiteCity database as this will be
used to translate a IP address into a Geo location(longitude & latitude). The
database can be downloaded
here: [GeoLiteCity-data](https://github.com/mbcc2006/GeoLiteCity-data)

## Wireshark

Besides the GeoLiteCity database you will also be needing the Wireshark
application to be able to capture network traffic on your device. The captured
traffic will act as input to our Python script and will be the data displayed
at the end using Google Maps. The Wireshark application can be downloaded
here: [https://www.wireshark.org](https://www.wireshark.org/)

## Google Maps

With our newly created .kml file, we’re now ready to add it to Google Maps.
Here you can create a new map and Import a new
layer: [MyMaps](https://www.google.com/mymaps).

Click on Import and then select the .kml file on your computer, once the file
is uploaded you should see the network traffic being dislayed on the map.

# View Project in Execution

The example below is based on my captured data.

![](https://raw.githubusercontent.com/alexcamargos/Learning_Python_Programming/master/NetworkTraffic/resources/google_maps.jpg)

## License

Copyright (c) 2021 - **Alexsander Lopes Camargos**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.