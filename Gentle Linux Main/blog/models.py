from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class PostManager(models.Manager):
    """Simple PostManager for publish__lte.
    Look views def index for more detail."""

    def active(self):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Post(models.Model):
    """Стандарная модель MVC MODEL VIEW CONTROLLER"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    # slug = models.SlugField(unique=True ,max_length=100)
    image = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    text = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})

    # def upload_location(instance, filename):
    #     return "%s/%s" %(instance.id, filename)

    class Meta():
        """Сортирует по времени.
        Вверху всегда свежие записи."""
        ordering = ['-created', '-updated']
