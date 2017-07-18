from django.conf.urls import url
from .views import cistern_info, keys

urlpatterns = [
    url(r'^$', cistern_info, name='cist_info'),
    url(r'^keys/$', keys, name='keys'),
]
