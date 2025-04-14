from django.contrib import admin
from .models import Documento, Tipo_Doc, Programa, ImagemPrograma, AreaAtuacao, Parceiro, Projeto, ImagemProjeto

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('name_doc', 'tipo')  # Campos visíveis na listagem
    list_filter = ('tipo',)  # Adiciona filtro por tipo
    search_fields = ('name_doc', 'tipo__name')  # Adiciona campo de busca

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tipo_Doc)
admin.site.register(AreaAtuacao)
admin.site.register(Programa)
admin.site.register(ImagemPrograma)
admin.site.register(Parceiro)
admin.site.register(Projeto)
admin.site.register(ImagemProjeto)
