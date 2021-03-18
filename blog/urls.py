from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # Ex.: /
    path('', views.post_list, name='post_list'),
    # Ex.: post/5
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]