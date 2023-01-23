from django.shortcuts import render, redirect
from .models import Localities
from .forms import LocalitiesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакты'})

def project(request):
        locs = Localities.objects.order_by('title')
        return render(request, 'main/project.html', {'locs': locs})

class LocsDetailView(DetailView):
    model = Localities
    template_name = 'main/details_loc.html'
    context_object_name = 'loc'

class LocsUpdateView(UpdateView):
    model = Localities
    template_name = 'main/create.html'
    form_class = LocalitiesForm

class LocsDeleteView(DeleteView):
    model = Localities
    success_url = '/project'
    template_name = 'main/locs-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = LocalitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
        else:
            error = 'Форма заполнена неверно!!!'
    form = LocalitiesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)