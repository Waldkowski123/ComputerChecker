import socket #Nic nie wiem o tej bibliot
def check_vnc_connection(host): #Nazwa funkcji od chata

    try:
        # Port VNC standardowy to 5900
        with socket.create_connection((host, 5900), timeout=2): #blablabla
            return True #tu mówimy TAK :D
    except (socket.timeout, ConnectionRefusedError, OSError): #hmmm tu robimy to i tak dalej...
        return False # a tu mówimy NIE >:C

def main():
    base_url = "p{}.iem.pw.edu.pl" #Adres wiadomo o co chodzi
    available_hosts = [] #Jakaś tablica gdzie walimy komputerki sprawne :)
    print("Code made by: Valentin Banobre Kalinowski \n (Nahh just kidding chatgpt)")
    for i in range(33):  # Od 0 do 32, tu jest napisane in range do 33 ale w pythonie to jest do 32 bo python jest głupi
        print("Sprawdzanie komputera p", i)
        host = base_url.format(i)
        if check_vnc_connection(host): #Jeżeli działa host to fajnie a jeżeli nie to nie ;/
            available_hosts.append(host)
            print("Znaleziono połączenie z komputerkiem {} :D".format(i)) #mamy komputerek

    print("Dostępne komputery przez VNC:") #Jakiś princik
    for host in available_hosts:
        print(host) #I kolejny princik

if __name__ == "__main__":
    main() #i tutaj wiadomo uruchamiamy naszą funkcję main