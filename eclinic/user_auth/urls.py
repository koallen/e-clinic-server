from django.conf.urls import url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^auth-tokens/$', views.obtain_auth_token)
]
