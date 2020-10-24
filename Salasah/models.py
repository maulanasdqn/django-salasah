from django.db import models
from django.db import connection, transaction

jasa = (
    ("Ninja Xpress", "Ninja Xpress"),
    ("J&T Express", "J&T Express"),
    ("JNE EXPRESS","JNE EXPRESS"),
    ("SICEPAT","SICEPAT"),
    ("TiKi","TiKi"),
    ("Pos Indonesia" ,"Pos Indonesia"),
    ("anteraja","anteraja"),
    ("GrabExpress","GrabExpress"),
    ("Gojek" , "Gojek")
)

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Bahan(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Varian(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class KodeBarang(models.Model):
    kode_barang = models.CharField(max_length=10)
    def __str__(self):
        return self.kode_barang

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    harga_beli = models.IntegerField()
    harga_jual = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, unique=False)
    bahan = models.ForeignKey(Bahan, on_delete=models.CASCADE, unique=False)
    berat = models.IntegerField(null=True)
    varian = models.ManyToManyField(Varian, unique=False, null=True, blank=True)
    deskripsi = models.TextField()
    kode_barang = models.ForeignKey(KodeBarang, on_delete=models.CASCADE)
    gambar = models.ImageField(null=True, blank=True)
    


    def __str__ (self):
        return self.nama

class Masuk(models.Model):
    kode_barang = models.ManyToManyField(KodeBarang)
    satuan = models.IntegerField()
    keterangan = models.TextField()
    tanggal = models.DateTimeField()

class Keluar(models.Model):
    kode_barang = models.ManyToManyField(KodeBarang)
    satuan = models.IntegerField()
    keterangan = models.TextField()
    tanggal = models.DateTimeField()

class Toko(models.Model):
    nama = models.CharField(max_length=200)
    no_telepon = models.CharField(max_length=13)

    def __str__(self):
        return self.nama

class OnlineOrder(models.Model):
    toko = models.ManyToManyField(Toko)
    penerima = models.CharField(max_length=100, null=True)
    alamat = models.TextField()
    no_penerima = models.CharField(max_length=13)
    kode_booking = models.CharField(max_length=30)
    jasa_kirim = models.CharField(null=True, choices=jasa, max_length=100)
    kode_barang = models.ManyToManyField(KodeBarang)
    tanggal = models.DateTimeField()

    def __str__(self):
        return self.penerima

class OfflineOrder(models.Model):
    nama = models.CharField(max_length=70)
    no_telepon = models.CharField(max_length=13)
    keterangan = models.TextField()
    kode_barang = models.ManyToManyField(KodeBarang)
    tanggal = models.DateTimeField()

    def __str__(self):
        return self.nama
