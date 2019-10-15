# Create your views here.

from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.base import filter
from apps.portrait import models as pm
from apps.utils import restful
from apps.utils import serialiser
from apps.utils.pagination import Pagination


class JqszView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
    """系统管理之假期设置"""
    # authentication_classes = []

    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.XtglJq.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.JqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.JqFilter
    """获取所有数据"""

    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)

    """删除"""

    # @action(methods=['delete'], detail=False)
    def delete(self, request, *args, **kwargs):
        id = request.query_params.get('id', None)
        if not id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in id.split(','):
            get_object_or_404(pm.XtglJq, pk=int(i)).delete()
        return restful.ok()

    """添加数据"""

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            it = request.data['jqmc']
            try:
                mc = list(pm.XtglJq.objects.filter(jqmc=it).values('jqmc'))[0]["jqmc"]
                return restful.result2(message="请勿重复保存操作")
            except IndexError:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message=e.detail)

    """更新数据"""

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = pm.XtglJq.objects.filter(id=request.data['id']).first()
            ser = serialiser.JqSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message=e.detail)

    """批量更新状态"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(pm.XtglJq.objects.filter(id=i).values('kqzt'))[0]['kqzt']
                    it = int(request.data['kqzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = pm.XtglJq.objects.filter(id=i).first()
                        print(ret)
                        ser = serialiser.JqSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message=e.detail)


class BqwdView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
    """系统管理之标签维度管理"""
    # authentication_classes = []
    # permission_classes = []

    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.XtglBqwd.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.BqwdSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.BqwdFilter
    """获取所有数据"""

    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)

    """删除"""

    def delete(self, request, *args, **kwargs):
        id = request.query_params.get('id', None)
        if not id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in id.split(','):
            get_object_or_404(pm.XtglBqwd, pk=int(i)).delete()
        return restful.ok()

    """添加数据"""

    def post(self, request, *args, **kwargs):
        try:
            it = request.data['wdmc']
            try:
                mc = list(pm.XtglBqwd.objects.filter(wdmc=it).values('wdmc'))[0]["wdmc"]
                return restful.result2(message="请勿重复保存操作")
            except IndexError:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message=e.detail)

    """更新数据"""

    def put(self, request, *args, **kwargs):

        try:
            # self.partial_update(request, *args, **kwargs)
            ret = pm.XtglBqwd.objects.filter(id=request.data['id']).first()
            ser = serialiser.BqwdSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message=e.detail)

    """更新状态"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(pm.XtglBqwd.objects.filter(id=i).values('kqzt'))[0]['kqzt']
                    it = int(request.data['kqzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = pm.XtglBqwd.objects.filter(id=i).first()
                        print(ret)
                        ser = serialiser.BqwdSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message=e.detail)


class HxbqszfzView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    """系统管理之画像标签设置之复制标签"""
    queryset = pm.XtglBqsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.BqszSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.HxbqszFilter
    """复制标签"""

    def put(self, request, *args, **kwargs):
        try:
            ret = pm.XtglBqsz.objects.get(id=request.data['id'])

            xtglbqsz = pm.XtglBqsz(bqmc=ret.bqmc + "_副本", zbfl=ret.zbfl, zbwd=ret.zbwd, zbx=ret.zbx, bqgz=ret.bqgz,
                                   bqms=ret.bqms
                                   , kfqx=ret.kfqx, create_time=ret.create_time, update_time=datetime.now())
            xtglbqsz.save()
            return restful.ok()
        except Exception:
            return restful.result2(message="操作失败")


class HxbqszView(mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                 generics.GenericAPIView, ):
    """系统管理之画像标签设置"""
    # authentication_classes = []
    # permission_classes = []

    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.XtglBqsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.BqszSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.HxbqszFilter
    """获取所有数据"""

    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)

    """添加数据"""

    def post(self, request, *args, **kwargs):

        try:
            it = request.data['bqmc']
            try:
                mc = list(pm.XtglBqsz.objects.filter(bqmc=it).values('bqmc'))[0]["bqmc"]
                return restful.result2(message="请勿重复保存操作")
            except IndexError:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败")

    """更新数据"""

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = pm.XtglBqsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.BqszSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败")

    """更新状态"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(pm.XtglBqsz.objects.filter(id=i).values('kqzt'))[0]['kqzt']
                    it = int(request.data['kqzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = pm.XtglBqsz.objects.filter(id=i).first()
                        print(ret)
                        ser = serialiser.BqszSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message="操作失败")

    """删除"""

    def delete(self, request, *args, **kwargs):
        id = request.query_params.get('id', None)
        if not id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in id.split(','):
            get_object_or_404(pm.XtglBqsz, pk=int(i)).delete()
        return restful.ok()


class HxbqszZbxView(mixins.ListModelMixin, generics.GenericAPIView):
    """画像标签设置新增之指标项选择"""

    # authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序

    def get_queryset(self):
        all_queryset = pm.XtglZbx.objects.none()
        ids = self.request.query_params.get('id').split(",")
        print(ids)
        querysetall = []
        for i in ids:
            rets = pm.XtglZbx.objects.filter(zbwd__icontains=i).filter(kqzt=1)
            querysetall.append(rets)
        for i in querysetall:
            all_queryset = all_queryset | i
        return all_queryset

    # 序列化
    serializer_class = serialiser.HxbqszZbxSerializer
    # 过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.HxbqszZbxFilter
    """获取所有数据"""

    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        return restful.result(message="操作成功", data=ret.data)


class ZbxView(mixins.ListModelMixin, mixins.CreateModelMixin,
              mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
    """系统管理之指标项管理"""
    # authentication_classes = []
    # permission_classes = []

    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.XtglZbx.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.ZbxglSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.ZbxglFilter
    """获取所有数据"""

    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)

    """添加数据"""

    def post(self, request, *args, **kwargs):
        try:
            it = request.data['zbxmc']
            try:

                mc = list(pm.XtglZbx.objects.filter(zbxmc=it).values('zbxmc'))[0]["zbxmc"]
                return restful.result2(message="请勿重复保存操作")
            except IndexError:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败")

    """更新数据"""

    def put(self, request, *args, **kwargs):
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = pm.XtglZbx.objects.filter(id=request.data['id']).first()
            ser = serialiser.ZbxglSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败")

    """更新状态"""

    def patch(self, request, *args, **kwargs):
        try:
            if not request.data['id']:
                return restful.result2(message="请选择您想要更新的数据")
            else:
                for i in request.data['id'].split(','):
                    zt = list(pm.XtglZbx.objects.filter(id=i).values('kqzt'))[0]['kqzt']
                    it = int(request.data['kqzt'])
                    if zt == it:
                        # return JsonResponse(rt)
                        return restful.result2(message="请勿重复操作")
                    else:
                        ret = pm.XtglZbx.objects.filter(id=i).first()
                        print(ret)
                        ser = serialiser.ZbxglSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            return restful.result2(message="操作失败")

    """删除"""

    def delete(self, request, *args, **kwargs):
        id = request.query_params.get('id', None)
        if not id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in id.split(','):
            get_object_or_404(pm.XtglZbx, pk=int(i)).delete()
        return restful.ok()


class SjbxzView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """数据表选择"""
    # authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    # queryset = pm.Sjzb.objects.all()
    def get_queryset(self):
        zywbm = self.request.query_params.get('zywbm', None)
        if not zywbm:
            ret = pm.Sjzb.objects.all()
        else:
            if zywbm.isalpha():
                ret = pm.Sjzb.objects.filter(zwbm=zywbm)
            else:
                ret = pm.Sjzb.objects.filter(ywbm=zywbm)
        return ret

    # 序列化
    serializer_class = serialiser.SjbxzSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.SjbxzFilter

    # 获取数据
    def get(self, request, *args, **kwargs):
        # print(type(request.data))
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)


class SjbxzzdView(viewsets.ModelViewSet):
    """数据表字段选择"""
    authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        all_queryset = pm.Sjzbzd.objects.none()
        sjzb_id = self.request.query_params.get('id').split(",")
        querysetall = []
        for i in sjzb_id:
            rets = pm.Sjzbzd.objects.filter(sjzb_id=i)
            querysetall.append(rets)
        for i in querysetall:
            all_queryset = all_queryset | i
        return all_queryset

    # 序列化

    serializer_class = serialiser.SjbxzzdSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.SjbxzzdFilter

    # 获取数据
    def retrieve(self, request, *args, **kwargs):
        try:
            # print(self.request.query_params.get('sjzb_id').split(","))
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败")

    # 获取数据
    # def get(self, request, *args, **kwargs):
    #     # print(type(request.data))
    #     ret = self.list(request, *args, **kwargs)
    #     # print(connection.queries[-1:])
    #     return restful.result(message="操作成功", data=ret.data)

    def post(self, request, *args, **kwargs):
        # ret = pm.Sjzbzd.objects.filter(sjzb_id=request.data['id'])
        # ser = serialiser.SjbxzzdSerializer(instance=ret, many=True, )
        # dumps = json.dumps(ser.data, ensure_ascii=False)
        # print(type(dumps))
        # return restful.result(data=dumps)
        try:
            # print(self.request.query_params.get('sjzb_id').split(","))
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败")


class JshxView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """教师画像管理员"""
    # authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.UibeJzg.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.UibeJzgSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.UibeJzgFilter

    def get(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)


class JshxxqView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """教师画像详情"""

    # authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        xhs = self.request.query_params.get('zgh')
        ret = pm.UibeJzg.objects.filter(zgh=xhs)
        return ret

    # 序列化
    serializer_class = serialiser.UibeJzgXqSerializer

    def get(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)


class JshxzcxqView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    """教师画像职称详情"""
    # authentication_classes = []

    queryset = pm.Zcdj.objects.all()
    # 序列化
    serializer_class = serialiser.UibeJzgZcXqSerializer

    def post(self, request, *args, **kwargs):
        try:
            qxrs = pm.UibeJzg.objects.filter(zcjb=request.data['zcjb']).count()
            co = list(pm.Zcdj.objects.filter(zcjb=request.data['zcjb']).values('code'))
            mbjb = list(pm.Zcdj.objects.filter(code=str(int(co[0]['code']) + 1)).values('zcjb'))
            bmrs = pm.UibeJzg.objects.filter(zcjb=request.data['zcjb']).filter(bm=request.data['bm']).count()
            bdrq = list(pm.UibeJzg.objects.filter(zgh=request.data['zgh']).extra(
                select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d')"}).values('zcjbbdrq'))
            # DateTime类型extra(select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d %%H:%%i:%%s')"}).values('zcjbbdrq')
            # Date类型extra(select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d')"}).values('zcjbbdrq')
            ret = {}
            ret['qxrs'] = qxrs
            ret['zcjb'] = request.data['zcjb']
            ret['bmrs'] = bmrs
            ret['bdrq'] = bdrq[0]['zcjbbdrq']
            ret['xymb'] = mbjb[0]['zcjb']
            rets = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=rets.data, kwargs=ret)
        except Exception as e:
            return restful.result2(message="操作失败")


class XshxJsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像教师端"""
    # authentication_classes = []
    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.UibeBzks.objects.all()
    # 序列化
    serializer_class = serialiser.XshxJstSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdFilter

    def get(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)


class XshxXsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像学生端"""

    #  authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        xhs = self.request.query_params.get('xh')
        ret = pm.XshxBq.objects.filter(bqqx=1).filter(xh=xhs)
        return ret

    # queryset = pm.XshxBq.objects.filter(bqqx=1).filter()
    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdXqFilter

    def get(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)


class XshxJsdXqVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像教师端详情"""
    # authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        xhs = self.request.query_params.get('xh')
        ret = pm.XshxBq.objects.filter(xh=xhs)
        return ret

    # queryset = pm.XshxBq.objects.filter()
    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdXqFilter

    def get(self, request, *args, **kwargs):
        ret = self.list(request, *args, **kwargs)
        # print(connection.queries[-1:])
        return restful.result(message="操作成功", data=ret.data)
