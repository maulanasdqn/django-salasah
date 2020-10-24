from rest_framework import serializers
from .models import *

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class BahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bahan
        fields = '__all__'     

class VarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varian
        fields = '__all__'       

class KodeBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = KodeBarang
        fields = '__all__'        

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ('id', 'nama', 'harga_beli', 'harga_jual', 'kategori', 'bahan', 'berat', 'varian', 'deskripsi', 'kode_barang', 'gambar')

class MasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masuk
        fields = '__all__'      

class KeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keluar
        fields = '__all__'   

class TokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toko
        fields = '__all__'       

class OnlineOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineOrder
        fields = '__all__'        

class OfflineOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineOrder
        fields = '__all__'      