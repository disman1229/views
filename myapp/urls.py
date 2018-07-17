from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('attribles/',views.attribles),
    path('get1/',views.get1),
    path('get2/',views.get2),
    path('showregist/',views.showregist),
    path('showregist/regist/',views.regist),
    # path('showresponse/',views.showresponse)
    path('cookietest/',views.cookietest),
    path('redirect1/',views.redirect1),
    path('redirect2/',views.redirect2),
    path('main/',views.main),
    path('login/',views.login),
    path('showmain/',views.showmain),
    path('quit/',views.quit)


]