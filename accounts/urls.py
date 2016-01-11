from django.conf.urls import *
from ecofstore import settings

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^my_account/$', views.my_account, name='my_account'),
#    url(r'^order_details/(?P<order_id>[-\w]+)/$', views.order_details, name='order_details'),
#    url(r'^order_info//$', views.order_info, name='order_info'),
]
urlpatterns += [
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
]
