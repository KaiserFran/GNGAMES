from django.urls import path
from . import views
from .views import nosotros
urlpatterns = [
    path('', views.home, name='home'), # PAGINA HOME
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('nosotros/', nosotros, name='nosotros'),
]
