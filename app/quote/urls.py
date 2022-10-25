"""
URL mappings for the quote app.
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from quote import views


router = DefaultRouter()
router.register('quotes', views.QuoteViewSet)

app_name = 'quote'

urlpatterns = [
    path('', include(router.urls)),
]
