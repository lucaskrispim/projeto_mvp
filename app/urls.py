from django.urls import path
from .views import *

urlpatterns = [
    path('', index.index_view, name = 'index'),
    path('api/test', Index.as_view()),
]