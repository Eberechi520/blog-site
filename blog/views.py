from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
# Create your views here.

def all_post(request):
    posts = Blog.objects.filter(status = 'published')

    context = {
        'section' : 'my_stories',
        'posts' : posts
    }

    return render(request, 'all_posts.html', context)

def post_detail(request, year, month, day, slug):

    post = get_object_or_404(Blog, slug=slug, status = 'published', date_created__year=year, date_created__month=month, date_created__day = day)

    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name') 
        main_comment =request.POST.get('comment')

        Comment.objects.create(f_name=f_name, l_name=l_name, comment=main_comment, blog=post)
    
    comment = post.comments.order_by('comment')
    context = {
        'section' : 'my_stories',
        'post' : post,
        'comments' : comment
    }

    return render(request, 'post_detail.html', context)



