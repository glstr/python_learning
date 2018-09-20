# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from fury import redisc
from imagec import image_manager

# Create your views here.


def snower(request):
    return render(request, 'snower/snower.html') 
 

def imagekitchen(request):
    return render(request, 'snower/imagekitchen.html')


def imagedata(request):
    metainfo = redisc.image_info()
    return render(request, 'snower/imagedata.html', {"imageinfo": metainfo})


def allimages(request):
    im = image_manager.ImageManager("snow")
    im.load()
    all_images = im.get_allimages_path()
    params = {"title": "all images"}
    new_images = []
    for ele in all_images:
        str_img = ele.split('/')
        id_str = str_img[-1].rstrip('.png')
        new_images.append(id_str)
    params["allimages"] = new_images
    return render(request, 'snower/list.html', params)


def image_detail(request, img_id):
    img_id = int(img_id)
    img_last = img_id - 1
    if img_last < 1:
        img_last = 1
    img_next = img_id + 1
    img_path = '/image/' + str(img_id) + '.png'
    content = {
            "title": "image detail", "img_path": img_path,
            "img_next": img_next, "img_last": img_last}
    return render(request, 'snower/detail.html', content)

