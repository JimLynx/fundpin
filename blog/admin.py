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
        'active',
    )
    list_filter = (
        'active',
        'created_on',
    )
    search_fields = (
        'name',
        'email',
        'body',
    )
    actions = ['approve_comments']

    def approve_comments(self, request, blog_description):
        blog_description.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
