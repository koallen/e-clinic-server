from django.conf.urls import url
from .views import ProgressList

urlpatterns = [
    url(r'^progresses/$', ProgressList.as_view())
]
