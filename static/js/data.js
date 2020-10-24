const produk = document.querySelector('.table')
const url = '/api/Produk/'
const tambahData = document.querySelector('.tambahproduk')
const nama = document.getElementById('produk_nama')
const harga_beli = document.getElementById('harga_beli')
const harga_jual = document.getElementById('harga_jual')
const kategori = document.getElementById('kategori')
const bahan = document.getElementById('bahan')
const berat = document.getElementById('berat')
// const varian = document.getElementById('varian')
const deskripsi = document.getElementById('deskripsi')
const kode_barang = document.getElementById('kode_barang')
// const gambar = document.getElementById('gambar')
// const formData = FormData()

tambahData.addEventListener('submit', () => {
    // console.log(varian.value)
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nama: nama.value,
            harga_beli: harga_beli.value,
            harga_jual: harga_jual.value,
            kategori: kategori.value,
            bahan: bahan.value,
            berat: berat.value,
            // varian: varian.value,
            deskripsi: deskripsi.value,
            kode_barang: kode_barang.value,
            // gambar: gambar.value
        })
    })
    .then(res => res.json())
    .then(data => {
        const dataArr = []
        dataArr.push(data)
    })
})