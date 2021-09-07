#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ---------------------------------------------------------------------------
#  Name: network_traffic.py
#  Version: 0.0.1
#  Summary: Network Traffic visualization using the Python, Wireshark and
#           Google Map.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ---------------------------------------------------------------------------

"""Network Traffic visualization using the Python, Wireshark and Google Map."""

import socket
from os import path

# Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
import dpkt
# Pure Python GeoIP API
import pygeoip
import requests

# My Variables
DIRECTORYDATAFILE = 'resources'

# Combines paths names into one complete path.
GEOCITYFILE = path.join(path.dirname(__file__), DIRECTORYDATAFILE, 'geo_lite_city.dat')
PCAPFILE = path.join(path.dirname(__file__), DIRECTORYDATAFILE, 'network_data.pcap')
KMLFILE = path.join(path.dirname(__file__), DIRECTORYDATAFILE, 'network_traffic_display.kml')

try:
    # IP geolocation legacy databases.
    # https://github.com/mbcc2006/GeoLiteCity-data
    geolocation_ip = pygeoip.GeoIP(GEOCITYFILE)
except pygeoip.GeoIPError as error:
    import sys

    sys.exit(f'FATAL ERROR: Failure to load IP geolocation legacy databases (Pure Python GeoIP API).')

try:
    # This service allows you to get your public ip address.
    IPIFY_APIURL = r'https://api.ipify.org'
    IPADDRESS = requests.get(IPIFY_APIURL, timeout=.5).text
except requests.exceptions.RequestException as error:
    print('A serious problem happened. Could not get public IP address.')
    IPADDRESS = input('Enter a valid IP address: ')


def attach_geolocation_data(destination_ip, source_ip):
    """Attach geolocation data to IP's."""

    destination = geolocation_ip.record_by_name(destination_ip)
    # Your public IP address, this was found using 'python requests.get()'.
    source = geolocation_ip.record_by_name(IPADDRESS)

    try:
        destination_longitude = destination['longitude']
        destination_latitude = destination['latitude']
        source_longitude = source['longitude']
        souce_latitude = source['latitude']

        kml = ('<Placemark>\n'
               '<name>%s</name>\n'
               '<extrude>1</extrude>\n'
               '<tessellate>1</tessellate>\n'
               '<styleUrl>#transBluePoly</styleUrl>\n'
               '<LineString>\n'
               '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
               '</LineString>\n'
               '</Placemark>\n'
               ) % (destination_ip,
                    destination_longitude,
                    destination_latitude,
                    source_longitude,
                    souce_latitude)

        return kml
    except:
        return ''


def extract_ip_address(pcap_file):
    """Parsing a PCAP File over captured network data and extract IP's."""

    kmlpts = ''

    # For each packet in the pcap file process the contents.
    for (ts, buf) in pcap_file:
        try:
            # Unpack the Ethernet frame (MAC source/destination, ethernet type).
            ethernet = dpkt.ethernet.Ethernet(buf)

            # Now unpack the data within the Ethernet frame (the IP packet)
            # pulling out source and destination IP.
            ip = ethernet.data

            # inet_ntoa returns IP address in dotted quad-string format.
            # It takes IP addresses in 32-bit packed format as an argument.
            try:
                source = socket.inet_ntoa(ip.src)
                destination = socket.inet_ntoa(ip.dst)
            except OSError as error:
                print(f'ERROR: The byte sequence passed to this function is not exactly 4 bytes in '
                      f'length: {ip.dst}')

            # Attach geolocation IP data.
            kml = attach_geolocation_data(destination, source)

            kmlpts = kmlpts + kml
        except:
            continue

    return kmlpts


def main():
    """Simple Network Traffic visualization."""

    kml_header = '<?xml version="1.0" encoding="UTF-8"?> \n<kml ' \
                 'xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                 '<Style id="transBluePoly">' \
                 '<LineStyle>' \
                 '<width>1.5</width>' \
                 '<color>501400E6</color>' \
                 '</LineStyle>' \
                 '</Style>'

    kml_footer = '</Document>\n</kml>\n'

    try:
        with open(PCAPFILE, 'rb') as filename:
            pcap = dpkt.pcap.Reader(filename)
            kml_file = f'{kml_header}{extract_ip_address(pcap)}{kml_footer}'
    except OSError as error:
        print(f'ERROR: File {PCAPFILE} could not be found.')

    try:
        with open(KMLFILE, 'w+') as filename:
            filename.write(kml_file)
    except OSError as error:
        print(f'ERROR: File {KMLFILE} could not be created.')


if __name__ == '__main__':
    main()
