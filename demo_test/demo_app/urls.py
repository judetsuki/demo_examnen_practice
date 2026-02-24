from django.urls import path
from demo_app.views import ViewProduct, UserLoginView, UserLogoutView


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('products/', ViewProduct.as_view(), name='product_list'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
