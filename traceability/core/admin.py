from django.contrib import admin
from .models import LoteFrango

@admin.register(LoteFrango)
class LoteFrangoAdmin(admin.ModelAdmin):
    list_display = ('numero_lote', 'data_producao_abate', 'granja_origem', 'empresa_produtora', 'data_cadastro')
    list_filter = ('data_producao_abate', 'granja_origem', 'empresa_produtora')
    search_fields = ('numero_lote', 'granja_origem', 'empresa_produtora')
    date_hierarchy = 'data_producao_abate'
    ordering = ('-data_producao_abate',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero_lote', 'data_producao_abate', 'granja_origem', 'empresa_produtora', 'data_cadastro')
        }),
        ('Qualidade da Carne', {
            'fields': ('orgao_inspecao', 'resultados_analises', 'prazo_validade', 'condicoes_conservacao')
        }),
        ('Vacinas e Sanidade Animal', {
            'fields': ('historico_vacinacao', 'status_sanitario_granja', 'medidas_biosseguridade', 'manejo_sanitario')
        }),
        ('Ambiente Animal e Bem-Estar', {
            'fields': ('densidade_alojamento', 'temperatura_galpao', 'umidade_galpao', 'sistema_ventilacao', 'iluminacao', 'acesso_agua_alimento', 'estrutura_galpao', 'manejo_bem_estar')
        }),
        ('Informações Adicionais', {
            'fields': ('tipo_racao', 'abatedouro', 'certificacoes', 'contato_duvidas')
        }),
    )