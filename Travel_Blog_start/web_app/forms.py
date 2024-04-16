from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article, Plan


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Login",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=100, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title",
                            widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'title'}))
    content = forms.CharField(label="Content",
                              widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'content'}))

    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'})
        }


class PlanForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title",
                            widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'title'}))
    content = forms.CharField(label="Content",
                              widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'content'}))
    from_date = forms.DateTimeField(label="from date",
                                    widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}))
    to_date = forms.DateTimeField(label="to date",
                                  widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}))

    class Meta:
        model = Plan
        fields = ('title', 'content', 'from_date', 'to_date')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
        }
