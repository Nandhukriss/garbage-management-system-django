from django.urls import path
from . import views

from .import views
from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
#  from django.contrib.auth import views as auth_views
urlpatterns =[
    path('registration1',views.signup,name='registration1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('change_password',views.change_password,name='change_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),


 ]

