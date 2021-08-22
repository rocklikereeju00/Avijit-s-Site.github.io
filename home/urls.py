from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Log In Here"
admin.site.site_title = "Saraswati Admin Portal"
admin.site.index_title = "Welcome to Saraswati Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page, name='page'),
    path('Home', views.index, name='index'),
    path('eCommerce', views.eCommerce, name='eCommerce'),
    path('about', views.about, name='about'),
    path('Personal', views.Personal, name='Personal'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('removing', views.removing, name='removing'),
    path('capitalize', views.capitalize, name='capitalize'),
    path('line_remover', views.line_remover, name='line_remover'),
    path('spa', views.spa, name='spa'),
]