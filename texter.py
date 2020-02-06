#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pyperclip

def mac(arg,f='u'):

    MAC=[ i for  i in  arg if i.isalnum()]
    MAC=''.join(MAC)
    MAC_UP=MAC.upper()
    LOW={'low': MAC[0:2] + ':' + MAC[2:4] + ':' + MAC[4:6] + ':' + MAC[6:8] + ':' + MAC[8:10] + ':' + MAC[10:]}
    UP={'up':MAC_UP[0:2] + ':' + MAC_UP[2:4] + ':' + MAC_UP[4:6] + ':' + MAC_UP[6:8] + ':' + MAC_UP[8:10] + ':' + MAC_UP[10:]}
    HP_STALE={'HP-Style': MAC[0:4] + '-' + MAC[4:8] + '-' + MAC[8:]}
    CISCO_STYLE={'Cisco-Style': MAC[0:4] + '.' + MAC[4:8] + '.' + MAC[8:]}
    if f =='c':
        pyperclip.copy(CISCO_STYLE['Cisco-Style'])
    elif f == 'h':
        pyperclip.copy(HP_STALE['HP-Style'])
    elif f == 'l':
        pyperclip.copy(LOW['low'].lower())
    else:
        pyperclip.copy(UP['up'])


    print(CISCO_STYLE['Cisco-Style'])
    print(HP_STALE['HP-Style'])
    print(LOW['low'].lower())
    print(UP['up'])






if __name__ == "__main__":
    mac(input(':'))
