from django.shortcuts import render

# Create your views here.

from catalogo.models import Genero, Linguagem, Autor, Livro, ExemplarLivro

def index(request):

    num_livros = Livro.objects.all().count()
    num_exemplares = ExemplarLivro.objects.all().count()

    num_exemplares_disponiveis = ExemplarLivro.objects.filter(situacao__exact='d').count()

    num_autores = Autor. objects.count()

    contexto = {
        'num_livros': num_livros,
        'num_exemplares': num_exemplares,
        'num_exemplares_disponiveis': num_exemplares_disponiveis,
        'num_autores': num_autores,
    }

    return render(request, 'index.html', context=contexto)