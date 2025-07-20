from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import RegisterForm, AvatarForm
from .models import Avatar

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')
 
    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        if user:
            login(self.request, user)
        return response
    
class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html' 

    def get_success_url(self):
        return reverse_lazy('inicio')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProfileView(DetailView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class AvatarUpdateView(UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'usuarios/avatar_form.html'
    
    def get_object(self, queryset=None):
        # Obtiene o crea el avatar asociado al usuario actual
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar


class ProfileUpdateView(UpdateView):
    model = User
