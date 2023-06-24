from collections import namedtuple

barang = {
    'beras': {'satuan': 'kg', 'harga': 12000},
    'minyak': {'satuan': 'liter', 'harga':20000},
    'gula': {'satuan': 'kg', 'harga': 10000},
    'telur': {'satuan': 'kg', 'harga': 18000}
    }

hasil = namedtuple('hasil', 'produk qty satuan subtotal')

class Model:    
    def __init__(self):
        self.rekap_belanja = []
        self.grandtotal = 0
        
    def hitung_subtotal(self, kode, qty):
        if kode in barang.keys():
            #hitung harga subtotal dan simpan dalam namedtuple (Soal 1)
            #tambahkan namedtuple pada list rekap_belanja (Soal 2)          
        else:
            print('Produk tidak ditemukan!')

    def hitung_grandtotal(self):
        for i in range(len(self.rekap_belanja)):
            #hitung grandtotal (total belanjaan yang harus dibayar) (Soal 3)
        return self.grandtotal

class View:
    def daftar_harga(self):
        print("Berikut adalah daftar harga barang TRI-mart:")
        for i in barang.keys():
            print(i, "\tper ", barang[i]['satuan'], "\tRp ", barang[i]['harga'])

    def beli(self):
        #Minta user mengetikkan barang yang ingin dibeli (Soal 4)
        #Gunakan method lower() agar input dapat digunakan untuk akses dictionary
        valid_qty = False
        while not valid_qty:
            try:
                #Minta user mengetikkan jumlah pembelian (Soal 5)
                valid_qty = True
            except ValueError:
                print("Masukkan jumlah pembelian dalam angka!")

    def tanya_pembeli(self):
        valid_respon = False
        while not valid_respon:
            respon = input("Apakah Anda masih ingin membeli barang? [Y/T]")
            respon = respon.lower()
            if respon == 'y'or respon == 't':
                valid_respon = True
        return respon

    def totalan(self,belanjaan):
        print("="*45)
        print("Berikut adalah daftar dan total belanja Anda:")
        for i in range(len(belanjaan.rekap_belanja)):
            item = belanjaan.rekap_belanja[i]
            print(item.produk, '\t', item.qty, '\t',item.satuan, '\tRp', item.subtotal)
        print("-"*35)
        print("Total harus dibayar: \tRp", belanjaan.hitung_grandtotal())
            
class Controller:
    def __init__(self):
        #Tambahkan atribut yang diperlukan (Soal 6)
        #

    def run(self):
        valid_input = False
        while not valid_input:
            #Panggil method tanya_pembeli() (Soal 7)
            if  transaksi == 'y':
                #Panggil method beli() (Soal 8)
                #Panggil method hitung_subtotal() (Soal 9)
            else:
                #Panggil method totalan() (Soal 10)
                valid_input = True

aplikasi = Controller()
aplikasi.view.daftar_harga()
aplikasi.run()
            
        
        
            
