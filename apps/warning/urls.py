# -*- coding: utf-8 -*-
# @Time    :2019/8/21 15:57
from django.conf.urls import url, include
from django.urls import re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()  # 默认附带一个api根视图，相对于SimpleRouter（）
router.register(r'zjzxbxkmx', views.ZjzxbxkmxView),
router.register(r'spinner', views.SpinnerView, base_name='spinner'),

urlpatterns = [
    re_path(r'^(?P<version>[v1|v2]+)/zjzxbxk/$', views.ZjzxbxkView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xxtxblx/$', views.XxtxblxView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xwzs/$', views.XwzsView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/bzx/$', views.BzxView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/tkxw/$', views.TkxwView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/wg/$', views.WgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/swxw/$', views.SwxwView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xwgj/$', views.XwgjView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/zjzxbxkmx/$', views.ZjzxbxkmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/xxtxblxmx/$', views.XxtxblxmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/xwzsmx/$', views.XwzsmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/bzxmx/$', views.BzxmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/tkxwmx/$', views.TkxwmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/swxwmx/$', views.SwxwmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/wgmx/$', views.WgmxView.as_view({'get': 'retrieve'})),
    re_path(r'^(?P<version>[v1|v2]+)/xwgjmx/$', views.XwgjmxView.as_view({'get': 'retrieve'})),

    re_path(r'^(?P<version>[v1|v2]+)/zjzxbxkxg/$', views.ZjzxbxkxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/tkxwxg/$', views.TkxwxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/wgxg/$', views.WgxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xxtxblxxg/$', views.XxtxblxxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/xwzsxg/$', views.XwzsxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/bzxxg/$', views.BzxxgView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/yjyzsz/$', views.YjyzszView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/yjyzlssz/$', views.YjyzlsszView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/yjyzlssz2/$', views.YjyzlsszView2.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/warningtable/$', views.WaringTableView.as_view()),

    re_path(r'^(?P<version>[v1|v2]+)/college/$', views.CollegeView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/college/(?P<pk>\d+)/$', views.CollegeView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/grade/$', views.GradeView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/class/$', views.ClassView.as_view()),

    # re_path(r'^(?P<version>[v1|v2]+)/yx/$', views.YxView.as_view()),
    # re_path(r'^(?P<version>[v1|v2]+)/nj/$', views.NjView.as_view()),
    # re_path(r'^(?P<version>[v1|v2]+)/bj/$', views.BjView.as_view()),



    url(r'^', include(router.urls)),

]
urlpatterns += router.urls
