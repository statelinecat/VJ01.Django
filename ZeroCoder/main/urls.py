from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index),
#     path('new', views.new),
#     path('data', views.data),
#     path('test', views.test),
#     path('data/', views.data_view, name='data'),
#     path('test/', views.test_view, name='test'),
# ]
urlpatterns = [
    path('', views.index, name=''),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]

