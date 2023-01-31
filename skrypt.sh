#!/bin/bash

#ifconfig | grep -oE "([0-9]{1,3}[\.]){3}[0-9]{1,3}" | sort | uniq
prefiks=192.168.1 #należy zmienić prefiks na sieci którą chcemy przeskanować
pierwszy_adr=1  # ustawiamy zakres od
ostatni_adr=254 # do
echo "znalezione adresy:"
for (( ip=$pierwszy_adr; ip<=$ostatni_adr; ip++ ))
do
	ping -c 1 $prefiks.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & > adresy.txt
done

while read linia;
    do
        echo "skanowanie adresu $lini:"
        #nmap 
done < temp.txt