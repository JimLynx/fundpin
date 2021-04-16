from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from blog.models import Post, Comment
from .forms import CommentForm, BlogForm


def blog_list(request):
    """ return blog list page """

    blog_list = Post.objects.all()

    template = 'blog/blog_list.html'
    context = {
        'blogs': blog_list,
    }

    return render(request, template, context)


def blog_description(request, slug):
    """ return blog description page for each blog """

    blog_description = get_object_or_404(Post, slug=slug)
    comments = blog_description.comments.filter(
        active=True).order_by("-created_on")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_description
            new_comment.save()
            messages.success(request, (mark_safe("Thank you, your comment was succcessfully submitted."
                                                 "<br><br>It is awaiting admin approval (which can take up to 48 hours), "
                                                 "so please check back later.")))
            comment_form = CommentForm()
            return redirect(reverse('blog_description', args=[blog_description.slug]))
        else:
            messages.error(
                request, 'Failed to add comment. Please ensure the form is valid.')
    else:
        comment_form = CommentForm()

    template = 'blog/blog_description.html'
    context = {
        'blog_description': blog_description,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, template, context)


@login_required
def add_blog(request):
    """ Add a new blog post """

    form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
