from django.urls import path

from .views import MainSiteIndex

urlpatterns = [
    path('', MainSiteIndex.as_view(), name="index"),
]