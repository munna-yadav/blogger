from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('blog/<int:id>/',views.blog_detail,name='blog_deatil_view')
]