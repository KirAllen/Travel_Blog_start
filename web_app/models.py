from django.db import models


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # article_id = models.ForeignKey()


class Article(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)


class Plan(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=700)
    created_at = models.DateTimeField()


