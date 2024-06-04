from django.urls import path
from.views import CategoryList, CategoryDetail

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view())
]