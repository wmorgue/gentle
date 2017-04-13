from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Вывод в админку описание и автор, а так же поиск по описанию"""
    list_display = ('title', 'author', 'created')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
