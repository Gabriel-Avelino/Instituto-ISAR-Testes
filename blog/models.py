from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from unicodedata import normalize
import datetime
import uuid 

def uploadImageFormaterNoticias(instance, filename):
    return 'fotos/{}/{}-{}'.format(datetime.date.today(), str(uuid.uuid4()), filename)

def uploadImageFormater(instance, filename):
    return 'thumbs/{}-{}'.format(str(uuid.uuid4()), filename)

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name

class Post (models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    foto = models.ImageField(upload_to=uploadImageFormater)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    resumo = models.TextField(blank=False, null=False)
    conteudo = models.TextField(blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if self.foto and self.foto.name:
            self.foto.name = normalize('NFKD', self.foto.name).encode('ascii', 'ignore').decode('ascii')
        super(Post, self).save(*args, **kwargs)
    
class ImagemNoticia(models.Model):
    file = models.FileField(upload_to= uploadImageFormaterNoticias)
    descricao = models.TextField()
    noticia = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name_plural = 'Imagens noticias'
