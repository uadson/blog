from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # Ex.: /
    path('', views.post_list, name='post_list'),
    # Ex.: post/5
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    # Ex.: post/new/
    path('post/new/', views.post_new, name='post_new'),
    # Ex.: post/5/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # Ex.: post/drafts/
    path('post/drafts/', views.post_draft_list, name='post_draft_list'),
]