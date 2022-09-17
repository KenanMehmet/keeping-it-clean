from django.urls import path

from .views import MainSiteIndex, MainSiteClientSignup

urlpatterns = [
    path('', MainSiteIndex.as_view(), name="index"),
    path('client-signup', MainSiteClientSignup.as_view(), name="client-signup"),
]