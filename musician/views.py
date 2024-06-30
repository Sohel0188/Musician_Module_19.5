from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView
from .models import Musician
from .forms import MusicianForm
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
def index(request):
    return HttpResponse('This is Musician App')

class AddMusician(CreateView):
    template_name = 'musician/create.html'
    model = Musician
    form_class = MusicianForm
    def form_valid(self, form):
        messages.success(self.request, 'Add Musician Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Sorry Musician Didnot add')
        return super().form_invalid(form)
    success_url = reverse_lazy('add_musician')

class EditMusician(UpdateView):
    template_name = 'musician/edit.html'
    model = Musician
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    
    
# def add_musician(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_musician')
#     else:
#         form = MusicianForm()
#     # print(form)
#     return render(request,'add_musician.html',{'form': form})
          