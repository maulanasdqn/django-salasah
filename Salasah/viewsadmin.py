from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.http import JsonResponse
from django.template.loader import render_to_string


def home(request):
    form = ProdukModelForm()
    context = {'form': form}
    return render(request, 'Backend/Home/home.html', context)

def produk_list(request):
    produk = Produk.objects.all()
    context = {'produk': produk}
    return render(request, 'Backend/List-Produk/home.html')

def produk(request):
    produk = Produk.objects.all()
    kategori = Kategori.objects.all()
    bahan = Bahan.objects.all()
    varian = Varian.objects.all()
    kode_barang = KodeBarang.objects.all()
    data = {'produk': produk,
            'kategori': kategori,
            'bahan': bahan,
            'varian': varian,
            'kode_barang': kode_barang
            }
    return render(request, 'Backend/Produk/produk.html', data)

def produk_create(request):
    data = dict()
    if request.method == 'POST':
        form = ProdukModelForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ProdukModelForm()
    context = {'form': form}
    data['html_form'] = render_to_string('Backend/List-Produk/Create-Produk/create.html', context, request=request)
    return JsonResponse(data)







