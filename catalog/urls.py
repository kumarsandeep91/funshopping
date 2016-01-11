from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, name='catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, name='catalog_product'),
]