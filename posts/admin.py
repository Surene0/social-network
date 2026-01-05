from django.contrib import admin
from .models import Post, Like, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content_short', 'created_at', 'likes_count', 'comments_count')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__email')
    date_hierarchy = 'created_at'

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_short.short_description = 'Содержание'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_short', 'content_short', 'created_at')
    list_filter = ('created_at', 'author')

    def post_short(self, obj):
        return obj.post.content[:30] + '...' if len(obj.post.content) > 30 else obj.post.content

    post_short.short_description = 'Пост'

    def content_short(self, obj):
        return obj.content[:30] + '...' if len(obj.content) > 30 else obj.content

    content_short.short_description = 'Комментарий'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_short', 'created_at')
    list_filter = ('created_at', 'user')

    def post_short(self, obj):
        return obj.post.content[:30] + '...' if len(obj.post.content) > 30 else obj.post.content

    post_short.short_description = 'Пост'