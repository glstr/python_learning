# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.snower, name="snower"),
        url(r'^imagekitchen/$', views.imagekitchen, name="imagekitchen"),
        url(r'^imagekitchen/data/$', views.imagedata, name="imagedata"),
        url(r'^imagekitchen/allimage/$', views.allimages, name="allimages"),
        url(
            r'^imagekitchen/(?P<img_id>[0-9]+)/image$', views.image_detail, 
            name='imagedetail'),
]
