from django.urls import path

from profiles import views as v


urlpatterns = [
    path('', v.profile, name='user_profile'),
    path('<int:pk>/', v.ProfileView.as_view())
]