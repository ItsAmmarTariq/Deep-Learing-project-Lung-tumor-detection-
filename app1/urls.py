from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('data_processing',views.data_processing,name='data_processing'),
    path('chat/', views.render_chat, name='render_chat'),
    path('chat/process/', views.process_chat, name='process_chat'),

]
