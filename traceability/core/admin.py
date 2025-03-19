from django.contrib import admin
from .models import LoteFrango
from .blockchain import registrar_lote_na_blockchain


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
    def save_model(self, request, obj, form, change):
            super().save_model(request, obj, form, change)

            try:
                registrar_lote_na_blockchain(
                    obj.numero_lote,
                    obj.data_producao_abate,
                    obj.granja_origem,
                    obj.empresa_produtora
                )
            except Exception as e:
                self.message_user(request, f"Erro ao registrar lote na blockchain: {str(e)}", level='error')