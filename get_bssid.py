""" Get the Commotion-Wireless style BSSID based on ESSID and channel. """

__license__ = 'GPLv3'

import hashlib
import sys

BSSID_SIZE = 6
CHAN_SIZE = 2

def get_bssid_chunks(essid, chan):
    """ Returns BSSID as a list of numbers
    essid   Advertised network name as a string.
    channel 802.11b/g/n/ac channel number as a string.
    returns MAC address as a list of integers.
    """
    md5 = hashlib.md5()
    md5.update(essid)
    digest = md5.hexdigest()
    # chop the md5sum into 1 byte hex segments
    bytes = []
    for i in range(0, len(digest)/2, 2):
        bytes.append(digest[i:i+2])
    # grab a MAC address worth of checksum starting from the front
    bssid = [int(x, 16) for x in bytes][:6]
    # zero out the channel id section
    for i in range(BSSID_SIZE-CHAN_SIZE,CHAN_SIZE):
        bssid[i] = 0
    # Set the first byte to 0x02 (the value of a link-local ethernet address)
    #  which is required for a valid bssid.
    bssid[0] = 2
    # set the channel id at the end of the MAC
    bssid[BSSID_SIZE-CHAN_SIZE] = chan / 10
    bssid[BSSID_SIZE-CHAN_SIZE+1] = chan % 10
    # return the list of 1 byte hex strings
    return bssid

def get_bssid(essid, channel):
    """ Returns the BSSID as a formatted string.
        eg. essid="b" channel="4" then bssid="02:EB:5F:FE:00:04"
    essid   Advertised network name as a string.
    channel 802.11b/g/n/ac channel number as a string.
    returns MAC address as a string.
    """
    bssid = get_bssid_chunks(essid, int(channel, 10))
    return ':'.join(['%02x' % x for x in bssid])


if __name__ == '__main__':
    print(get_bssid(sys.argv[1], sys.argv[2]).upper())
