import time

daftar = []

limit = 1

jumlah_wajar = 100

opsi = ["tambahkan", "upgrade", "lihat", "keluar"]

for nomor, option in enumerate(opsi, start=1):
        print(f"{nomor}. {option}")
        
def ketik(teks, delay=0.20):
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(delay)
    print()        
        
while True:
    print(f"inventory: {len(daftar)}/{limit}")
    pilihan = input("opsi> ")
    
    if pilihan == "1":
        if len(daftar) >= limit:
            print("yahaha kena limit")
        else:
            masuk = input("masukkan item: ")
            
            if masuk == "67":
                ketik("SIX SEVEN,ROKU NANA,ENAM TUJUH", 0.05)
                
                time.sleep(2)
                
                print("67676767676767")
                
                time.sleep(1)
                
                daftar.append(masuk)
            else:
                daftar.append(masuk)
            for konten in daftar:
                print(konten)
    elif pilihan == "2":
        tambah = int(input("masukan kredit kamu: "))
        
        if tambah >= jumlah_wajar:
            print("yang bener ajg")
        else:
            
            print("tunggu...")
            
            time.sleep(3)
            
            print("mengambil value...")
            
            time.sleep(3)
            
            limit += tambah
            
            print(f"slot inventory sekarang: {limit}")
            
    elif pilihan == "3":
        print(daftar)

    elif pilihan == "4":
            break
    else:
        print("opsi tidak valid")        
