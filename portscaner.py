import sys
plik_adresy = open("adresy.txt", "r+")
if plik_adresy.readable():
    zbior_adresow = plik_adresy.readlines()
    for adres in zbior_adresow:
        print("="*10)
        print("Skanowanie hosta", adres)
        for port in range (1, 65535):
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            wynik_polaczenia = soket.connect_ex((adres, port))
            if not(wynik_polaczenia):
                print("Port", port, "jest otwarty")
            soket.close()
