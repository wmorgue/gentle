from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Вывод в админку описание и автор, а так же поиск по описанию"""
    list_display = ['title', 'author', 'created', 'updated']
    list_display_links = ['updated']
    list_filter = ['created']
    list_editable = ['title']
    search_fields = ['title, text']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
