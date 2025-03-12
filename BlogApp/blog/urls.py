from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path("create/",views.create_blog, name="create_blog"),
    path('<int:id>/',views.blog_detail,name='blog_detail_view'),
    path('<int:blog_id>/edit',views.edit_blog, name="edit_blog"),
    path('<int:blog_id>/delete',views.delete_blog, name="delete_blog"),
    path('<int:blog_id>/comment', views.create_comment, name='create_comment'),
    path('profile/',views.profile_view, name='profile_view')
]