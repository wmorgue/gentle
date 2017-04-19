from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Вывод в админку описания, автора, поиск по описанию.
    Редактирование описания"""
    list_display = ['title', 'author', 'created', 'updated']
    list_display_links = ['updated']
    list_filter = ['created']
    list_editable = ['title']
    search_fields = ['title, text']
    # prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
