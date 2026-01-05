from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm


@login_required
def home(request):
    """Главная страница с лентой постов"""
    posts = Post.objects.all().select_related('author')
    return render(request, 'posts/home.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    """Детальная страница поста"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().select_related('author')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def create_post(request):
    """Создание нового поста"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Пост успешно создан!')
            return redirect('posts:home')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def like_post(request, pk):
    """Лайк/анлайк поста"""
    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        # Если лайк уже существует - удаляем (анлайк)
        like.delete()
        messages.info(request, 'Лайк удален')
    else:
        messages.success(request, 'Посту понравилось!')

    return redirect('posts:home')


@login_required
def delete_comment(request, pk):
    """Удаление комментария"""
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk  # Сохраняем ID поста для редиректа

    # Проверяем, что пользователь - автор комментария или автор поста
    if request.user == comment.author or request.user == comment.post.author:
        comment.delete()
        messages.success(request, 'Комментарий удален!')
    else:
        messages.error(request, 'Вы не можете удалить этот комментарий!')

    return redirect('posts:post_detail', pk=post_pk)