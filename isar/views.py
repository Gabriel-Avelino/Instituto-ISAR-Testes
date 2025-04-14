from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Documento
from django.views.decorators.http import require_GET
from blog.models import Post, ImagemNoticia
from collections import OrderedDict
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def index(request):
    noticias = Post.objects.all().order_by('-criado_em')
    noticias_list = list()
    for n in noticias:
        noticias_list.append(n)

    ultimo_index = len(noticias_list)
    penultimo_index = ultimo_index - 1

    return render(request, 'index.html', {'noticias': noticias, 'ultimo_index': ultimo_index, 'penultimo_index': penultimo_index})

def sobreNos(request):
    return render(request, 'about.html')

'''     
def imoveis(request):
    imoveis = Imovel.objects.all()
    estados = Estado.objects.all()
    tipos = Tipo.objects.all()
    return render(request, 'imoveis.html', {'imoveis': imoveis, 'estados': estados, 'tipos':tipos})

def imovel(request, id):
    imovel = Imovel.objects.get(id=id)
    sugestoes = Imovel.objects.filter(tipo=imovel.tipo, cidade=imovel.cidade, estado=imovel.estado, bairro=imovel.bairro, regiao=imovel.regiao).filter(~Q(id=imovel.id))
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestions': sugestoes})
'''  

def transparencia(request):
    # Cria um OrderedDict para garantir a ordem dos dropdowns
    ordered_documents = OrderedDict([
        ("Alvará de Funcionamento", []),
        ("Atestados de Capacidade Técnica", []),
        ("Regularidade Fiscal Matriz - São Paulo/SP", []),
        # Adicione mais tipos de documentos conforme necessário
    ])
    
    documentos = Documento.objects.all()
    
    # Organiza os documentos de acordo com o tipo esperado
    for document in documentos:
        tipo_documento = document.tipo.name
        # Verifica se o tipo de documento está nos tipos ordenados
        if tipo_documento in ordered_documents:
            ordered_documents[tipo_documento].append(document)
        else:
            # Se o tipo de documento não estiver na lista ordenada, adiciona no final
            ordered_documents[tipo_documento] = [document]

    return render(request, 'transparencia.html', {'documentos': ordered_documents.items()})

def noticias(request):
    posts = Post.objects.all().order_by('-criado_em')
    destaques = posts[:3]
    outros = posts[3:]
    return render(request, 'noticias.html',{'noticias': posts, 'destaques': destaques, 'outros': outros})

def contato(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        send_mail(
            'Mensagem de {}: {}'.format(name, assunto),
            'Nome: {} \nEmail: {} \nTelefone: {} \nAssunto: {} \nMensagem: {}'.format(name, email, telefone, assunto, mensagem),
            "ti@institutoisar.com.br",
            ["administrativo@institutoisar.com.br"],
            fail_silently=False,
        )
        messages.success(request, 'Formulário enviado com sucesso!')
        return redirect('contato')
    else:
        return render(request, 'contato.html')
    
def noticia(request, id):
    post = Post.objects.get(id=id)
    posts = Post.objects.filter(~Q(id=post.id)).order_by('-criado_em')
    sugestoes = posts[:3]
    current_url = request.build_absolute_uri()
    fotos = ImagemNoticia.objects.filter(noticia=post)
    return render(request, 'noticia.html',{'post': post, 'sugestoes': sugestoes, 'current_url': current_url, 'fotos': fotos})

'''
@require_GET
def get_options(request):
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    regiao = request.GET.get('regiao')

    opcoes = ''

    if estado:
        try: 
            selectestado = Estado.objects.get(name=estado)
            opcoes = list(Imovel.objects.filter(estado=selectestado).values_list('cidade__name', flat=True))
        except Imovel.DoesNotExist:
            return JsonResponse({'error': 'Cidades não encontradas'}, status=404)
        
    if cidade:
        try:
            selectcidade = Cidade.objects.get(name=cidade)
            opcoes = list(Imovel.objects.filter(estado=selectestado, cidade=selectcidade).values_list('regiao__name', flat=True))
        except Imovel.DoesNotExist:
            return JsonResponse({'error': 'Regiões não encontradas'})
        
    if regiao:
        try:
            selectregiao = Regiao.objects.get(name=regiao)
            opcoes = list(Imovel.objects.filter(estado=selectestado, cidade=selectcidade, regiao=selectregiao).values_list('bairro__name', flat=True))
        except Imovel.DoesNotExist:
            return JsonResponse({'error': 'Bairros não encontrados'})   
         
    return JsonResponse({'opcoes': opcoes})  

@require_GET
def get_imoveis(request):
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    regiao = request.GET.get('regiao')
    bairro = request.GET.get('bairro')
    
     # Inicia o queryset com todos os imóveis
    imoveis = Imovel.objects.all()

    # Aplica os filtros apenas se os valores estiverem presentes
    if estado:
        try:
            selectestado = Estado.objects.get(name=estado)
            imoveis = list(Imovel.objects.filter(estado=selectestado).values('id', 'foto', 'tipo__name', 'name', 'cidade__name', 'estado__name', 'regiao__name', 'bairro__name'))
        except Estado.DoesNotExist:
            return JsonResponse({'error': 'Estado não encontrado'}, status=404)

    if cidade:
        try:
            selectcidade = Cidade.objects.get(name=cidade)
            imoveis = list(Imovel.objects.filter(estado=selectestado, cidade=selectcidade).values('id', 'foto', 'tipo__name', 'name', 'cidade__name', 'estado__name', 'regiao__name', 'bairro__name'))
        except Cidade.DoesNotExist:
            return JsonResponse({'error': 'Cidade não encontrada'}, status=404)

    if regiao:
        try:
            selectregiao = Regiao.objects.get(name=regiao)
            imoveis = list(Imovel.objects.filter(estado=selectestado, cidade=selectcidade, regiao=selectregiao).values('id', 'foto', 'tipo__name', 'name', 'cidade__name', 'estado__name', 'regiao__name', 'bairro__name'))
        except Regiao.DoesNotExist:
            return JsonResponse({'error': 'Região não encontrada'}, status=404)

    if bairro:
        try:
            selectbairro = Bairro.objects.get(name=bairro)
            imoveis = list(Imovel.objects.filter(estado=selectestado, cidade=selectcidade, regiao=selectregiao, bairro=selectbairro).values('id', 'foto', 'tipo__name', 'name', 'cidade__name', 'estado__name', 'regiao__name', 'bairro__name'))
        except Bairro.DoesNotExist:
            return JsonResponse({'error': 'Bairro não encontrado'}, status=404)
    return JsonResponse({'imoveis': imoveis})

@require_GET
def reset_filtro(request):
    imoveis = list(Imovel.objects.values('id', 'foto', 'tipo__name', 'name', 'cidade__name', 'estado__name', 'regiao__name', 'bairro__name'))
    estados = list(Estado.objects.values_list('name', flat=True))
    tipos = list(Tipo.objects.values_list('name', flat=True))

    return JsonResponse({'imoveis': imoveis, 'estados': estados, 'tipos': tipos}) 
'''