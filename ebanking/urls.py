from django.contrib import admin
from django.urls import path
from core.views import UserView
from ebanking.application import ApplicationBase

# Django URL
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Tornado URL
URL_PATTERNS = ApplicationBase([
    ('/users', UserView),
])