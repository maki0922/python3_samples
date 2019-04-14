#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ipaddress

if __name__ == "__main__":

    IPADDR = '192.168.10.10'
    NWADDR = '192.168.10.0'
    SUBNET = '255.255.255.0'
    PREFIX = '28'

    print('Base IP        : ' + IPADDR)
    print('NetWrok        : ' + NWADDR)
    print('Subnet Address : ' + SUBNET)
    print('Prefix         : ' + PREFIX)

    print('\n---- IPアドレス判定系 ----\n') 

    if ipaddress.ip_address(IPADDR) :
        print(IPADDR + 'はIPv4アドレスと判定されます')

    try :
        ipaddress.ip_address('192.168.10.257')
    except : 
        print('192.168.10.257はIPv4アドレスと判定されません')

    print('\n ---- ネットワークアドレス判定系 ---- \n')

    if ipaddress.ip_network(NWADDR + '/' + PREFIX):
       print(NWADDR + 'はネットワークアドレスと判定されます')

    try : 
        ipaddress.ip_network(IPADDR + '/' + PREFIX)
    except :
        print(IPADDR + 'はネットワークアドレスではありません')

    print('\n ####### オブジェクトを使ってみる ####### \n')

    base_ip = ipaddress.ip_address(IPADDR)
    print('オブジェクトのIPアドレス : %s' % base_ip)

    print('\n ---- IPアドレスをプラマイ操作 ---- \n')
    increment_ip = base_ip + 1
    decrement_ip = base_ip - 1
    print('IPアドレスをインクリメント : %s' % increment_ip)
    print('IPアドレスをデクリメント   : %s' % decrement_ip)

    print('\n ---- 第3オクテットを+1してみる ----\n')
    increment_3_ip = str(ipaddress.ip_address(int(base_ip + (256*1))))
    increment_4_ip = str(ipaddress.ip_address(int(base_ip + (256*256))))
    print('ベースのIP                                                          : %s' % base_ip)
    print('まずは整数化(%d)して数値化してオクテット数分(256)を増やすと : %s' % (int(base_ip), increment_3_ip)) 
    print('おまけで第2の場合は256*256を追加すれば                              : %s' % increment_4_ip) 
