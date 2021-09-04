from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), 
    path('rates/', views.rates, name='rates'),
    path('meet-our-staff/', views.meet, name='meet'),
   
   
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('service/', views.service, name='service'), 

    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register_view),


]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
