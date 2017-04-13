from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Стандарная модель"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish_recent(self):
        return self.published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title
