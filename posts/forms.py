from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Что у вас нового?',
                'class': 'form-control'
            }),
        }
        labels = {
            'content': 'Текст поста',
            'image': 'Изображение'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Добавить комментарий...',
                'class': 'form-control'
            }),
        }
        labels = {
            'content': 'Ваш комментарий'
        }