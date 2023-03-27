from django.http import HttpResponse
from django.urls import path, include

from authentication import views as v


urlpatterns = [
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.logout_view, name='logout'),
    path('register/', v.RegisterView.as_view(), name='register'),
    path('edit/', v.UserEditView.as_view(), name='user_edit'),
    path('detail/', v.UserDetailView.as_view(), name='user_detail'),
    path('password/', v.PasswordChangeView.as_view(), name='password_edit'),

]