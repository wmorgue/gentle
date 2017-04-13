from django.db import models


class Post(models.Model):
    """Стандарная модель MVC MODEL VIEW CONTROLLER"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
