from django.http import HttpResponse
from django.urls import path, include

from organization import views as v


urlpatterns = [
    path('director/', v.Test.as_view(), name='directorhome'),
    path('manager/', v.Test2.as_view(), name='managerhome'),

]
