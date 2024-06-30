from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views import generic 
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse ('I am Author')

class Register(CreateView):
    template_name = 'author/register.html'
    form_class = RegisterForm
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    success_url = reverse_lazy('register')
    
class Login(LoginView):
    template_name = 'author/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
@login_required 
def profile(request):
    return render(request,'author/profile.html')

# class UserLogout(LogoutView):
#     def get_success_url(self):
        
#         logout(self.request)
#         return reverse_lazy('home')
class UserLogout(generic.View):
    def get(self, request):
        logout(request)
        return redirect('home')