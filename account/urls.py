from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import register

urlpatterns = [
	path('register/', register, name='register'),
   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

    #   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # from rest_framework_simplejwt.views import TokenVerifyView
