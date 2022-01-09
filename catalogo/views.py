from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalogo.models import Genero, Linguagem, Autor, Livro, ExemplarLivro


def index(request):
    num_livros = Livro.objects.all().count()
    num_exemplares = ExemplarLivro.objects.all().count()

    num_exemplares_disponiveis = ExemplarLivro.objects.filter(situacao__exact='d').count()

    num_autores = Autor.objects.count()

    num_visitas = request.session.get('num_visitas',1)
    request.session['num_visitas'] = num_visitas + 1

    contexto = {
        'num_livros': num_livros,
        'num_exemplares': num_exemplares,
        'num_exemplares_disponiveis': num_exemplares_disponiveis,
        'num_autores': num_autores,
        'num_visitas': num_visitas
    }

    return render(request, 'index.html', context=contexto)


class BookListView(generic.ListView):
    model = Livro


class BookDetailView(generic.DetailView):
    model = Livro
