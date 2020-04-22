#!/usr/bin/env python2

import sys

# for get ip
import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

if __name__ == "__main__":
    dev = "wlan0"
    try:
        dev = sys.argv[1]
    except Exception as e:
        pass
    ip = get_ip_address(dev)
    print( dev,ip)
    print("momentlink:","http://"+ip+":81/minizhiku/wechat/recv.php?user=orangepi4_1&gen=1")

    '''
    try:
        print get_ip_address(sys.argv[1])
    except IndexError:
        raise SystemExit("Usage: %s <interface name>" % sys.argv[0])
    except IOError as err:
        raise SystemExit("{}\n".format(err) +\
                         "Please Enter Correct interface name,\n\t" +\
                         "you can use `$ ifconfig` to check the name")
    except Exception:
        import traceback; traceback.print_exc();
        raise
    '''