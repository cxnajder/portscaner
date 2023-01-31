import sys
plik_adresy = open("adresy.txt", "r+")
if plik_adresy.readable():
    zbior_adresow = plik_adresy.readlines()
    for adres in zbior_adresow:
        print(adres)