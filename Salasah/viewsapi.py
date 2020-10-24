from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class KategoriView(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class BahaniView(viewsets.ModelViewSet):
    queryset = Bahan.objects.all()
    serializer_class = BahanSerializer

class VarianView(viewsets.ModelViewSet):
    queryset = Varian.objects.all()
    serializer_class = VarianSerializer

class KodeBarangView(viewsets.ModelViewSet):
    queryset = KodeBarang.objects.all()
    serializer_class = KodeBarangSerializer

class ProdukiView(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

    def retrieve(self, request, *args, **kwargs):
          instance = self.get_object()
          bs = Produk.objects.all()
          serializer = ProdukSerializer(bs, many=True)

          return Response(serializer.data)

class MasukView(viewsets.ModelViewSet):
    queryset = Masuk.objects.all()
    serializer_class = MasukSerializer

class KeluarView(viewsets.ModelViewSet):
    queryset = Keluar.objects.all()
    serializer_class = KeluarSerializer

class TokoView(viewsets.ModelViewSet):
    queryset = Toko.objects.all()
    serializer_class = TokoSerializer

class OnlineOrderView(viewsets.ModelViewSet):
    queryset = OnlineOrder.objects.all()
    serializer_class = OnlineOrderSerializer

class OfflineOrderView(viewsets.ModelViewSet):
    queryset = OfflineOrder.objects.all()
    serializer_class = OfflineOrderSerializer

