from django.urls import path
from demo_app.views import ViewProduct


urlpatterns = [
    path('', ViewProduct.as_view()),
]
