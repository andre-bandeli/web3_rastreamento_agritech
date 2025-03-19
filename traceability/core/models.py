from django.db import models
from django.utils import timezone
from django.urls import reverse

from .blockchain import registrar_lote_na_blockchain


class LoteFrango(models.Model):
    """
    Informações relevantes de rastreabilidade.
    """
    numero_lote = models.CharField(max_length=50, unique=True, verbose_name="Número do Lote")
    data_producao_abate = models.DateField(verbose_name="Data de Produção/Abate")
    granja_origem = models.CharField(max_length=100, verbose_name="Granja de Origem")
    empresa_produtora = models.CharField(max_length=100, verbose_name="Empresa Produtora")
    data_cadastro = models.DateTimeField(default=timezone.now, verbose_name="Data de Cadastro")

    # Qualidade da Carne
    orgao_inspecao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Órgão de Inspeção Sanitária")
    resultados_analises = models.TextField(blank=True, null=True, verbose_name="Resultados de Análises")
    prazo_validade = models.DateField(verbose_name="Prazo de Validade")
    condicoes_conservacao = models.TextField(verbose_name="Condições de Conservação")

    # Vacinas e Sanidade Animal
    historico_vacinacao = models.TextField(blank=True, null=True, verbose_name="Histórico de Vacinação")
    status_sanitario_granja = models.CharField(max_length=100, blank=True, null=True, verbose_name="Status Sanitário da Granja")
    medidas_biosseguridade = models.TextField(blank=True, null=True, verbose_name="Medidas de Biosseguridade")
    manejo_sanitario = models.TextField(blank=True, null=True, verbose_name="Manejo Sanitário")

    # Ambiente Animal e Bem-Estar
    densidade_alojamento = models.IntegerField(blank=True, null=True, verbose_name="Densidade de Alojamento (aves/m²)")
    temperatura_galpao = models.CharField(max_length=20, blank=True, null=True, verbose_name="Temperatura do Galpão (°C)")
    umidade_galpao = models.CharField(max_length=20, blank=True, null=True, verbose_name="Umidade do Galpão (%)")
    sistema_ventilacao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sistema de Ventilação")
    iluminacao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Iluminação")
    acesso_agua_alimento = models.BooleanField(default=True, verbose_name="Acesso Adequado à Água e Alimento")
    estrutura_galpao = models.TextField(blank=True, null=True, verbose_name="Estrutura do Galpão")
    manejo_bem_estar = models.TextField(blank=True, null=True, verbose_name="Práticas de Manejo para Bem-Estar Animal")

    # Informações Adicionais (Opcionais)
    tipo_racao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de Ração")
    abatedouro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Abatedouro")
    certificacoes = models.TextField(blank=True, null=True, verbose_name="Certificações")
    contato_duvidas = models.CharField(max_length=200, blank=True, null=True, verbose_name="Contato para Dúvidas")

    def __str__(self):
        return self.numero_lote

    class Meta:
        verbose_name = "Lote de Frango"
        verbose_name_plural = "Lotes de Frango"
        ordering = ['-data_producao_abate']
    
    def get_absolute_url(self):
        return reverse('lote-detail', args=[str(self.pk)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            registrar_lote_na_blockchain(
                self.numero_lote,
                self.data_producao_abate,
                self.granja_origem,
                self.empresa_produtora
            )
        except Exception as e:
            print(f"Erro ao registrar lote na blockchain: {str(e)}")