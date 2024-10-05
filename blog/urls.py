from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog_list),
    path('blog/', views.blog_detail),
]
