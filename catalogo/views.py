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

from django.contrib.auth.mixins import LoginRequiredMixin
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = ExemplarLivro
    template_name = 'catalogo/exemplares_emprestados_usuario.html'

    def get_queryset(self):
        return ExemplarLivro.objects.filter(usuario=self.request.user).filter(situacao__exact='e').order_by('data_devolucao')


import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

from catalogo.forms import RenovarLivroForm

@permission_required('catalogo.pode_renovar_emprestimo')
def renew_book(request, pk):
    book_instance = get_object_or_404(ExemplarLivro, pk=pk)

    if request.method == 'POST':
        form = RenovarLivroForm(request.POST)
        if form.is_valid():
            book_instance.data_devolucao = form.cleaned_data['data_renovacao']
            book_instance.save()
            return HttpResponseRedirect(reverse('meus-emprestimos'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenovarLivroForm(initial={'data_renovacao': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalogo/renovar_livro.html', context)
