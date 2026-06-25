import requests
import os
import time
import pyfiglet
from colorama import Fore, init


init(autoreset=True)


BASE_URL = "https://zeldyplakaapi-s60u.onrender.com/plaka"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_banner():

    print(Fore.BLUE + pyfiglet.figlet_format(" ZELDY", font="slant"))
    print(Fore.WHITE + "        PLAKA SORGU TOOL")
    print(Fore.CYAN + "          telegram: @zeldyhackteam\n")

def get_data(params):
    try:
        print(Fore.YELLOW + " Sorgulanıyor...")
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("durum") == "basarili":
                results = data.get("data", [])
                print(Fore.GREEN + f"\n  {len(results)} sonuç bulundu \n")
                
                for idx, item in enumerate(results, 1):
                    print(Fore.YELLOW + f"Sonuç {idx} ")
                    print(f"{Fore.WHITE}Plaka   : {Fore.CYAN}{item.get('plaka')}")
                    print(f"{Fore.WHITE}Sahibi  : {Fore.CYAN}{item.get('sahibi')}")
                    print(f"{Fore.WHITE}Tarih   : {Fore.CYAN}{item.get('tarih')}")
                    print(f"{Fore.WHITE}Telefon : {Fore.CYAN}{item.get('telefon')}\n")
            else:
                print(Fore.RED + f" Hata: {data.get('hata', 'Bilinmeyen hata')}")
        else:
            print(Fore.RED + f" Sunucu hatası: {response.status_code}")
            
    except Exception as e:
        print(Fore.RED + f"  Bağlantı başarısız: {e}")

def main():
    while True:
        clear()
        draw_banner()
        print(f"{Fore.WHITE}1{Fore.YELLOW} - {Fore.WHITE}Plaka ile Sorgula")
        print(f"{Fore.WHITE}2{Fore.YELLOW} - {Fore.WHITE}Ad Soyad ile Sorgula")
        print(f"{Fore.WHITE}3{Fore.YELLOW} - {Fore.WHITE}Çıkış")
        
        choice = input(f"\n{Fore.YELLOW} Seçim: ").strip()

        if choice == "1":
            plaka = input(f"{Fore.CYAN}Plaka gir (Örn: 12ABC12): ").strip().upper()
            get_data({"plaka": plaka})
            input(f"\n{Fore.WHITE}Devam etmek için Enter'a bas...")
        
        elif choice == "2":
            adi = input(f"{Fore.CYAN}Ad: ").strip()
            soyadi = input(f"{Fore.CYAN}Soyad: ").strip()
            get_data({"adi": adi, "soyadi": soyadi})
            input(f"\n{Fore.WHITE} Devam etmek için Enter'a bas...")
            
        elif choice == "3":
            print(f"\n{Fore.BLUE} Görüşürüz..")
            break
        else:
            print(Fore.RED + "\n Yanlış seçim.")
            time.sleep(1)

if __name__ == "__main__":
    main()
              
