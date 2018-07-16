from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    return render(request,'myapp/index.html')

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

def get1(request):
    a = request.GET.get("a")


def get2(request):
    pass