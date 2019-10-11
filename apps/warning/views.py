# Create your views here.
import datetime

from django.db import connection
from django.db.models import Count, Q, Sum
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

        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))

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

        ret = self.list(request, *args, **kwargs)

        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}

        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            print(connection.queries)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result(message=e.detail)

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
                    it = int(request.data['clzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = wm.ZnyjZjzxbxk.objects.filter(id=i).first()
                        print(ret)
                        ser = serialiser.ZjzxbxkmxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""*****************************智能预警之休学退学不离校预警*********************************"""


class XxtxblxView(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(xxtxblx__create_time__gt=kssj) & Q(xxtxblx__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("xxtxblx", filter=myfilter)).filter(
                yjcs__gte=1).order_by("-update_time")
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(xwzs__xh=xhxm).annotate(
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
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        # <class 'rest_framework.response.Response'>
        # <class 'collections.OrderedDict'>
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)

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
    #     #         return restful.result(message=e.detail)
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
                        print(ret)
                        ser = serialiser.XxtxblxMxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""*****************************智能预警之校外住宿预警*******************************"""


class XwzsView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))
        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(xwzs__create_time__gt=kssj) & Q(xwzs__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("xwzs", filter=myfilter)).filter(
                yjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(xwzs__xh=xhxm).annotate(
                    yjcs=Count("xwzs", filter=myfilter)).filter(
                    yjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("xwzs", filter=myfilter)).filter(
                    yjcs__gte=1)

        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


'''校外住宿预警明细'''


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
            return restful.result(message=e.detail)

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
                        print(ret)
                        ser = serialiser.XwzsMxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""******************************智能预警之不在校预警***********************************"""


class BzxView(mixins.ListModelMixin, mixins.CreateModelMixin,
              mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
              generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(bzx__create_time__gt=kssj) & Q(bzx__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("bzx", filter=myfilter)).filter(
                yjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(bzx__xh=xhxm).annotate(
                    yjcs=Count("bzx", filter=myfilter)).filter(
                    yjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("bzx", filter=myfilter)).filter(
                    yjcs__gte=1)

        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)

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
                        print(ret)
                        ser = serialiser.BzxMxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""*****************************智能预警之逃课行为预警*****************************"""


class TkxwView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))

        xhxm = self.request.query_params.get('xhxm', None)
        myfilter = Q(tkxw__create_time__gt=kssj) & Q(tkxw__create_time__lt=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(yjcs=Count("tkxw", filter=myfilter)).filter(
                yjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(tkxw__xh=xhxm).annotate(
                    yjcs=Count("tkxw", filter=myfilter)).filter(
                    yjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(
                    yjcs=Count("tkxw", filter=myfilter)).filter(
                    yjcs__gte=1)
        return ret

    # 序列化
    serializer_class = serialiser.BzksSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)

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
                        print(ret)
                        ser = serialiser.TkxwMxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""***********************************智能预警之晚归预警************************************"""


class WgView(mixins.ListModelMixin, mixins.CreateModelMixin,
             mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
             generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))

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
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}

        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)

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
                        ser = serialiser.WgMxSerialiser(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['clzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result(message=e.detail)


"""*****************************智能预警之上网行为预警*****************************"""


class SwxwView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))
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
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)


"""******************************行为轨迹分析-**************************"""


class XwgjView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               generics.GenericAPIView, ):
    # authentication_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", datetime.date.min)
        jssj = self.request.query_params.get("jssj", datetime.date.today() + datetime.timedelta(days=1))
        xhxm = self.request.query_params.get('xhxm', None)
        print(xhxm)

        myfilter = Q(grgj__create_time__gt=kssj) & Q(grgj__create_time__lte=jssj)

        if not xhxm:
            ret = pm.UibeBzks.objects.annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                gjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeBzks.objects.filter(grgj__xh=xhxm).annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
            else:
                ret = pm.UibeBzks.objects.filter(xm=xhxm).annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
        return ret

    # 序列化
    serializer_class = serialiser.BzksXwgjSerialiser
    filter_class = filter.BzksFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xznj', 'bj', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        d = {"kssj": self.request.query_params.get("kssj", datetime.date.min),
             "jssj": self.request.query_params.get("jssj", datetime.date.today())}
        return restful.result(message="操作成功", data=ret.data, kwargs=d)


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
            return restful.result(message=e.detail)


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


"""下拉列表"""


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
            return restful.result2(message=e.detail)

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
            return restful.result2(message=e.detail)

    # """更新"""
    #
    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.TkxwxgSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


"""预警阈值之晚归预警修改"""


class WgxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.WgxgSerializer
    #
    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.WgxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message=e.detail)

    # """更新"""
    #
    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.WgxgSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


"""预警阈值之休学退学不离校预警修改"""


class XxtxblxxgView(mixins.CreateModelMixin, generics.GenericAPIView, ):
    # 认证类
    # authentication_classes = []
    # 查询出来所有数据按照创建时间进行排序
    queryset = wm.XtglYjyzsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.XxtxblxxgSerializer

    # def patch(self, request, id):
    #     ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #     ser = serialiser.XxtxblxxgSerializer(instance=ret, many=False)
    #     return restful.result(message="查询成功", data=ser.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            ret = self.create(request, *args, **kwargs)
            # print(connection.queries)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message=e.detail)

    # """更新"""
    #
    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.XxtxblxxgSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


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
            return restful.result2(message=e.detail)

    # """更新"""
    #
    # def put(self, request, *args, **kwargs):
    #     print(request.data)
    #     try:
    #
    #         # self.partial_update(request, *args, **kwargs)
    #         ret = wm.XtglYjyzsz.objects.filter(id=request.data['id']).first()
    #         ser = serialiser.XwzsxgSerializer(instance=ret, data=request.data, partial=True)
    #         if ser.is_valid():
    #             ser.save()
    #         return restful.ok()
    #     except Exception as e:
    #         return restful.result(message=e.detail)


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
            return restful.result2(message=e.detail)

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


# from django.core import serializers as serializ
# import json
# from django.http import JsonResponse


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
        ret1 = self.list(request, *args, **kwargs)

        # bzx = wm.XtglYjyzsz.objects.filter(code='bzxxg').order_by("-update_time")[0:1]
        # data = serializ.serialize("json", bzx)
        # loads = json.loads(data)
        # # return JsonResponse(loads, safe=False)
        # # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret1.data)

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
                        print(ret)
                        ser = serialiser.YjyzszSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message=e.detail)


"""预警阈值历史设置查询"""


class YjyzlsszView(mixins.ListModelMixin, generics.GenericAPIView):
    # authentication_classes = []

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
        resoult = self.list(request, *args, **kwargs)
        return restful.result(message="操作成功", data=resoult.data)
