from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.hom,name='home'),
    # path('two/',views.login),
    path('zero/',views.registration1),
    path('four/',views.about,name='about'),
    path('five/',views.contact,name='contact'),
    path('six/',views.base),
    path('seven/',views.service,name='service'),
    # path('nine/',views.home2,name='nine'),

    path('eleven',views.Views_bin,name='eleven'),
    path('twelve',views.complaint,name='twelve'),
    # path('thirteen',views.searchbar,name='thirteen'),
    # path('fourteen',views.searchresult,name='fourteen')
    path('view-all-complaints/', views.view_all_complaints, name='view_all_complaints'),
    path('view-assigned-complaints/', views.driver_complaints, name='view_assigned_complaints'),
]