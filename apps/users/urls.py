from django.urls import path, include
from .views import SignupView, LoginView, CurrentUserView, UserDetailView
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('<int:id>/', UserDetailView.as_view(), name='user-detail'),
]
