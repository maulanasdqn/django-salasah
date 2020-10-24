from django.urls import path, include
from .import viewsapi 
from rest_framework import routers
# Create your views here.

router = routers.DefaultRouter()
router.register('Kategori', viewsapi.KategoriView)
router.register('Bahan', viewsapi.BahaniView)
router.register('Varian', viewsapi.VarianView)
router.register('KodeBarang', viewsapi.KodeBarangView)
router.register('Produk', viewsapi.ProdukiView)
router.register('Masuk', viewsapi.MasukView)
router.register('Keluar', viewsapi.KeluarView)
router.register('Toko', viewsapi.TokoView)
router.register('OnlineOrder', viewsapi.OnlineOrderView)
router.register('OfflineOrder', viewsapi.OfflineOrderView)

urlpatterns = [
    path('', include(router.urls)),
    
]

