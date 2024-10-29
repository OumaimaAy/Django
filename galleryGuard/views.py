from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html') 

def gallery(request):
    return render(request, 'gallery.html') 

def events(request):
    return render(request, 'event.html') 

def ticket(request):
    return render(request, 'ticket.html') 

def blog_home(request):
    return render(request, 'blog-home.html') 
    
def contact (request):
    return render(request, 'contact.html') 