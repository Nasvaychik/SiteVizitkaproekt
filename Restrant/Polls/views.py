from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return redirect('reg')
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, 'authorization.html', {'form': form})
    
class LoginView(View):
    def get(self, request):
        return redirect('reg')
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'authorization.html', {'form': form})

def reg(request):
    return render(request, 'authorization.html')

def index(request):
    return render(request, 'index.html')


class CartView(TemplateView):
    template_name = 'cart.html'
