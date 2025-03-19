from django.urls import path
from . import views
from .views import LoteFrangoDetailView, generate_qrcode


app_name = 'core'

urlpatterns = [
    path('lotes/', views.LoteFrangoListView.as_view(), name='lotefrango-list'),
    path('lotes/<int:pk>/', views.LoteFrangoDetailView.as_view(), name='lotefrango-detail'),
    path('lotes/novo/', views.LoteFrangoCreateView.as_view(), name='lotefrango-create'),
    path('lotes/<int:pk>/editar/', views.LoteFrangoUpdateView.as_view(), name='lotefrango-update'),
    path('lotes/<int:pk>/excluir/', views.LoteFrangoDeleteView.as_view(), name='lotefrango-delete'),
    path('lote/<int:pk>/', LoteFrangoDetailView.as_view(), name='lote-detail'),
    path('lote/<int:pk>/qrcode/', generate_qrcode, name='lote-qrcode'),
]