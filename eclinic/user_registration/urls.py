from django.conf.urls import url

from .views import UserList

urlpatterns = [
    url(r'^users/$', UserList.as_view())
]
