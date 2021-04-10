from django.urls import path
from rest_framework import routers

from bot.views import BotAPIView

urlpatterns = [
    path('', BotAPIView.as_view())
]