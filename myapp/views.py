from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

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
    b = request.GET.get("b")
    c = request.GET.get("c")
    return HttpResponse( a +" "+ b +" "+ c )


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get("c")
    return HttpResponse(a1 + " " + a2 + " " + c)

#POST
def showregist(request):
    return render(request,'myapp/regist.html')
def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("12312")

# #showresponse
# def showresponse(request):
#     res = HttpResponse()
#     res.content = b'good'
#     print(res.content)
#     print(res.charset)
#     print(res.status_code)
#     print(res.content-type)
#     return res


def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["disman"]+"<h1/>")
    # cookie = res.set_cookie("disman","good")
    return res


#重定向
def redirect1(request):
    # return HttpResponseRedirect('/redirect2')
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向视图")
