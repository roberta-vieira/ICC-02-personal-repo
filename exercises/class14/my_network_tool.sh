#!/bin/bash

menu_1='Check Network Interface Information'
menu_2='Ping a Host'
menu_3='Port Scan with Nmap'
menu_4='Display Routing Table'
menu_5='Traceroute to Host'
menu_6='Exit'

echo "
Hello dear user, this is my menu, from which you can choose what do to next!

Menu Options:
1) $menu_1
2) $menu_2
3) $menu_3
4) $menu_4
5) $menu_5
6) $menu_6
"

read -p 'Please choose a number from 1 to 6 to select the desired menu option: ' user_menu_option

if [ $user_menu_option -eq 1 ]; then
    echo "
    1) $menu_1
    "
    ip a
elif [ $user_menu_option -eq 2 ]; then
    echo "
    1) $menu_2
    "
    read -p 'Please provide the IP address or domain name you want to ping: ' user_ip_address
    ping -c 5 $user_ip_address
elif [ $user_menu_option -eq 3 ]; then
    echo "
    1) $menu_3
    "
    read -p 'Please provide the IP address range you want to scan: ' user_nmap_ip_address
    nmap  -sn $user_nmap_ip_address
else
    echo "
    6) $menu_6
    "
fi
echo "
Thank you for your visit."


