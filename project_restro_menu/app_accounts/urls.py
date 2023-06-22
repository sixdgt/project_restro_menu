from django.urls import path
from app_accounts.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),    
    path('logout/', LogoutView.as_view(), name='logout'),    
    path('register/', RegisterView.as_view(), name='register'),    
]