from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LoteFrango
from io import BytesIO
from django.urls import reverse
from django.http import HttpResponse

import qrcode


class LoteFrangoListView(ListView):
    model = LoteFrango
    template_name = 'core/templates/lotefrango_list.html'
    context_object_name = 'lotes'

class LoteFrangoDetailView(DetailView):
    model = LoteFrango
    template_name = 'core/lotefrango_detail.html'
    context_object_name = 'lote'

class LoteFrangoCreateView(CreateView):
    model = LoteFrango
    template_name = 'core/templates/lotefrango_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:lotefrango-list')

class LoteFrangoUpdateView(UpdateView):
    model = LoteFrango
    template_name = 'core/templates/lotefrango_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:lotefrango-list')

class LoteFrangoDeleteView(DeleteView):
    model = LoteFrango
    template_name = 'core/templates/lotefrango_confirm_delete.html'
    success_url = reverse_lazy('core:lotefrango-list')

def generate_qrcode(request, pk):
    lote_url = request.build_absolute_uri(reverse('core:lote-detail', args=[pk]))
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(lote_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return HttpResponse(buffer, content_type="image/png")