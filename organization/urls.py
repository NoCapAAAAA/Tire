from django.http import HttpResponse
from django.urls import path, include

from organization import views as v
from . import views

urlpatterns = [
    path('director/', v.DirectorHomeView.as_view(), name='directorHome'),
    path('director/users', v.DirectorUsersView.as_view(), name='directorUsers'),
    path('director/clients', v.DirectorClientsView.as_view(), name='directorClients'),
    path('director/stuff', v.DirectorStuffView.as_view(), name='directorStuff'),
    path('director/orders/', v.DirectorOrdersView.as_view(), name='directorOrders'),
    path('director/orders/<int:pk>/', v.DetailOrderViewDir.as_view(), name='directorOrdersDetail'),
    path('director/statistics', v.DirectorStatisticsView.as_view(), name='directorStatistics'),
    path('docs/', views.TestDocument, name='report_download'),

    path('manager/', v.ManagerHomeView.as_view(), name='managerHome'),
    path('manager/setting/', v.ManagerEdit.as_view(), name='manager_edit'),
    path('manager/pass/', v.PassChange.as_view(), name='pass_change'),


]
