from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     context = {'this_is': 'latest_question_list'}
     return render(request, 'myApp/myhtml.html', context)
