from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LoteFrango

class LoteFrangoListView(ListView):
    model = LoteFrango
    template_name = 'core/lotefrango_list.html'
    context_object_name = 'lotes'

class LoteFrangoDetailView(DetailView):
    model = LoteFrango
    template_name = 'core/lotefrango_detail.html'
    context_object_name = 'lote'

class LoteFrangoCreateView(CreateView):
    model = LoteFrango
    template_name = 'core/lotefrango_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:lotefrango-list')

class LoteFrangoUpdateView(UpdateView):
    model = LoteFrango
    template_name = 'core/lotefrango_form.html'
    fields = '__all__'
    success_url = reverse_lazy('core:lotefrango-list')

class LoteFrangoDeleteView(DeleteView):
    model = LoteFrango
    template_name = 'core/lotefrango_confirm_delete.html'
    success_url = reverse_lazy('core:lotefrango-list')