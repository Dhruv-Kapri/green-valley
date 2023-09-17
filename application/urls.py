from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.homepage),
    path('home/post_event/', views.postEvent),
    path('home/browse_event/', views.browseEvents),
    path('home/browse_event/<id>', views.register),
    path('home/browse_event/registration_done/<id>', views.regDone),
    path('home/post_event/hosting_done/', views.hostDone)
    
]