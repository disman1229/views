from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('attribles/',views.attribles),
    path('get1/',views.get1),
    path('get2/',views.get2)
]