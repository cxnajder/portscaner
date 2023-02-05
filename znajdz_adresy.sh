#!/bin/bash

#ifconfig | grep -oE "([0-9]{1,3}[\.]){3}[0-9]{1,3}" | sort | uniq
prefiks=$1 #należy zmienić prefiks na sieci którą chcemy przeskanować
pierwszy_adr=$2 # ustawiamy zakres od
ostatni_adr=$3 # do
for (( ip=$pierwszy_adr; ip<=$ostatni_adr; ip++ ))
do
	ping -c 1 $prefiks.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
