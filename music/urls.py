from django.conf.urls import url

from . import views

app_name = 'music'

urlpatterns = [
	url(r'^$',views.index,name='index'),

	#/music/id
	url(r'^(?P<album_id>[0-9]+)$',views.detail,name='detail'),

	#/music/favorite
	url(r'^(?P<album_id>[0-9]+)/favorite$',views.detail,name='favorite'),
]