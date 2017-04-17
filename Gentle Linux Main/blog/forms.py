from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    """Простая форма с тремя полями: автор, описание, текст и загрузка изображения.
    Добавляется во вьюху в виде функции и не только."""
    class Meta:
        model = Post
        fields = ['author', 'title', 'image', 'text']
