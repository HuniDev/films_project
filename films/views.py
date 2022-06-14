from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Film


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'
    films_list = Film.objects.all()
    context = {'title': title,
                'films_list': films_list}
    return render(request, 'films/main.html', context)
    

def user_info(request):
    if request.method == 'Get':
     print('\n\nrequest.GET ==>>',
              request.GET,
              '\n\n')
    userinfo = {
        'username': 'Huni', # Put your name here
        'country': 'America', # Put your country here
    }
    context = {'userinfo': userinfo,
               'title': 'User Info Page'}
    
    return render(request,
                  'films/user_info.html',
                  context)

def user_form(request):
    if request.method == 'GET':
        context = {'title': 'User Form Page'}
        template = 'films/user_form.html'

        return render(request,
                      template,
                      context)
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        country = request.POST.get('country')
        request.session['username'] = username
        request.session['country'] = country

        return redirect(reverse('films:user_info'))

def details(request, id):
    film = Film.objects.get(id=id)
    # other query option:
    # film = Film.objects.filter(id=id)[0]
    context = {'film': film}
    return render(request, 'films/details.html', context)