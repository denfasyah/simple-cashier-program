print("=" * 100)
print("{:^100}".format("SELAMAT DATANG"))
print("=" * 100)
# Input Awal
nama_pembeli = input("Masukkan Nama Lengkap anda : ")
no_hp = input("Masukkan No. Handphone anda : ")
belibarang =int(input("Banyaknya Pembelian Product  : "))
print("-" * 100)

# List
list_product = []
list_harga = []
list_ukuran = []
list_subtotal = []


# Fungsi Def
def Tshirt():
    print("{:^100}".format("Product T-Shirt"))
    print("=" * 100)
    print("{:^20}{:^20}{:^20}{:^20}{:^20}".format("Nama Produk", "Harga S", "Harga M", "Harga L", "Harga XL"))
    print("=" * 100)
    print("{:^20}{:<20}{:<20}{:<20}{:<20}".format("1. T-Shirt A", "      Rp75.000,-", "      Rp78.000,-", "      Rp80.000,-", "      Rp85.000,-"))
    print("{:^20}{:<20}{:<20}{:<20}{:<20}".format("2. T-Shirt B", "      Rp90.000,-", "      Rp93.000,-", "      Rp95.000,-", "      Rp100.000,-"))
    print("{:^20}{:<20}{:<20}{:<20}{:<20}".format("3. T-Shirt C", "      Rp100.000,-", "      Rp103.000,-", "      Rp105.000,-", "      Rp110.000,-"))
    print("{:^20}{:<20}{:<20}{:<20}{:<20}".format("4. T-Shirt D", "      Rp90.000,-", "      Rp93.000,-", "      Rp95.000,-", "      Rp100.000,-"))
    print("{:^20}{:<20}{:<20}{:<20}{:<20}".format("5. T-Shirt E", "      Rp80.000,-", "      Rp83.000,-", "      Rp85.000,-", "      Rp90.000,-"))
    print("=" * 100)
    return


def Pants():
    print("{:^100}".format("Product Pants"))
    print("=" * 100)
    print("{:^20}{:^20}{:^20}{:^20}{:^20}".format("Nama Produk", "Harga S", "Harga M", "Harga L", "Harga XL"))
    print("=" * 100)
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("    1. PANTS A", "      Rp95.000,-", "      Rp98.000,-", "      Rp90.000,-", "      Rp95.000,-"))
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("    2. PANTS B", "      Rp110.000,-", "      Rp113.000,-", "      Rp115.000,-", "      Rp120.000,-"))
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("    3. PANTS C", "      Rp120.000,-", "      Rp123.000,-", "      Rp125.000,-", "      Rp130.000,-"))
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("    4. PANTS D", "      Rp110.000,-", "      Rp113.000,-", "      Rp115.000,-", "      Rp120.000,-"))
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("    5. PANTS E", "      Rp100.000,-", "      Rp103.000,-", "      Rp105.000,-", "      Rp110.000,-"))
    print("=" * 100)
    return

# Percabangan & Perulangan
for i in range(belibarang):
    print("Pembelian barang ke- " + str(i + 1))
    KategoriProduct = input("Kategori Product [T-Shirt/Pants] : ")
    print()
    #T-SHIRT
    if KategoriProduct.upper() == "T-SHIRT": 
        Tshirt()
        pilihan_product = input("Masukkan Pilihan T-Shirt [1 - 5] : ")
        ukuran_baju = input("Ukuran [S/M/L/XL] : ")
        
        #Product
        
            #T-Shirt A
        if pilihan_product == "1" or pilihan_product == "T-Shirt A":
            nama_product = "T-Shirt A"
            list_product.append(nama_product)
            
            #Size T-Shirt A
            if ukuran_baju == "S" or ukuran_baju == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 75000
            elif ukuran_baju == "M" or ukuran_baju == "m":
                ukuran = "M"
                harga = 78000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "L" or ukuran_baju == "l":
                ukuran = "L"
                harga = 80000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
                ukuran = "XL"
                harga = 85000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #T-Shirt B
        elif pilihan_product == "2" or pilihan_product == "T-Shirt B":
            nama_product = "T-Shirt B"
            list_product.append(nama_product)
            
            #Size T-Shirt B
            if ukuran_baju == "S" or ukuran_baju == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 90000
            elif ukuran_baju == "M" or ukuran_baju == "m":
                ukuran = "M"
                harga = 93000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "L" or ukuran_baju == "l":
                ukuran = "L"
                harga = 95000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
                ukuran = "XL"
                harga = 100000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #T-Shirt C
        elif pilihan_product == "3" or pilihan_product == "T-Shirt C":
            nama_product = "T-Shirt C"
            list_product.append(nama_product)
            
            #Size T-Shirt C
            if ukuran_baju == "S" or ukuran_baju == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 100000
            elif ukuran_baju == "M" or ukuran_baju == "m":
                ukuran = "M"
                harga = 103000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "L" or ukuran_baju == "l":
                ukuran = "L"
                harga = 105000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
                ukuran = "XL"
                harga = 110000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #T-Shirt D
        elif pilihan_product == "4" or pilihan_product == "T-Shirt D":
            nama_product = "T-Shirt D"
            list_product.append(nama_product)
            
            #Size T-Shirt D
            if ukuran_baju == "S" or ukuran_baju == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 90000
            elif ukuran_baju == "M" or ukuran_baju == "m":
                ukuran = "M"
                harga = 93000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "L" or ukuran_baju == "l":
                ukuran = "L"
                harga = 95000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
                ukuran = "XL"
                harga = 100000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #T-Shirt E
        elif pilihan_product == "5" or pilihan_product == "T-Shirt E":
            nama_product = "T-Shirt E"
            list_product.append(nama_product)
            
            #Size T-Shirt E
            if ukuran_baju == "S" or ukuran_baju == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 80000
            elif ukuran_baju == "M" or ukuran_baju == "m":
                ukuran = "M"
                harga = 83000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "L" or ukuran_baju == "l":
                ukuran = "L"
                harga = 85000
                list_ukuran.append(ukuran)
            elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
                ukuran = "XL"
                harga = 90000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)

        else:
            print("Kode T-Shirt salah")
            print("T-Shirt tidak ditemukan")
            print()


    #PANTS
    elif KategoriProduct.upper() == "PANTS": 
        Pants()
        pilihan_product = input("Masukkan Pilihan Pants [1 - 5] : ")
        ukuran_celana = input("Ukuran [S/M/L/XL] : ")
        print()

        #Product
        
            #Pants A
        if pilihan_product == "1" or pilihan_product == "Pants A":
            nama_product = "Pants A"
            list_product.append(nama_product)
            
            #Size Pants A
            if ukuran_celana == "S" or ukuran_celana == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 95000
            elif ukuran_celana == "M" or ukuran_celana == "m":
                ukuran = "M"
                harga = 98000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "L" or ukuran_celana == "l":
                ukuran = "L"
                harga = 100000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "XL" or ukuran_celana == "Xl" or ukuran_celana == "xl":
                ukuran = "XL"
                harga = 105000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
     
            #Pants B
        elif pilihan_product == "2" or pilihan_product == "Pants B":
            nama_product = "Pants B"
            list_product.append(nama_product)
            
            #Size Pants B
            if ukuran_celana == "S" or ukuran_celana == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 110000
            elif ukuran_celana == "M" or ukuran_celana == "m":
                ukuran = "M"
                harga = 113000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "L" or ukuran_celana == "l":
                ukuran = "L"
                harga = 115000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "XL" or ukuran_celana == "Xl" or ukuran_celana == "xl":
                ukuran = "XL"
                harga = 120000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #Pants C
        elif pilihan_product == "3" or pilihan_product == "Pants C":
            nama_product = "Pants C"
            list_product.append(nama_product)
            
            #Size Pants C
            if ukuran_celana == "S" or ukuran_celana == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 120000
            elif ukuran_celana == "M" or ukuran_celana == "m":
                ukuran = "M"
                harga = 123000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "L" or ukuran_celana == "l":
                ukuran = "L"
                harga = 125000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "XL" or ukuran_celana == "Xl" or ukuran_celana == "xl":
                ukuran = "XL"
                harga = 130000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #Pants D
        elif pilihan_product == "4" or pilihan_product == "Pants D":
            nama_product = "Pants D"
            list_product.append(nama_product)
            
            #Size Pants D
            if ukuran_celana == "S" or ukuran_celana == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 110000
            elif ukuran_celana == "M" or ukuran_celana == "m":
                ukuran = "M"
                harga = 113000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "L" or ukuran_celana == "l":
                ukuran = "L"
                harga = 115000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "XL" or ukuran_celana == "Xl" or ukuran_celana == "xl":
                ukuran = "XL"
                harga = 120000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)
            
            #Pants E
        elif pilihan_product == "5" or pilihan_product == "Pants E":
            nama_product = "Pants E"
            list_product.append(nama_product)
            
            #Size Pants E
            if ukuran_celana == "S" or ukuran_celana == "s":
                ukuran = "S"
                list_ukuran.append(ukuran)
                harga = 100000
            elif ukuran_celana == "M" or ukuran_celana == "m":
                ukuran = "M"
                harga = 103000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "L" or ukuran_celana == "l":
                ukuran = "L"
                harga = 105000
                list_ukuran.append(ukuran)
            elif ukuran_celana == "XL" or ukuran_celana == "Xl" or ukuran_celana == "xl":
                ukuran = "XL"
                harga = 110000
                list_ukuran.append(ukuran)
            else:
                print()
                print("     Tidak diketahui ukurannya")
                print()
            
            list_harga.append(harga)
            sub_total = list_harga[i] 
            list_subtotal.append(sub_total)        

        else:
            print("Kode Pants salah")
            print("Pants tidak ditemukan")
            

    else:
        print()
        print("Kategori Product Salah")
        break

# Output Program
print("=" * 100)
print("{:^100}".format("SARZ STORE"))
print("{:^100}".format("Your Own Style"))
print("=" * 100)
print()
print("{:^100}".format(str(nama_pembeli)))
print("{:^100}".format(str(no_hp)))
print()
print("Daftar Belanjaan :")
print("=" * 100)
# print("{:_<20}{:=^20}{:_>20}".format('Rata Kiri', 'Tengah', 'Rata Kanan'))
print("{:^20}{:^20}{:^20}{:^20}".format("Nama Product","Ukuran","Harga","Subtotal"))
print("=" * 100)
for i in range(belibarang):
    print("{:^20}{:^20}{:^20}{:^20}".format(list_product[i], list_ukuran[i], list_harga[i], list_subtotal[i]))
print("-" * 100)

# Total Jumlah Harga Seluruh Barang Belanjaan
Total = sum(list_subtotal)

print("Total belanja : Rp" + str(Total))

# Pemberian Diskon
if Total >= 300000:
    print()
    print("Selamat!")
    print("Anda Mendapatkan Diskon 10%")
    diskon = Total * 10 / 100
else:
    diskon = 0
print()

jumlah_bayar = int(Total - diskon)

print("Total Akhir : Rp", jumlah_bayar)
print("-" * 100)

# Pembayaran
Ubyr = int(input("Bayar : Rp"))

# Uang Kembalian
uangkembalian = Ubyr - jumlah_bayar
if uangkembalian == 0:
    print("Uang Kembalian : Rp0")
else:
    print("Uang Kembalian : Rp", int(uangkembalian))


print()
print("{:^100}".format("TERIMA KASIH SUDAH BELANJA DI SARZ STORE :)"))





