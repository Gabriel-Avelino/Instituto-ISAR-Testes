from django.contrib.auth.models import User
from django.db import models
import uuid 
from unicodedata import normalize

# Create your models here.
def uploadFotoPrograma(instance, filename):
    if isinstance(instance, Programa):
        nome_programa = instance.name
    else:
        nome_programa = instance.programa.name
    return 'programas/{}/{}-{}'.format(normalize('NFKD', nome_programa).encode('ascii', 'ignore').decode('ascii'), str(uuid.uuid4()), filename)

def uploadFotoArea(instance, filename):
    return 'areas/{}-{}'.format(str(uuid.uuid4()), filename)

def uploadFotoParceiro(instance, filename):
    return 'parceiros/{}-{}'.format(str(uuid.uuid4()), filename)

def uploadFotoProjeto(instance, filename):
    if isinstance(instance, Projeto):
        nome_projeto = instance.name
    else:
        nome_projeto = instance.projeto.name
    return 'projetos/{}/{}-{}'.format(normalize('NFKD', nome_projeto).encode('ascii', 'ignore').decode('ascii'), str(uuid.uuid4()), filename)

class Tipo_Doc(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tipos docs'

class Documento (models.Model):
    name_doc = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo_Doc, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name_doc
    
    def save(self, *args, **kwargs):
        self.file.name = normalize('NFKD', self.file.name).encode('ascii', 'ignore').decode('ascii')
        existing_doc = Documento.objects.filter(name_doc=self.name_doc, tipo=self.tipo).first()
        
        if existing_doc:
            existing_doc.file.delete(save=False)  # Delete the old file from disk
            existing_doc.file = self.file  # Update the file with the new one
            existing_doc.tipo = self.tipo  # Update tipo if necessary
            super(Documento, existing_doc).save(*args, **kwargs)  # Save the existing document
        else:
            super(Documento, self).save(*args, **kwargs)
    
class AreaAtuacao(models.Model):
    name = models.CharField(max_length=256, unique=True)
    foto = models.FileField(upload_to=uploadFotoArea)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Areas Atuacao'
    
class Programa(models.Model):
    name = models.CharField(max_length=256, unique=True)
    foto = models.FileField(upload_to=uploadFotoPrograma)
    descricao = models.TextField(blank=True, null=True)
    areasAtuacao = models.ManyToManyField(AreaAtuacao, related_name='programas')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Programas'
    
class ImagemPrograma(models.Model):
    file = models.FileField(upload_to= uploadFotoPrograma)
    descricao = models.TextField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name_plural = 'Imagens Programas'

class Parceiro(models.Model):
    name = models.CharField(max_length=256, unique=True)
    foto = models.FileField(upload_to=uploadFotoParceiro)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Parceiros'

class Projeto(models.Model):
    name = models.CharField(max_length=256, unique=True)
    foto = models.FileField(upload_to=uploadFotoProjeto)
    descricao = models.TextField(blank=True, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    objetivos = models.TextField(blank=True, null=True)
    parceiros = models.ManyToManyField(Parceiro, related_name='projetos')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Projetos'
    
class ImagemProjeto(models.Model):
    file = models.FileField(upload_to= uploadFotoProjeto)
    descricao = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name_plural = 'Imagens Projetos'
