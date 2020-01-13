# Create your views here.

import json
# todo import datetime直接导入 报错 nomodule min
from datetime import *

from dateutil.relativedelta import relativedelta
from django.db.models import Count, Q, Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.base import filter
from apps.portrait import models as pm
from apps.utils import restful
from apps.utils import serialiser
from apps.utils.pagination import Pagination
from apps.warning import models as wm


class ZjzxbxkView(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,

                  generics.GenericAPIView, ):
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):

        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(zjzxbxk__create_time__gt=kssj) & Q(zjzxbxk__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("zjzxbxk", filter=myfilter)).filter(
                yjcs__gte=1).order_by("-update_time")
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(zjzxbxk__xh=xhxm).annotate(
                    yjcs=Count("zjzxbxk", filter=myfilter)).filter(
                    yjcs__gte=1).order_by("-update_time")
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("zjzxbxk", filter=myfilter)).filter(
                    yjcs__gte=1).order_by("-update_time")
        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    filter_class = filter.BzksFilter

    def post(self, request, *args, **kwargs):
        try:

            ret = self.list(request, *args, **kwargs)

            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}

            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""智能预警之在籍在校不选课预警明细"""


class ZjzxbxkmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # 分页
    pagination_class = Pagination
    queryset = wm.ZnyjZjzxbxk.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.ZjzxbxkmxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.ZjzxbxkmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # 更新状态
    # def patch(self, request, *args, **kwargs):
    #     ids = request.data['id'].split(',')
    #     print(ids)
    #     try:
    #         for i in ids:
    #             ret = wm.ZnyjZjzxbxk.objects.filter(id=i).first()
    #             ser = serialiser.ZjzxbxkmxSerialiser(instance=ret, data=request.data, partial=True)
    #             if ser.is_valid():
    #                 ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)
    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjZjzxbxk.objects.filter(id=i).values('clzt'))[0]['clzt']
                    print(zt)
                    it = int(request.data['clzt'])

                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjZjzxbxk.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # ser = serialiser.ZjzxbxkmxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()

                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")

        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""*****************************智能预警之休学退学不离校预警*********************************"""


class XxtxblxView(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        # todo kssj = self.request.query_params.get("kssj", datetime.date.min)
        # todo jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(xxtxblx__create_time__gt=kssj) & Q(xxtxblx__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("xxtxblx", filter=myfilter)).filter(
                yjcs__gte=1).order_by("-update_time")
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(xxtxblx__xh=xhxm).annotate(
                    yjcs=Count("xxtxblx", filter=myfilter)).filter(
                    yjcs__gte=1).order_by("-update_time")
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("xxtxblx", filter=myfilter)).filter(
                    yjcs__gte=1).order_by("-update_time")

        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.BzksFilter

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            # <class 'rest_framework.response.Response'>
            # <class 'collections.OrderedDict'>
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""智能预警之休学退学不离校预警明细"""


class XxtxblxmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjXxtxblx.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XxtxblxMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.XxtxblxmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
    # def patch(self, request, *args, **kwargs):
    #     #     ids = request.data['id'].split(',')
    #     #     # print(ids)
    #     #     try:
    #     #         for i in ids:
    #     #             ret = wm.ZnyjXxtxblx.objects.filter(id=i).first()
    #     #             ser = serialiser.XxtxblxMxSerialiser(instance=ret, data=request.data, partial=True)
    #     #             if ser.is_valid():
    #     #                 ser.save()
    #     #         return restful.ok()
    #     #     except Exception as e:
    #     #         return restful.result(message=e.detail)"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjXxtxblx.objects.filter(id=i).values('clzt'))[0]['clzt']
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjXxtxblx.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # ser = serialiser.XxtxblxMxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()
                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""*****************************智能预警之校外住宿预警*******************************"""


class XwzsView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))
        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(xwzs__create_time__gt=kssj) & Q(xwzs__create_time__lt=jssj)
        sfxx = self.request.query_params.get('sfxx', None)
        sftx = self.request.query_params.get('sftx', None)
        syd = self.request.query_params.get('syd', None)
        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("xwzs", filter=myfilter)).filter(
                Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(syd=syd), ~Q(xjzt=sftx))
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(xwzs__xh=xhxm).annotate(
                    yjcs=Count("xwzs", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(syd=syd),
                                                                ~Q(xjzt=sftx))
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("xwzs", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(syd=syd),
                                                                ~Q(xjzt=sftx))

        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""*************校外住宿预警明细************"""


class XwzsmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjXwzsyj.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XwzsMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.XwzsmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def patch(self, request, *args, **kwargs):
    #     ids = request.data['id'].split(',')
    #     # print(ids)
    #     try:
    #         for i in ids:
    #             ret = wm.ZnyjXwzsyj.objects.filter(id=i).first()
    #             ser = serialiser.XwzsMxSerialiser(instance=ret, data=request.data, partial=True)
    #             if ser.is_valid():
    #                 ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)
    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjXwzsyj.objects.filter(id=i).values('clzt'))[0]['clzt']
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjXwzsyj.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # ser = serialiser.XwzsMxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()
                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""******************************智能预警之不在校预警***********************************"""


class BzxView(mixins.ListModelMixin, mixins.CreateModelMixin,
              mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
              generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(bzx__create_time__gt=kssj) & Q(bzx__create_time__lt=jssj)
        sfxx = self.request.query_params.get('sfxx', None)
        sftx = self.request.query_params.get('sftx', None)

        syd = self.request.query_params.get('syd', None)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("bzx", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx)
                                                                                          , ~Q(syd=syd), ~Q(xjzt=sftx))
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(bzx__xh=xhxm).annotate(
                    yjcs=Count("bzx", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(syd=syd),
                                                               ~Q(xjzt=sftx))
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("bzx", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(syd=syd),
                                                               ~Q(xjzt=sftx))

        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', '=syd', '=xjzt', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


'''不在校预警明细'''


class BzxmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjBzx.objects.all()
    # 序列化
    serializer_class = serialiser.BzxMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.BzxmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def patch(self, request, *args, **kwargs):
    #     ids = request.data['id'].split(',')
    #     try:
    #         for i in ids:
    #             ret = wm.ZnyjBzx.objects.filter(id=i).first()
    #             ser = serialiser.BzxMxSerialiser(instance=ret, data=request.data, partial=True)
    #             if ser.is_valid():
    #                 ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)
    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjBzx.objects.filter(id=i).values('clzt'))[0]['clzt']
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjBzx.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # print(ret)
                        # ser = serialiser.BzxMxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()
                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""*****************************智能预警之逃课行为预警*****************************"""


class TkxwView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(tkxw__create_time__gt=kssj) & Q(tkxw__create_time__lt=jssj)
        sfxx = self.request.query_params.get('sfxx', None)
        sftx = self.request.query_params.get('sftx', None)
        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("tkxw", filter=myfilter)).filter(
                Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(xjzt=sftx))
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(tkxw__xh=xhxm).annotate(
                    yjcs=Count("tkxw", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(xjzt=sftx))
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("tkxw", filter=myfilter)).filter(Q(yjcs__gte=1) & ~Q(xjzt=sfxx), ~Q(xjzt=sftx))
        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


'''逃课行为预警明细'''


class TkxwmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjTkxw.objects.all()
    # 序列化
    serializer_class = serialiser.TkxwMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.TkxwmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def patch(self, request, *args, **kwargs):
    #     #     ids = request.data['id'].split(',')
    #     #     # print(ids)
    #     #     try:
    #     #         for i in ids:
    #     #             ret = wm.ZnyjTkxw.objects.filter(id=i).first()
    #     #             ser = serialiser.TkxwMxSerialiser(instance=ret, data=request.data, partial=True)
    #     #             if ser.is_valid():
    #     #                 ser.save()
    #     #         return restful.ok()
    #     #     except Exception as e:
    #     #         return restful.result(message=e.detail)
    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjTkxw.objects.filter(id=i).values('clzt'))[0]['clzt']
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjTkxw.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # print(ret)
                        # ser = serialiser.TkxwMxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()
                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""***********************************智能预警之晚归预警************************************"""


class WgView(mixins.ListModelMixin, mixins.CreateModelMixin,
             mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
             generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(wg__create_time__gt=kssj) & Q(wg__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("wg", filter=myfilter)).filter(
                yjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(wg__xh=xhxm).annotate(
                    yjcs=Count("wg", filter=myfilter)).filter(
                    yjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("wg", filter=myfilter)).filter(
                    yjcs__gte=1)
        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}

            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


'''晚归预警明细'''


class WgmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjWgyj.objects.all()
    # 序列化
    serializer_class = serialiser.WgMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.WgmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def patch(self, request, *args, **kwargs):
    #     ids = request.data['id'].split(',')
    #     # print(ids)
    #     try:
    #         for i in ids:
    #             ret = wm.ZnyjWgyj.objects.filter(id=i).first()
    #             ser = serialiser.WgMxSerialiser(instance=ret, data=request.data, partial=True)
    #             if ser.is_valid():
    #                 ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)
    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.ZnyjWgyj.objects.filter(id=i).values('clzt'))[0]['clzt']
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjWgyj.objects.filter(id=i).first()
                        ret.clzt = int(request.data['clzt'])
                        ret.update_time = datetime.now()
                        ret.save()
                        # ser = serialiser.WgMxSerialiser(instance=ret, data=request.data, partial=True)
                        # if ser.is_valid():
                        #     ser.save()
                if int(request.data['clzt']) == 1:
                    return restful.result(message="操作成功，已确认预警")
                elif int(request.data['clzt']) == 2:
                    return restful.result(message="操作成功，已取消预警")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""*****************************智能预警之上网行为预警*****************************"""


class SwxwView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))
        xhxm = self.request.query_params.get('xhxm', None)
        syll = self.request.query_params.get('syll', "0~2**20")
        # print(syll.split("~"))
        llrange = syll.split("~")
        # 流量上限和下限
        llmin = eval(llrange[0])
        llmax = eval(llrange[1])

        myfilter = Q(swxw__create_time__gt=kssj) & Q(swxw__create_time__lte=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(zsyll=Sum("swxw__syll", filter=myfilter)).filter(
                zsyll__gte=1).filter(zsyll__range=(llmin, llmax))
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(swxw__xh=xhxm).annotate(
                    zsyll=Sum("swxw__syll", filter=myfilter)).filter(
                    zsyll__gte=1).filter(zsyll__range=(llmin, llmax))
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    zsyll=Count("swxw__syll", filter=myfilter)).filter(
                    zsyll__gte=1).filter(zsyll__range=(llmin, llmax))
        return ret

    # 序列化
    serializer_class = serialiser.BzksSwxwSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""智能预警之上网行为预警明细"""


class SwxwmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.ZnyjSwxw.objects.all().order_by('-update_time')
    # 序列化
    serializer_class = serialiser.SwxwMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.SwxwmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""******************************行为轨迹分析-**************************"""


class XwgjView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))
        xhxm = self.request.query_params.get('xhxm', None)
        print(xhxm)

        myfilter = Q(grgj__create_time__gt=kssj) & Q(grgj__create_time__lte=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                gjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(grgj__xh__icontains=xhxm).annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm__icontains=xhxm).annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
        return ret

    # 序列化
    serializer_class = serialiser.BzksXwgjSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""******************************行为轨迹个人分析-**************************"""


class XwgjmxView(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination
    queryset = wm.XwgjGrgj.objects.all().order_by('-update_time')
    # 序列化
    serializer_class = serialiser.XwgjMxSerialiser
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = filter.XwgjmxFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


# class XwgjView(mixins.ListModelMixin, mixins.CreateModelMixin,
#                mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#                generics.GenericAPIView, ):
#     # authentication_classes = []
#     # permission_classes = []
#     """分页"""
#     pagination_class = Pagination
#
#     queryset = pm.UibeBzks.objects.all()
#     # 序列化
#     serializer_class = serialiser.BzksSerialiser
#     filter_class = filter.BzksFilter
#     # 搜索，前端通过search关键字传值，？search=''
#     search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则
#
#     def post(self, request, *args, **kwargs):
#         ret = self.list(request, *args, **kwargs)
#         return restful.result(message="操作成功", data=ret.data)


"""下拉列表


# todo 院系
class YxView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = []
    queryset = wm.Yx.objects.all()
    # 序列化
    serializer_class = serialiser.YxSerialiser
    filter_class = filter.YxFilter

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


# todo 年级
class NjView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = []
    queryset = wm.Nj.objects.all()
    # 序列化
    serializer_class = serialiser.NjSerialiser
    filter_class = filter.NjFilter

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


# todo 班级
class BjView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = []
    queryset = wm.Bj.objects.all()
    # 序列化
    serializer_class = serialiser.BjSerialiser
    filter_class = filter.BjFilter

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

"""

"""预警下拉列表中院系数据"""


class CollegeView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = pm.UibeBzks.objects.filter(xjzt='01', xznj__isnull=False).values('yx').distinct()

    serializer_class = serialiser.CollegeSerialiser

    # filter_class = filter.BjFilter

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # 去重
            # retsult = [dict(t) for t in set([tuple(d.items()) for d in ret.data])]

            # print(connection.query)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""下拉列表中年级数据"""


class GradeView(mixins.ListModelMixin, generics.GenericAPIView):
    # def get_queryset(self):
    #     yx = self.request.query_params.get('yxdm')
    #     if yx:
    #         ret = pm.UibeBzks.objects.filter(xjzt='01',xznj__isnull=False).values('xznj').distinct()
    #         return ret
    #     else:
    #         ret = pm.UibeBzks.objects.filter(yxdm=yx, xznj__isnull=False).values('xznj').distinct()
    #         return ret
    queryset = pm.UibeBzks.objects.filter(xjzt='01', xznj__isnull=False).values('xznj').distinct()
    serializer_class = serialiser.GradeSerialiser

    filter_class = filter.GradeFilter

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""下拉列表班号数据"""


class ClassView(generics.ListAPIView, generics.GenericAPIView):
    queryset = pm.UibeBzks.objects.filter(xjzt='01', bj__isnull=False).values('bj').distinct()
    serializer_class = serialiser.ClassSerialiser
    filter_class = filter.ClassFilter

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class SpinnerView(ReadOnlyModelViewSet):
    # authentication_classes = []
    # permission_classes = []

    def get_queryset(self):
        ret = {'code': 200, 'msg': '操作成功！'}
        if self.action == 'list':
            # pid = None 的时候，返回的是院级数据
            yj = wm.Spinner.objects.filter(pid=None)
            # re =[]
            # re.append(yj)
            # # for i in yj:
            # #     re.append(i)
            # ret['data'] = re
            # print(ret)
            return yj

            # return restful.result(message="操作成功", data=models.Spinner.objects.filter(pid=None))
        else:
            bj = wm.Spinner.objects.all()
            return bj
            # return restful.result(message="操作成功", data=models.Spinner.objects.all())

    def get_serializer_class(self):
        if self.action == 'list':
            return serialiser.SpinnerInfoSerializer
        else:
            return serialiser.NextSpinnerInfoSerializer


"""预警阈值置之在籍在校不选课预警修改"""


class ZjzxbxkxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XtglYjyzszZjzxbxkSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def post(self, request, *args, **kwargs):
    #     # print(request.data)
    #     try:
    #         it = request.data['yjgz']
    #         try:
    #             mc = list( wm.XtglYjyzsz.objects.filter(yjgz=it).values('yjgz'))[0]["yjgz"]
    #             return restful.result2(message="请勿重复保存操作")
    #         except IndexError:
    #             ret = self.create(request, *args, **kwargs)
    #             return restful.result(message="保存成功")
    #     except Exception as e:
    #         return restful.result(message=e.detail)
    #
    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.XtglYjyzszZjzxbxkSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)
    #
    # """更新"""
    #
    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.XtglYjyzszZjzxbxkSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


"""预警阈值之逃课预警修改"""


class TkxwxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.TkxwxgSerializer

    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.TkxwxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.TkxwxgSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result(message=e.detail)"""


"""预警阈值之晚归预警修改"""


class WgxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.WgxgSerializer

    """
    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.WgxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)"""

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.WgxgSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result(message=e.detail)"""


"""预警阈值之休学退学不离校预警修改"""


class XxtxblxxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XxtxblxxgSerializer
    """
    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.XxtxblxxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)"""

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.XxtxblxxgSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result(message=e.detail)"""


"""预警阈值之休学校外住宿预警修改"""


class XwzsxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XwzsxgSerializer

    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.XwzsxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:

            # self.partial_update(request, *args, **kwargs)
            ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.XwzsxgSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result(message=e.detail)"""


"""预警阈值之不在校预警修改"""


class BzxxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.BzxSerializer

    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.BzxSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)

    """更新"""

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.BzxSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


"""预警阈值设置"""


class YjyzszView(mixins.ListModelMixin, generics.GenericAPIView):
    # authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    # queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    def get_queryset(self):
        all_queryset = wm.XtglYjyzsz.objects.none()
        res = ['bzxxg', 'xwzsxg', "xxtxblx", "tkyjxg", "wgyjxg", "zjzxbxk"]
        querysetall = []
        for i in res:
            query = wm.XtglYjyzsz.objects.filter(
                id=wm.XtglYjyzsz.objects.filter(code=i).order_by("-update_time")[:1].values('id')[0]['id'])
            querysetall.append(query)
        for i in querysetall:
            all_queryset = all_queryset | i
        return all_queryset

    # 序列化
    serializer_class = serialiser.YjyzszSerializer
    # 过滤器
    filter_class = filter.YjyzsjFilter

    def get(self, request, *args, **kwargs):
        try:
            ret1 = self.list(request, *args, **kwargs)

            # bzx = wm.XtglYjyzsz.objects.filter(code='bzxxg').order_by("-update_time")[0:1]
            # data = serializ.serialize("json", bzx)
            # loads = json.loads(data)
            # # return JsonResponse(loads, safe=False)
            # # print(connection.queries[-1:])
            # todo 加载函数，放在标签建模设置中指定运行，
            return restful.result(message="操作成功", data=ret1.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新状态"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(wm.XtglYjyzsz.objects.filter(id=i).values('kqzt'))[0]['kqzt']
                    it = int(request.data['kqzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.XtglYjyzsz.objects.filter(id=i).first()
                        ser = serialiser.YjyzszSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""预警阈值历史设置查询"""


class YjyzlsszView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = []

    def get_queryset(self):
        all_queryset = wm.XtglYjyzsz.objects.none()

        querysetall = []
        query = wm.XtglYjyzsz.objects.filter(code=self.request.query_params.get("code"))

        querysetall.append(query)
        for i in querysetall:
            all_queryset = all_queryset | i
        return all_queryset
        # 序列化

    def get_serializer_class(self):
        code = self.request.query_params.get("code")
        if code == "zjzxbxk":
            return serialiser.ZjzxbxkYjyzlsszSerializer
        elif code == "wgyjxg":
            return serialiser.YjyzlsszSerializer2
        elif code == "tkyjxg":
            return serialiser.ZjzxbxkYjyzlsszSerializer
        elif code == "xxtxblx":
            return serialiser.YjyzlsszSerializer2
        elif code == "xwzsxg":
            return serialiser.YjyzlsszSerializer2
        elif code == "bzxxg":
            return serialiser.YjyzlsszSerializer2
        else:
            return serialiser.YjyzlsszSerializer2

    def get(self, request, *args, **kwargs):
        try:
            resoult = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=resoult.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""智能预警历史规则修改"""


class YjyzlsszView2(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = []

    def get_queryset(self):
        all_queryset = wm.XtglYjyzsz.objects.none()

        querysetall = []
        query = wm.XtglYjyzsz.objects.filter(code=self.request.query_params.get("code"))
        querysetall.append(query)
        for i in querysetall:
            all_queryset = all_queryset | i
        return all_queryset
        # 序列化

    serializer_class = serialiser.YjyzlsszSerializer

    def get(self, request, *args, **kwargs):
        try:
            resoult = self.list(request, *args, **kwargs)

            return restful.result(message="操作成功", data=resoult.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class WaringTableView(mixins.ListModelMixin, generics.GenericAPIView):
    # todo 认证

    authentication_classes = []

    def get(self, request, *args, **kwargs):
        try:
            import datetime as dt
            # yesterday = '2019-11-14'
            yesterday = dt.date.today() + dt.timedelta(-1)
            print(yesterday)
            # mong = datetime.datetime.now().month
            # year = datetime.datetime.now().year

            # todo 在籍在校不选课
            zjzxbxkqxcs = wm.ZnyjZjzxbxk.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            zjzxbxkqrcs = wm.ZnyjZjzxbxk.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            zjzxbxkcs = zjzxbxkqrcs + zjzxbxkqxcs

            # todo 休学退学不离校
            xxtxblxqxcs = wm.ZnyjXxtxblx.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            xxtxblxqrcs = wm.ZnyjXxtxblx.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            xxtxbxlyjcs = xxtxblxqxcs + xxtxblxqrcs
            # todo 校外住宿
            xwzsqxcs = wm.ZnyjXwzsyj.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            xwzsqrcs = wm.ZnyjXwzsyj.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            xwzsyjcs = xwzsqxcs + xwzsqrcs
            # todo 不在校
            bzxqxcs = wm.ZnyjBzx.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            bzxqrcs = wm.ZnyjBzx.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            bzxyjcs = bzxqxcs + bzxqrcs
            # todo 逃课行为
            tkxwqxcs = wm.ZnyjTkxw.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            tkxwqrcs = wm.ZnyjTkxw.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            tkxwyjcs = tkxwqxcs + tkxwqrcs
            # todo 晚归
            wgqxcs = wm.ZnyjWgyj.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            wgqrcs = wm.ZnyjWgyj.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            wgyjcs = wgqxcs + wgqrcs

            # todo 上网行为
            # swxwqxcs = wm.ZnyjSwxw.objects.filter(clzt=2).filter(update_time__contains=yesterday).count()
            # swxwqrcs = wm.ZnyjSwxw.objects.filter(clzt=1).filter(update_time__contains=yesterday).count()
            # swxwyjcs = swxwqxcs + swxwqrcs

            ret = {}
            ret['yesterday'] = yesterday
            ret['zjzxbxkcs'] = zjzxbxkcs
            ret['zjzxbxkqrcs'] = zjzxbxkqrcs
            ret['zjzxbxkqxcs'] = zjzxbxkqxcs

            ret['xxtxblxqxcs'] = xxtxblxqxcs
            ret['xxtxblxqrcs'] = xxtxblxqrcs
            ret['xxtxbxlyjcs'] = xxtxbxlyjcs

            ret['xwzsqxcs'] = xwzsqxcs
            ret['xwzsqrcs'] = xwzsqrcs
            ret['xwzsqrcs'] = xwzsyjcs

            ret['bzxqxcs'] = bzxqxcs
            ret['bzxqrcs'] = bzxqrcs
            ret['bzxyjcs'] = bzxyjcs

            ret['tkxwqxcs'] = tkxwqxcs
            ret['tkxwqrcs'] = tkxwqrcs
            ret['tkxwyjcs'] = tkxwyjcs

            ret['wgqxcs'] = wgqxcs
            ret['wgqrcs'] = wgqrcs
            ret['wgyjcs'] = wgyjcs

            # ret['swxwqxcs'] = swxwqxcs
            # ret['swxwqrcs'] = swxwqrcs
            # ret['swxwyjcs'] = swxwyjcs

            # # 一年前的今天
            # start = datetime.datetime.now() - relativedelta(month=12)
            # print(start)
            # # 当前时间
            # now = datetime.datetime.now()
            # print(now)
            # # 获取近一年数据
            # data= wm.ZnyjZjzxbxk.objects.filter(create_time__range=(start, now))
            # print(data)
            # # 利用年月日进行分组查询
            # from django.db.models import Count
            #
            # res = data.extra(select={'year': 'year(create_time)', 'month': 'month(create_time)'}).values('year',
            #                                                                                              'month').annotate(
            #     count=Count('id')).order_by()
            # print(res)

            # 计算时间
            time = datetime.now() - relativedelta(years=1)
            # list集合
            # rett = ['ZnyjZjzxbxk', 'ZnyjXxtxblx', 'ZnyjBzx', 'ZnyjXwzsyj', 'ZnyjWgyj', 'ZnyjTkxw']
            # for i in range(len(rett)):
            # 获取近一年数据
            one_year_data1 = wm.ZnyjZjzxbxk.objects.filter(create_time__gte=time)
            one_year_data2 = wm.ZnyjXxtxblx.objects.filter(create_time__gte=time)
            one_year_data3 = wm.ZnyjBzx.objects.filter(create_time__gte=time)
            one_year_data4 = wm.ZnyjXwzsyj.objects.filter(create_time__gte=time)
            one_year_data5 = wm.ZnyjWgyj.objects.filter(create_time__gte=time)
            one_year_data6 = wm.ZnyjTkxw.objects.filter(create_time__gte=time)

            # 分组统计每个月的数据
            zjzxbxk_year_month = one_year_data1 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))
            xxtxblx_year_month = one_year_data2 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))
            bzx_year_month = one_year_data3 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))
            xwzs_year_month = one_year_data4 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))
            wg_year_month = one_year_data5 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))
            tkxw_year_month = one_year_data6 \
                .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
                .values('year', 'month').order_by('year', 'month').annotate(count=Count('create_time'))

            print("**************************")
            ret['zxzxbxk_year_month'] = list(zjzxbxk_year_month)
            ret['xxtxblx_year_month'] = list(xxtxblx_year_month)
            ret['bzx_year_month'] = list(bzx_year_month)
            ret['xwzs_year_month'] = list(xwzs_year_month)
            ret['wg_year_month'] = list(wg_year_month)
            ret['tkxw_year_month'] = list(tkxw_year_month)
            # query = pickle.loads()
            # zxzxbxk_year_month.query = query
            # print(query)
            return restful.result(message="操作成功", data=ret)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


""" 自定义函数，读取标签建模中设定规则，函数规则拼接SQL，并写入到数据库中"""

from datetime import datetime

def BqjmToSQL():
    yjyzs = pm.XtglBqsz.objects.all().order_by("-update_time").values('bqgz', 'zbfl').first()
    aa = yjyzs['bqgz']
    # 将str转化为dict
    print("aa:" + aa)
    if yjyzs['zbfl'] == 1:
        bb = json.loads(aa)['domlist']
        ret = []
        # todo 1.遍历列表获取索引值
        for i in bb:
            index = bb.index(i)
            ywbm = \
                json.loads(list(pm.XtglZbx.objects.filter(id=bb[index]['id']).values('zdxz'))[0]['zdxz'])['dataSelect'][
                    0][
                    'ywbm']
            zdxz = \
                json.loads(list(pm.XtglZbx.objects.filter(id=bb[index]['id']).values('zdxz'))[0]['zdxz'])['dataSelect'][
                    0][
                    'zdsjbbs']

            jsf = bb[index]['arrName'][0]['jsf']
            ysf = bb[index]['arrName'][0]['ysf']
            yz_val = bb[index]['arrName'][0]['yz_val']
            SQL = "SELECT " + 'xh, ' + jsf + "(" + zdxz + ")" + "FROM " + ywbm + " WHERE " + zdxz + ysf + yz_val
            ret.append(SQL)
        # todo 2列表中拼接字符串
        list_join = ' UNION ALL '.join(ret)
        SQL_parameters = len(ret) - 1
        SQL_result = "SELECT  xh, COUNT(*) FROM (" + list_join + ") a GROUP BY xh HAVING COUNT(*) > " + str(
            SQL_parameters)

        xsbq = pm.XtglBqsz.objects.all().order_by("-update_time").first()
        xsbq.bqSQL = SQL_result
        xsbq.create_time = datetime.now()
        xsbq.save()

    elif yjyzs['zbfl'] == 0:
        ret = []
        ysf = json.loads(aa)['ysf']
        yz_val = json.loads(aa)['yz_val']
        qzxs = json.loads(aa)['zbxmcarry'][0]['qzxs']
        ywbm = \
            json.loads(
                list(pm.XtglZbx.objects.filter(id=json.loads(aa)['zbxmcarry'][0]['id']).values('zdxz'))[0]['zdxz'])[
                'dataSelect'][0]['ywbm']
        zdxz = \
            json.loads(
                list(pm.XtglZbx.objects.filter(id=json.loads(aa)['zbxmcarry'][0]['id']).values('zdxz'))[0]['zdxz'])[
                'dataSelect'][
                0][
                'zdsjbbs']
        SQL = "SELECT " + 'xh, ' + zdxz + " * " + qzxs + " FROM " + ywbm + " WHERE " + zdxz + ysf + yz_val
        ret.append(SQL)
        # todo 3列表中拼接字符串
        list_join = ' UNION ALL '.join(ret)
        SQL_parameters = len(ret) - 1
        SQL_result = "SELECT  xh, COUNT(*) FROM (" + list_join + ") a GROUP BY zgh HAVING COUNT(*) > " + str(
            SQL_parameters)

        xsbq = pm.XtglBqsz.objects.all().order_by("-update_time").first()
        xsbq.bqSQL = SQL_result
        xsbq.update_time = datetime.now()
        xsbq.save()
    else:
        print("指标项缺少")

    # 2 获取索引和值
    # for index, value in enumerate(bb):
    #     print(index, value)


"""函数:查询标签建模SQL语句，为本专科生打标签"""


def search():
    # todo 1. 导入包 DB 连接
    from django.db import connection
    cursor = connection.cursor()

    # todo 2.按照系统管理标签设置更新时间字段取出最新的值
    sqlResult = pm.XtglBqsz.objects.all().order_by("-update_time").values('bqmc', 'bqSQL', 'bqms', 'kfqx').first()
    # todo 4.获取插入学生画像标签数据
    bqmss = sqlResult['bqms']
    kfqxs = sqlResult['kfqx']
    bqs = sqlResult['bqmc']
    sql = sqlResult['bqSQL']
    # todo 5.执行sql
    cursor.execute(sql)
    # todo 6.获取值（tupbo）
    return_arr = cursor.fetchall()
    try:
        # todo 3.按照学生画像更新字段来取出最新的值
        bq = list(pm.XshxBq.objects.all().order_by("-update_time").values('bq'))[0]['bq']
        # todo 7.循环插入mysql数据库
        if bq == bqs:
            print("修改标签有效状态为0 ，再次插入有效状态标签")
            pm.XshxBq.objects.filter(bq=bqs).update(sfyx=0)

            for item in return_arr:
                pm.XshxBq.objects.create(xh=item[0], bq=bqs, bqsm=bqmss, bqqx=kfqxs)
            # 遍历保存修改的结果，源数据（未删除）
            # for i in ret:
            #     bqsfyx = pm.XshxBq(bq=i.bq,sfyx=0,xh=i.xh,bqsm=i.bqsm,bqqx=i.bqqx,create_time=i.create_time)
            #     bqsfyx.save()
        else:
            for item in return_arr:
                pm.XshxBq.objects.create(xh=item[0], bq=bqs, bqsm=bqmss, bqqx=kfqxs)
            print("操作成功")
    except IndexError:
        print("插入数据")
        for item in return_arr:
            pm.XshxBq.objects.create(xh=item[0], bq=bqs, bqsm=bqmss, bqqx=kfqxs)

    # # todo 3 str类型的列表转化为Python中真正的列表，借用第三方工具实现
    # from ast import literal_eval
    # new_list = literal_eval(sql)
