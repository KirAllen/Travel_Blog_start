from django.shortcuts import render
import logging
from .forms import LoginForm, RegisterUserForm, PlanForm, ArticleForm
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.decorators import login_required
from .models import Article


logger = logging.getLogger(__name__)


# Главныя странца
def index(request):
    logger.info('Index page accessed')
    return render(request, 'web_app/home.html')


# Страница "О нас"
def about(request):
    logger.info('About page accessed')
    return render(request, 'web_app/about.html')


# Функция входа
def loging(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            logger.info(f'Получили {user=}.')
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    return render(request, 'web_app/loging.html', {'form': form})


# Функция выхода
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('loging'))


# Это, вообще, клас, но внутри функция регистрации на сайте
class RegisterUser(FormView):
    form_class = RegisterUserForm
    template_name = 'web_app/registration.html'
    success_url = reverse_lazy('loging')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Фунцкия отображения страницы создания плана приключений
@login_required
def plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f'Получили {form=}')
        else:
            return 'ERROR'
    form = PlanForm()
    return render(request, 'web_app/plan.html', {'form': form})

# Фунцкия отображения страницы ретроспективы приключений
@login_required
def diary(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f'Получили {form=}')
        else:
            return 'ERROR'
    form = ArticleForm()
    return render(request, 'web_app/diary.html', {'form': form})

@login_required
def canban(request): 
    articles = Article.objects.all()
    return render(request, 'web_app/canban.html', {'articles' : articles})

