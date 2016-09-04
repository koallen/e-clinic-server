from django.conf.urls import url
from .views import ReservationList


urlpattern = [
    url(r'^reservations/$', ReservationList.as_view())
]