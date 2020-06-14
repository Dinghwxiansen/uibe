# -*- coding: utf-8 -*-
# @Time    :2019/8/2 11:29

from django.urls import re_path

from . import views

#
# router = routers.DefaultRouter()  # 默认附带一个api根视图，相对于SimpleRouter（）
# router.register(r'jqsz', views.JqszView),

urlpatterns = [

    re_path(r'^(?P<version>[v1|v2]+)/jqsz/$', views.JqszView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/jqsz/(?P<pk>\d+)/$', views.JqszView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/bqwd/$', views.BqwdView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/bqwd/(?P<pk>\d+)/$', views.BqwdView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/hxbqsz/$', views.HxbqszView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/hxbqszfz/$', views.HxbqszfzView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/hxbqsz/(?P<pk>\d+)/$', views.HxbqszView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/hxbqszzbx/$', views.HxbqszZbxView.as_view()),



    re_path(r'^(?P<version>[v1|v2]+)/tzjm/$', views.ZbxView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/tzjm/(?P<pk>\d+)/$', views.ZbxView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/sjbxz/$', views.SjbxzView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/sjbxzzd/$', views.SjbxzzdView.as_view({'get': 'retrieve'})),

    re_path(r'^(?P<version>[v1|v2]+)/jshx/$', views.JshxView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/jshxxq/$', views.JshxxqView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/jshxzcxq/$', views.JshxzcxqView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/xshxjsd/$', views.XshxJsdVIew.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xshxxsd/$', views.XshxXsdVIew.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xshxjstxq/$', views.XshxJsdXqVIew.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/bm/$', views.BmVIew.as_view()),


    re_path(r'^(?P<version>[v1|v2]+)/yjsyx/$', views.YjsYxVIew.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/yjsnj/$', views.YjsNjVIew.as_view()),


    re_path(r'^(?P<version>[v1|v2]+)/yjsxwgj/$', views.YjsXwgjView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/yjsxwgjxq/$', views.YjsXwgjXqView.as_view()),



]
