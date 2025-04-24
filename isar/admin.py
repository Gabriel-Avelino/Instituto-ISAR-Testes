from django.contrib import admin
from .models import Documento, Tipo_Doc, Programa, ImagemPrograma, AreaAtuacao, Parceiro, Projeto, ImagemProjeto
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('name_doc', 'tipo')  # Campos visíveis na listagem
    list_filter = ('tipo',)  # Adiciona filtro por tipo
    search_fields = ('name_doc', 'tipo__name')  # Adiciona campo de busca

class ProjetoAdmin(SummernoteModelAdmin):
    pass

class ProgramaAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Tipo_Doc)
admin.site.register(AreaAtuacao)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(ImagemPrograma)
admin.site.register(Parceiro)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(ImagemProjeto)
