from django.conf.urls import url
from .views import MessageTokenList, MessageTokenDetail, MessageList

urlpatterns = [
	url(r'^tokens/$', MessageTokenList.as_view()),
	url(r'^token/(?P<id>[0-9]+)/$', MessageTokenDetail.as_view()),
    url(r'^messages/$', MessageList.as_view())
]
