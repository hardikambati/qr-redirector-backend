from django.urls import path

from . import views


urlpatterns = [
    path('redirect/', views.RedirectWebhookAPIView.as_view()),
]