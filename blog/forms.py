from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    """Простая форма с тремя полями автор, описание и текст."""
    class Meta:
        model = Post
        fields = [
            'author', 'title', 'text'
        ]
