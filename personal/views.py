from django.shortcuts import render
from .models import Contact
from django.contrib import messages

def home_page(request):

    context = {
        'section' : 'home'
    }

    return render(request, "home.html", context)


def about_me(request):
    context = {
        'section' : 'about_me'
    }
    return render(request, 'about_me.html', context)


def contact(request):

    if request.method ==  'POST':
        print(request.POST)

        Contact.objects.create(name = request.POST['name'], email=request.POST['email'], message  = request.POST['message'])

        messages.success(request, "Your response has been recorded successfully!")


    context = {
        'section' : 'contact_me'
    }

    return render(request, 'contact.html', context)