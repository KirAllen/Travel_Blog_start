from django.db import models



# class User(models.Model):
#     id = models.IntegerField(unique=True, primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     # article_id = models.ForeignKey()


class Article(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    # user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Запись: {self.title}'
    
    # class Meta: 
    #     verbose_name = 'Запись'
    #     verbose_name_plural = 'Записи'


class Plan(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    def __str__(self):
        return self.title
