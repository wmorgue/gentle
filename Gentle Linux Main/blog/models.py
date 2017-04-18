from django.db import models
from django.core.urlresolvers import reverse
# from django.db.models.signals import pre_save
# from django.utils.text import slugify


# def upload_location(instance, filename):
#     return "%s/%s" %(instance.id, filename)


class Post(models.Model):
    """Стандарная модель MVC MODEL VIEW CONTROLLER"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=100)
    image = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})

    class Meta():
        """Сортирует по времени.
        Вверху всегда свежие записи."""
        ordering = ['-created', '-updated']


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
# pre_save.connect(post_receiver, sender=Post)
