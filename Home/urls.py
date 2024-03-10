from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.home,name='home'),
    # path('two/',views.login),
    path('zero/',views.registration1),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('post-complaint',views.complaint,name='post-complaint'),
    path('view-all-complaints/', views.view_all_complaints, name='view_all_complaints'),
    path('view-assigned-complaints/', views.driver_complaints, name='view_assigned_complaints'),
]