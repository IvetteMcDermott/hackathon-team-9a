from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addNGO', views.AddNGOForm.as_view(), name='add_ngo'),
]