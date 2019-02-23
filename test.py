from ogn.client import AprsClient
from ogn.parser import parse, ParseError

import logging

# Test function to log position of arbitrary flarm data
def process_beacon(raw_message):
    try:
        beacon = parse(raw_message)
        print(beacon.get('name'))
    except ParseError as e:
        print('Error, {}'.format(e.message))
    

def main():
    # setup logging
    logging.basicConfig(filename="LiveRanking.log", level=logging.INFO)
    
    # set up ogn client
    ogn_filter = 'r/47.417690/7.500544/200'  
    client = AprsClient(aprs_user='N0CALL', aprs_filter=ogn_filter)
    client.connect()
    
    try:
        client.run(callback=process_beacon, autoreconnect=True)
    except KeyboardInterrupt:
        print('\nStop ogn gateway')
        client.disconnect()
    
if __name__ == '__main__':
    main()
    
    
# 47.417690, 7.500544
# r/47.417690/7.500544/100 -p/FLRD
#filter r/lat/lon/dist
