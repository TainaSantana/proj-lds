from django.urls import path
from . import views

urlpatterns = [
    path('', views.meetList, name='meet-list'),
    path('pauta/<int:id>', views.meetPauta, name='meet-pauta'),
    path('sobre/', views.meetAbout, name='meet-about'),
    path('newmeet/', views.newMeet, name='new-meet'),
    path('editmeet/<int:id>', views.editMeet, name='edit-meet'),
    path('deletemeet/<int:id>', views.deleteMeet, name='delete-meet'),
    path('email/', views.sendEmail, name='send-email'),
]