import sys
import socket

plik_adresy = open("adresy.txt", "r+")
if plik_adresy.readable():
    zbior_adresow = plik_adresy.readlines()
    for adres in zbior_adresow:
        print(adres)
        print("="*10)
        print("Skanowanie hosta", adres)
        for port in range (1,65535):
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(0.5)
            try:
                wynik_polaczenia = soket.connect((adres, port))
                print("Port", port, "jest otwarty")
            except:
                pass
            finally:
                soket.close()
