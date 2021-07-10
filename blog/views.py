from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.utils.safestring import mark_safe
from django.core.paginator import Paginator

from blog.models import Post
from .forms import CommentForm, BlogForm


def blog_list(request):
    """ return blog list page """

    blog_list = Post.objects.all()

    # pagination
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    blog_list = paginator.get_page(page)

    template = 'blog/blog_list.html'
    context = {
        'blogs': blog_list,
    }

    return render(request, template, context)


def blog_description(request, slug):
    """ return blog description page for each blog """

    blog_description = get_object_or_404(Post, slug=slug)
    comments = blog_description.comments.order_by("-created_on")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = blog_description
            new_comment.save()
            messages.success(
                request, ("Thank you, your comment was successfully posted."))
            comment_form = CommentForm()

            return redirect(reverse(
                'blog_description',
                args=[blog_description.slug]))
        else:
            messages.error(
                request,
                'Failed to add comment. Please ensure the form is valid.')
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

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_description = form.save()
            messages.success(request, 'Successfully added a new Blog Post.')
            return redirect(
                reverse('blog_description', args=[blog_description.slug]))
        else:
            messages.error(
                request,
                'Failed to add a Blog Post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """ Edit a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog Post.')
            return redirect(reverse('blog_description', args=[blog.slug]))
        else:
            messages.error(
                request,
                'Failed to edit Blog Post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """ Delete an existing blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Post, slug=slug)
    blog.delete()

    messages.success(
        request, 'The selected blog post has '
        'successfully been deleted.')
    return redirect(reverse('blog'))
