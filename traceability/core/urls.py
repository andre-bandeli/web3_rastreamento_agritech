from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('lotes/', views.LoteFrangoListView.as_view(), name='lotefrango-list'),
    path('lotes/<int:pk>/', views.LoteFrangoDetailView.as_view(), name='lotefrango-detail'),
    path('lotes/novo/', views.LoteFrangoCreateView.as_view(), name='lotefrango-create'),
    path('lotes/<int:pk>/editar/', views.LoteFrangoUpdateView.as_view(), name='lotefrango-update'),
    path('lotes/<int:pk>/excluir/', views.LoteFrangoDeleteView.as_view(), name='lotefrango-delete'),
]