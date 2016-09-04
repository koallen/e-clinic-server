from django.conf.urls import url
from .views import ProgressList

urlpattern = [
    url(r'^progresses/$', ProgressList.as_view())
]
