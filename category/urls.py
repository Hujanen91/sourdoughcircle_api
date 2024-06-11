from django.urls import path, include
from rest_framework.routers import DefaultRouter

from.views import CategoryList, CategoryDetail

router = DefaultRouter()

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('api/', include(router.urls)),
]