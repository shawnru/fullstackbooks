
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Book

def index(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, 'first_app/index.html', context)

def postresult(request):
    if request.method == 'POST':
        if request.POST['submit']:
             response_to_views = Book.objects.addbooks(request.POST)
            #  request.session['name'] = Book.objects.addbooks(postdat)
    return redirect('/')

# def session_test_1(request):
#     request.session['test'] = 'Session Vars Worked!'
#     return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)
#
# def session_test_2(request):
#     return http.HttpResponse('<br>'.join([
#         request.session.session_key,
#         request.GET.get('session'),
#         request.session.get('test', 'Session is Borked :(')
#          ]))
