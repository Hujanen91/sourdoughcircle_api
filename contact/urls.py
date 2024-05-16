from django.urls import path
from contact import views

urlpatterns = [
    path('contact_us/', views.ContactList.as_view()),
    path('contact_us/<int:pk>/', views.ContactDetail.as_view()),
]