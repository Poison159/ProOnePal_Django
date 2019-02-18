from django.shortcuts import render,render_to_response
from SiyApp.models  import Team

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def generic(request):
    my_dict = {'data': Team.objects.all()}
    return render(request,'generic.html',context=my_dict)



