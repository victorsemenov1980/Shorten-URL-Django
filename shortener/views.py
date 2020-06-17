from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponsePermanentRedirect
from .forms import UrlForm
from .models import url

import string
import random

def short_random_string(n):

    return ''.join(random.SystemRandom().choice(
                    string.ascii_uppercase + \
                    string.ascii_lowercase + \
                    string.digits) for _ in range(n))

def index(request):
    if request.method == 'POST':
        
        form = UrlForm(request.POST)
        
        if form.is_valid():
           val={'url': form.cleaned_data['url']}
           hash_ = form.cleaned_data['hash_']
           if hash_:
                if url.objects.filter(custom=hash_).exists():
                     return render(request, 'index.html',{'error':"Provided hash value is already taken",'form':form})
                else:
                    val.update({'custom':hash_})
           else:
                hash_=short_random_string(5)
                val.update({'custom':hash_})
           url.objects.create(**val)
           return render(request,'result.html',{'link': hash_})
            

   
    else:
        form = UrlForm()
        return render(request, 'index.html',{'form': form})

def result(request):
    return render(request,'result.html')

def go(request,link):
    hash_=link
    go=get_object_or_404(url, custom=hash_)
    return HttpResponsePermanentRedirect(go.url)

