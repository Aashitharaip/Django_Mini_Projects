from django.shortcuts import render
import requests
from .models import Contact,Messages
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def jokes(request):
    API= 'https://api.chucknorris.io/jokes/random'
    response = requests.get(API)

    if response.status_code == 200:
        json_data = response.json()
        joke = json_data.get('value')
    else:
        joke = 'Sorry, could not fetch the joke at this time!.'

    context = {'joke':joke}
    return render(request,'jokes.html',context)

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        p = Contact(full_name=full_name,email=email,message=message)
        p.save()
        return render(request,'contactus.html')
    else:
        return render(request,'contactus.html')
    
def pastebin(request):
    context= dict()
    if request.method == 'POST':
        message = request.POST.get('message')
        code = request.POST.get('code')
        burn = request.POST.get('burn')
        if (burn == 'on'):
            burn = True
        else:
            burn = False
        if not Messages.objects.filter(code=code).exists():
            m = Messages(message=message,code=code,burn=burn)
            m.save()
            context['success']=True
            context['url']=f'pastebin/{code}'
        return render(request,'pastebin.html',context)
    else:
        return render(request,'pastebin.html')
    
def pastebin_output(request,code):
    try:
        paste = Messages.objects.get(code=code)
        context = {'paste':paste}
        return render(request,'pastebin-output.html',context)

    except Messages.DoesNotExist:
        return HttpResponse('Enter a valid code')
    

    


     
