from myauth import views
from django.urls import path,include
from myauth.views import Category_viewset,Product_viewset

from rest_framework.routers import DefaultRouter
router=DefaultRouter()

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router.register('category',views.Category_viewset,basename='category')
router.register('Product',views.Product_viewset,basename='Product')


urlpatterns = [
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]