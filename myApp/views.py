from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    webpages_list = User.objects.all()
    date_dict ={'access_record': webpages_list}
    return render(request, 'myApp/myhtml.html', context=date_dict)
