from django.urls import path
from user_profile import views

urlpatterns = [
    path('view/<int:id>', views.user_profile)
]