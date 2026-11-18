from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post,AboutUs
from .forms import ContactForm
import logging


# Home Page
def index(request):
    blog_title = "Latest Posts"

    all_posts = Post.objects.all().order_by('-id')

    # Pagination
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'blog_title': blog_title,
        'page_object': page_object
    }

    return render(request, 'index.html', context)


# Post Detail Page
def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)

        related_posts = (
            Post.objects.filter(category=post.category)
            .exclude(pk=post.id)
        )

    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    context = {
        'post': post,
        'related_posts': related_posts
    }

    return render(request, 'details.html', context)


# Redirect Example
def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))


# New URL View
def new_url(request):
    return HttpResponse("This is the new URL")


# Contact Form View
def contact_view(request):
    logger = logging.getLogger("TESTING")

    form = ContactForm()
    name = ''
    email = ''
    message = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            logger.debug(
                f"Post data is : {name}  {email} {message}"
            )

            success_message = "Your mail is sent!"

            return render(
                request,
                'contact.html',
                {
                    'form': form,
                    'success_message': success_message
                }
            )

        else:
            logger.debug("Form validation failed")

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'name': name,
            'email': email,
            'message': message
        }
    )
def about_view(request):
    about_content=AboutUs.objects.first().content
    return render(request,'about.html',{'about_content':about_content})
    