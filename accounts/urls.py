from django.urls import path
from .views import home, signup, dashboard, NewLoginView

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', NewLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]