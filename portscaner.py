import os
import socket
import subprocess

prefiks = input("Prefiks: ")
pierwszy_adr = input("Pierwszy adres: ")
ostatni_adr = input("Ostatni adres: ")

os.system(f"./znajdz_adresy.sh {prefiks} {pierwszy_adr} {ostatni_adr} > adresy.txt")

plik_adresy = open("adresy.txt", "r+")
if plik_adresy.readable():
    zbior_adresow = plik_adresy.readlines()
    for adres in zbior_adresow:
        #print(adres)
        print("="*10)
        print("Skanowanie hosta", adres)
        for port in range (1,65535):
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(0.5)
            wynik_polaczenia = soket.connect_ex((adres.strip(), port))
            if not wynik_polaczenia:
                print("Port", port, "jest otwarty")
            soket.close()
