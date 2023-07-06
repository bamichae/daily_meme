from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='images-index'),
    path('upload/', views.upload_view, name='images-upload'),
    path('test/', views.test_view, name='test-upload'),
]