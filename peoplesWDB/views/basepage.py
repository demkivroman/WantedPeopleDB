from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def base(request):
    return render(request,'base.html',{})
