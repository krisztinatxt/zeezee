from django.shortcuts import render, redirect


def about(request, *args, **kwargs):
    '''
    Render About me Page
    '''
    return render(request, "pages/about.html", {"page": "about"})


def contact(request, *args, **kwargs):
    '''
    Render contact form
    '''
    return render(request, "pages/contact.html", {"page": "contact"})


def success(request, *args, **kwargs):
    '''
    Render success message if the feedback was sent successfully
    '''
    return render(request, "pages/success-contact.html", {"page": "success"})


