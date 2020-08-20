from django.urls import path
from . import views

app_name = 'ata'

urlpatterns = [
    path('', views.ataslist, name='ata-list'),
    #path('atatnew/', views.ataNew, name='ata-new'),
    #path('ataedit/<int:id>', views.ataEdit, name='ata-edit'),
    #path('atadelete/<int:id>', views.ataDelete, name='ata-delete'),
]