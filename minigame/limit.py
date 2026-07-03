import time
import random

daftar = []

limit = 1

jumlah_wajar = 100

opsi = ["tambahkan", "upgrade", "lihat", "keluar"]

print("=== Mini Inventory Game ===")
for nomor, option in enumerate(opsi, start=1):
    print(f"{nomor}. {option}")

def ketik(teks, delay=0.15):
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(delay)
    print()

def add_random_item():
    items = ["Sword", "Potion", "Shield", "Gem", "Key", "Ring"]
    return random.choice(items)

while True:
    print(f"\nInventory: {len(daftar)}/{limit}")
    pilihan = input("opsi> ").strip().lower()
    
    if pilihan in ["1", "tambahkan"]:
        if len(daftar) >= limit:
            print("Yahaha, inventory full!")
        else:
            masuk = input("Masukkan item (or type 'random'): ")
            if masuk.lower() == "random":
                masuk = add_random_item()
                print(f"Added random item: {masuk}")
            elif masuk == "67":
                ketik("SIX SEVEN, ROKU NANA, ENAM TUJUH", 0.05)
                time.sleep(1)
                print("67676767676767")
                daftar.append(masuk)
            else:
                daftar.append(masuk)
            print("Inventory now:")
            for konten in daftar:
                print(" -", konten)
    
    elif pilihan in ["2", "upgrade"]:
        try:
            tambah = int(input("Masukkan kredit: "))
            if tambah >= jumlah_wajar:
                print("Too much! Yang bener aja bro")
            else:
                print("Processing...")
                time.sleep(2)
                limit += tambah
                print(f"Inventory slots upgraded to: {limit}")
        except ValueError:
            print("Please enter a number!")
    
    elif pilihan in ["3", "lihat"]:
        if daftar:
            print("Your items:")
            for item in daftar:
                print(" -", item)
        else:
            print("Inventory empty.")
    
    elif pilihan in ["4", "keluar"]:
        print("Thanks for playing!")
        break
    else:
        print("Invalid option. Try 1-4 or the command names.")
