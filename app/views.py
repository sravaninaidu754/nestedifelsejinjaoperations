from django.shortcuts import render

# Create your views here.
def nested(request):
    d={'a':200,'b':400,'c':800}
    return render(request,'nestedifelse.html',d)
