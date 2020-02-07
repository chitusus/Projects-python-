#! /usr/bin/python3
# -*- coding: utf-8 -*-
''' this script chagnes mac addresses  '''
import pyperclip
from sys import argv


def mac(arg, f='u'):

    MAC = [i for i in arg if i.isalnum()]
    MAC = ''.join(MAC)
    MAC_UP = MAC.upper()
    LOW = {'low': MAC[0:2] + ':' + MAC[2:4] + ':' + MAC[4:6] +
           ':' + MAC[6:8] + ':' + MAC[8:10] + ':' + MAC[10:]}
    UP = {'up': MAC_UP[0:2] + ':' + MAC_UP[2:4] + ':' + MAC_UP[4:6] +
          ':' + MAC_UP[6:8] + ':' + MAC_UP[8:10] + ':' + MAC_UP[10:]}
    HP_STALE = {'HP-Style': MAC[0:4] + '-' + MAC[4:8] + '-' + MAC[8:]}
    CISCO_STYLE = {'Cisco-Style': MAC[0:4] + '.' + MAC[4:8] + '.' + MAC[8:]}
    if f == 'c':
        pyperclip.copy(CISCO_STYLE['Cisco-Style'])
        print("{:.<15s} {} {}".format('Cisco Style:',CISCO_STYLE['Cisco-Style'],'bufferd'))
        print("{:.<15s} {} ".format('HP Style:', HP_STALE['HP-Style']))
        print("{:.<15s} {} ".format('Low Style:', LOW['low'].lower()))
        print("{:.<15s} {} ".format('Up Style:',UP['up']))


    elif f == 'h':
        pyperclip.copy(HP_STALE['HP-Style'])
        print("{:.<15s} {}".format('Cisco Style:',CISCO_STYLE['Cisco-Style']))
        print("{:.<15s} {} {}".format('HP Style:', HP_STALE['HP-Style'],'bufferd'))
        print("{:.<15s} {} ".format('Low Style:', LOW['low'].lower()))
        print("{:.<15s} {} ".format('Up Style:',UP['up']))

    elif f == 'l':
        pyperclip.copy(LOW['low'].lower())
        print("{:.<15s} {} ".format('Cisco Style:',CISCO_STYLE['Cisco-Style']))
        print("{:.<15s} {} ".format('HP Style:', HP_STALE['HP-Style']))
        print("{:.<15s} {} {}".format('Low Style:', LOW['low'].lower(),'buffered'))
        print("{:.<15s} {} ".format('Up Style:',UP['up']))


    else:
        pyperclip.copy(UP['up'])
        print("{:.<15s} {} ".format('Cisco Style:',CISCO_STYLE['Cisco-Style']))
        print("{:.<15s} {} ".format('HP Style:', HP_STALE['HP-Style']))
        print("{:.<15s} {} ".format('Low Style:', LOW['low'].lower()))
        print("{:.<15s} {} {}".format('Up Style:',UP['up'],'bufferd'))



if __name__ == "__main__":
    if len(argv)==3 and argv[1]=='c' or argv[1]=='h' or argv[1]=='l' :
        mac(argv[2],f=argv[1])
    elif len(argv)==2 :
        mac(argv[1])
    else:
        print('miss!!! flag can be : c,h,l')


