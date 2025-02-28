from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def updates(request):
    return render(request, 'updates.html')

def cv_page(request):
    return render(request, 'cv_page.html')

def certificate(request):
    return render(request, 'certificate.html')

def about(request):
    return render(request, 'about.html')

def social(request):
    return render(request, 'social.html')

def email(request):
    return render(request, 'email.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('q')
    results = []  # Replace with actual search logic
    return render(request, 'search_results.html', {'query': query, 'results': results})
