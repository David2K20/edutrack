from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('students', views.index, name = 'index'),
    path('<int:id>', views.view_student, name = 'view_student'),
    path('add/', views.add, name = 'add'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]