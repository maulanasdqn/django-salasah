from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *

class ProdukModelForm(BSModalModelForm):
    class Meta:
        model = Produk
        fields = "__all__"