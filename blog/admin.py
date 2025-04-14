from django.contrib import admin
from .models import Categoria, Post, ImagemNoticia
from django.conf import settings
from django.forms.widgets import Media
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from django_summernote.utils import get_theme_files

class PostAdmin(SummernoteModelAdmin):
    pass

class AuthorAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    # For non-bootstrapped admin site,
    # JavaScript and CSS files should be imported manually like below.
    @property
    def media(self):
        media = super().media + Media(
            js = get_theme_files(settings.SUMMERNOTE_THEME, 'base_js'),
            css = {
            'all': get_theme_files(settings.SUMMERNOTE_THEME, 'base_css'),
        })
        return media
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post, PostAdmin)
admin.site.register(ImagemNoticia)
