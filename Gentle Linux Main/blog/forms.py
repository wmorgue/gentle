from django import forms


from pagedown.widgets import PagedownWidget
from .models import Post


class CreateForm(forms.ModelForm):
    """Простая форма с тремя полями: автор, описание, текст, загрузка изображения,
    А так же отмена публикации - draft.
    Добавляется во вьюху в виде функции и не только.
    Форму можно сделать во вьюхе, а не этим отдельным файлом."""
    text = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = ['author', 'title', 'image', 'text','draft', 'publish']
