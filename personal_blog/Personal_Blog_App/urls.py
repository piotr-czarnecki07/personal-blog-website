from django.urls import path
from Personal_Blog_App import views

urlpatterns = [
    path('', views.main, name='main'),
    path('article/<int:articleid>/', views.article, name='article'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminpage/post/', views.post, name='post'),
    path('adminpage/<int:articleid>/', views.adminarticle, name='adminarticle'),
    path('adminpage/<int:articleid>/edit/', views.edit, name='edit'),
    path('adminpage/<int:articleid>/delete/', views.delete, name='delete'),
    path('adminpage/<int:articleid>/deletecomment/<int:commentid>/', views.deletecomment, name='deletecomment'),
]