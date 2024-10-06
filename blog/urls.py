from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog_list),
    path('post/<int:id>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
]
