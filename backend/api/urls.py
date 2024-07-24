from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/verify', TokenVerifyView.as_view(), name='token-verify'),
    path('roken/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]