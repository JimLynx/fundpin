from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'is_featured',
        'created_on',
        'image',
    )
    list_filter = ("status",)
    list_editable=('status', 'is_featured')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'post',
        'created_on',
    )
    list_filter = (
        'created_on',
    )
    search_fields = (
        'name',
        'body',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
