from django.urls import path
from .views import ContactForm

urlpatterns = [
    path('contact_us/', ContactForm.as_view(), name='contact_us'),
    path('contact_us/<int:pk>/', ContactForm.as_view()),
]