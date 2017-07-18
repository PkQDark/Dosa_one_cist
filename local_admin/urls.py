from django.conf.urls import url
from .views import cistern_add, cistern_edit, cistern_info, \
    keys, edit_key, \
    users, add_local_user, edit_local_user, \
    hide_admin

urlpatterns = [
    url(r'^$', cistern_info, name='cist_info'),
    url(r'^cisterns/add/$', cistern_add, name='cistern_add'),
    url(r'^cisterns/edit/(?P<cist_id>\d+)/', cistern_edit, name='cist_edit'),
    url(r'^keys/$', keys, name='keys'),
    url(r'^keys/edit/(?P<key_id>\d+)/', edit_key, name='edit_key'),
    url(r'^users/$', users, name='users'),
    url(r'^users/add-user/$', add_local_user, name='add_user'),
    url(r'^users/edit/(?P<user_id>\d+)/', edit_local_user, name='edit_user'),
    url(r'^hide-admin/$', hide_admin, name='hide_admin'),
]