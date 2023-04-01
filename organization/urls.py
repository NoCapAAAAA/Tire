from django.http import HttpResponse
from django.urls import path, include

from organization import views as v


urlpatterns = [
    path('director/', v.DirectorHomeView.as_view(), name='directorHome'),
    path('director/users', v.DirectorUsersView.as_view(), name='directorUsers'),
    path('director/clients', v.DirectorClientsView.as_view(), name='directorClients'),
    path('director/stuff', v.DirectorStuffView.as_view(), name='directorStuff'),
    path('director/orders', v.DirectorOrdersView.as_view(), name='directorOrders'),
    path('director/statistics', v.DirectorStatisticsView.as_view(), name='directorStatistics'),


    path('manager/', v.ManagerHomeView.as_view(), name='managerHome'),


]
