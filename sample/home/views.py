from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Detail_form
from .models import Detail

from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60)
def index(request):
    q = Detail.objects.all()
    return render(request,'home/index.html',{'q':q})

def signup(request):
    form = Detail_form()
    if request.method == 'POST':
        form = Detail_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong""")
    else:
        return render(request,'home/signup.html',{'form':form})

def update(request,detail_id):
    try:
        q = Detail.objects.get(id=detail_id)
    except:
        return redirect('index')
    form = Detail_form(request.POST or None , instance=q)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'home/signup.html',{'form':form})
       