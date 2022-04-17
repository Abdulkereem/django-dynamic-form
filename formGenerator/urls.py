from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/<formkey>', views.form, name='index'),
    path('submit/<formkey>', views.submit, name='submit'),
    path('AddNewForm', views.AddNewForm, name='AddNewForm'),
]