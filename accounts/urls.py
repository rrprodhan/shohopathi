from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

#auth_views class has default functions for showing log-in and log-out page
#here we edited the log-in view to show our customized log-in page 

urlpatterns = [
    re_path(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    re_path(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    re_path(r'signup/$',views.SignUp.as_view(),name='signup')
]
