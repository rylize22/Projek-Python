from termcolor import colored, cprint


# cprint("Hello, World!", "green", "on_red")
print ("^-^-" *30)
print ("                                        PT. SINAR ABADI                                         ")
print ("\n")
cprint ("                Selamat Datang di Aplikasi Pemesanan Tiket Kereta Api PT. SINAR ABADI           ", "blue")
cprint ("^-^-" *30, "yellow")

print ("\n")
list_menu = ["Pemesanan Tiket" , "Pengajua Refund Tiket" , "Customer Service"]
print ("1" , list_menu[0])
print ('2' , list_menu[1])
print ("3" , list_menu[2])

while(True):
    #jika memilih opsi 1 (memesan) maka lengkapi data diri
    menu = input("Masukan Pilihan Anda  :       ")
    if menu == "1":
        print("\n")
        print("="*50)
        print("                 Formulir Data Diri                  ")
        print("="*50)
        nama    = input("Masukan Nama Lengkap   :    ")
        no_ktp  = input("Masukan Nomor KTP      :    ")
        alamat  = input("Masukan Alamat Anda    :    ")
        
        print("\n")
        
        #Masukan kereta pilihan
        print("="*50)
        print("                 DAFTAR KERETA                   ")
        print("="*50)
        list_kereta =   ["Kereta Tawang Jaya",  "Kaligung"]
        print("1", list_kereta[0])
        print("2", list_kereta[1])
        print("="*36)
        kereta  =  input("Pilih Kereta Anda:    ")
        print("\n")
        
        if kereta == "1":
            kereta = "KA Tawang Jaya"
            print("-"*50)
            print("    Selamat Datang Di Kereta Tawang Jaya     ")
            print("-"*50)
                #daftar waktu keberangkatan
            print("         Daftar Waktu Keberangkatan           ")
            print("\n")
            tanggal = input("Masukan Tanggal ex(10/06/2023):   ")
            print("\n")
            print("jam keberangkatan")
            list_jam = ["06.00" ,"12.00" , "18.00"]
            print("1", list_jam[0])
            print("2", list_jam[1])
            print("3", list_jam[2])
            print("=" *36)
            jam = input("Masukan Jam Keberangkatan Anda :   ")
            print("\n")
            if jam == "1":
                jam = "06.00"            
            if jam == "2":
                jam = "12.00"            
            if jam == "3":
                jam = "18.00"
            
            print("="*50)
            print("                 Daftar Tujuan                   ")
            print("="*50)
            print("\n")
            list_tujuan = ["Stasiun Gambir", "Stasiun Semarang Poncol"]      
            print("1", list_tujuan[0])    
            print("2", list_tujuan[1])
            print("="*36)
            
            tujuan = input("Masukan Tujuan Anda:    ")
            
                #jika memiih tujuan 1
            if tujuan == "1":
                tujuan = "Stasiun Gambir"
                print()
                print("="*50)
                print("              DAFTAR KELAS               ")
                print("="*50)
                #pilih kelas
                print("==")
                print("Kelas: ")
                Kelas=["Bisnis", "Ekonomi"]
                for x in range (2):
                    print(x+1, Kelas[x])
                #jika memilih kelas bisnis
                print("="*36)
                kelas   = input("Pilihlah Kelas Anda :  ")
                if kelas == "1":
                    kelas = "bisnis"
                    
                    print("\n")
                    pesan =input("Jumlah tiket yang dipesan (max 3 tiket):")
                    if pesan=="1":
                        D = 1*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*120000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "3 tiket"
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                
                elif kelas == "2":
                    kelas = "ekonomi"

                    print("\n")
                    pesan=input("Jumlah tiket yang dipesan (max 3 tiket):")
                    if pesan=="1":
                        D = 1*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "1 tiket"
                    elif pesan=="2":
                        D = 2*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "2 tiket"
                    elif pesan=="3":
                        D = 3*70000
                        print("Total harga tiket anda sebesar Rp.", D)
                        pesan = "3 tiket"
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!") 
            else:
                print("tujuan sudah digantikan")
                break
        else:
            print("kereta sedang tidak beroperasi")
            break
        print("Struk Pembelian")
        print("Nama Anda : ", nama)
        print("ktp :", no_ktp)
        print("alamat :", alamat)
        print("="*10)
        print("nama kereta : ", kereta)
        print("tanggal keberangkatan :",  tanggal)
        print("jam :", jam)
        print("tujuan :", tujuan)
        print("kelas :", kelas)
        break
    elif menu == "2":
        print("fitur belum ada")
        break
    else:
        print("maaf fitur belum ada")
        break
        
print("Terimakasih, jangan lupa senyum")
