from django.urls import path
from.views import CategoryList

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
]