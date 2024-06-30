from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models
from . import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





# Create your views here.
def index(request):
    return HttpResponse('This is Album App')


@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    template_name = 'album/create.html'
    model = models.Album
    form_class = forms.AlbumForm
    def form_valid(self, form):
        messages.success(self.request,"Album Create Success full")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,'Sorry Album Create Unsuccessful')
        return super().form_invalid(form)
    success_url= reverse_lazy("add_album")
    
@method_decorator(login_required, name='dispatch')

class EditAlbum(UpdateView):
    template_name = 'album/edit.html'
    pk_url_kwarg = 'pk'
    model = models.Album
    form_class = forms.AlbumForm
    success_url= reverse_lazy("add_album")
    
class DeleteAlbum(DeleteView):
    model = models.Album
    template_name = 'album/delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
          
        