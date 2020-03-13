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
from apps.warning.views import BqjmToSQL,search


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
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """删除"""

    # @action(methods=['delete'], detail=False)
    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params.get('id', None)
            if not id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in id.split(','):
                get_object_or_404(pm.XtglJq, pk=int(i)).delete()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """删除"""

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params.get('id')
            if id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in id.split(','):
                get_object_or_404(pm.XtglBqwd, pk=int(i)).delete()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)


class HxbqszfzView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    """系统管理之画像标签设置之复制标签"""
    queryset = pm.XtglBqsz.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = serialiser.BqszSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.HxbqszFilter
    """点击复制标签"""

    def put(self, request, *args, **kwargs):
        try:
            ret = pm.XtglBqsz.objects.get(id=request.data['id'])

            xtglbqsz = pm.XtglBqsz(bqmc=ret.bqmc + "_副本", zbfl=ret.zbfl, zbwd=ret.zbwd, zbx=ret.zbx, bqgz=ret.bqgz,
                                   bqms=ret.bqms
                                   , bqqx=ret.bqqx, create_time=ret.create_time, update_time=datetime.now())
            xtglbqsz.save()
            # BqjmToSQL()
            # search()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """添加数据"""

    def post(self, request, *args, **kwargs):

        try:
            it = request.data['bqmc']
            try:
                mc = list(pm.XtglBqsz.objects.filter(bqmc=it).values('bqmc'))[0]["bqmc"]
                return restful.result2(message="请勿重复保存操作")
            except IndexError:
                ret = self.create(request, *args, **kwargs)
                BqjmToSQL()
                search()
                return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """更新数据"""

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = pm.XtglBqsz.objects.filter(id=request.data['id']).first()
            ser = serialiser.BqszSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            # BqjmToSQL()
            # search()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

    """删除"""

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params.get('id', None)
            if not id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in id.split(','):
                get_object_or_404(pm.XtglBqsz, pk=int(i)).delete()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)

    """删除"""

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params.get('id', None)
            if not id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in id.split(','):
                get_object_or_404(pm.XtglZbx, pk=int(i)).delete()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
            if check_contain_chinese(zywbm):
                ret = pm.Sjzb.objects.filter(zwbm__icontains=zywbm)
            else:
                ret = pm.Sjzb.objects.filter(ywbm__icontains=zywbm)
        return ret

    # 序列化
    serializer_class = serialiser.SjbxzSerializer

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.SjbxzFilter
    search_fields = ('zwbm', 'ywbm')

    # 获取数据
    def get(self, request, *args, **kwargs):
        try:
            # print(type(request.data))
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


# todo  自定义方法，判断当前字符串中是否含有中文字符
def check_contain_chinese(self):
    # 在python3中要先把字节字符解码，然后转变为字符
    for ch in self.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        return False


class SjbxzzdView(viewsets.ModelViewSet):
    """数据表字段选择"""
    # authentication_classes = []   # 分页
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
            return restful.result2(message="操作失败", data=e.args)

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
            return restful.result2(message="操作失败", data=e.args)


class BmVIew(mixins.ListModelMixin, generics.GenericAPIView):
    "教师画像管理员下拉列表"
    # 查询
    queryset = pm.UibeJzg.objects.filter(bm__isnull=False).values('bm').distinct()
    # 序列化
    serializer_class = serialiser.UibeJzgBmSerializer

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


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
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class JshxzcxqView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    """教师画像职称详情"""

    # authentication_classes = []
    def get_queryset(self):
        zgh = self.request.data["zgh"]
        ret = pm.JzgZcxq.objects.filter(zgh=zgh)
        return ret

    # queryset = pm.JzgZcxq.objects.all()
    # 序列化
    serializer_class = serialiser.UibeJzgZcXqSerializer

    def post(self, request, *args, **kwargs):

        try:
            bdrq = request.data['zcbdrq']
            if bdrq:
                zcbdrq = datetime.strptime(request.data['zcbdrq'], '%Y%m%d').date()
            else:
                zcbdrq = ''
            # dqzc=request.data['zcxx']
            # if dqzc:
            #     print(dqzc)
            # else:
            #     dqzc=''
            dqzc = list(pm.UibeJzg.objects.filter(zgh=request.data["zgh"]).values('zcxx'))[0]['zcxx']
            qxrs = pm.UibeJzg.objects.filter(zcxxdm=request.data['zcxxdm']).count()
            bmrs = pm.UibeJzg.objects.filter(zcxxdm=request.data['zcxxdm']).filter(bmdm=request.data['bmdm']).count()

            # mb = list(pm.JzgZcxx.objects.filter(zwdm=str(int(request.data['zcxxdm']) - 1)).values('zwmc'))

            # co = list(pm.JzgZcxx.objects.filter(zcjb=request.data['zcjb']).values('code'))
            # mbjb = list(pm.Zcdj.objects.filter(code=str(int(co[0]['code']) + 1)).values('zcjb'))

            # bdrq = list(pm.UibeJzg.objects.filter(zgh=request.data['zgh']).extra(
            #    select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d')"}).values('zcjbbdrq'))
            # DateTime类型extra(select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d %%H:%%i:%%s')"}).values('zcjbbdrq')
            # Date类型extra(select={"zcjbbdrq": "DATE_FORMAT(zcjbbdrq, '%%Y-%%m-%%d')"}).values('zcjbbdrq')
            ret = {}
            ret['zcbdrq'] = zcbdrq
            ret['dqzc'] = dqzc
            ret['qxrs'] = qxrs
            ret['bmrs'] = bmrs
            # if mb:
            #     ret['mb'] = mb
            # else:
            #     ret['mb'] = '您已巅峰'

            # ret['zcjb'] = request.data['zcjb']
            # ret['bdrq'] = bdrq[0]['zcjbbdrq']
            # ret['xymb'] = mbjb[0]['zcjb']
            rets = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=rets.data, kwargs=ret)

        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class XshxJsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像教师端"""
    # authentication_classes = []
    # 分页
    pagination_class = Pagination
    # 查询出来所有数据按照创建时间进行排序
    queryset = pm.UibeBzks.objects.all()  # .filter(sfyx=1)
    # 序列化
    serializer_class = serialiser.XshxJstSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdFilter

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class XshxXsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像学生端"""

    #  authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):

        xhs = self.request.query_params.get('xh')
        ret = pm.XshxBq.objects.filter(bqqx=1).filter(xh=xhs, sfyx=1)
        return ret

    # queryset = pm.XshxBq.objects.filter(bqqx=1).filter()
    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdXqFilter

    def get(self, request, *args, **kwargs):
        try:
            xbdm = {}
            ret = self.list(request, *args, **kwargs)
            xhs = self.request.query_params.get('xh')
            xb = list(pm.UibeBzks.objects.filter(xh=xhs).values('xb'))[0]['xb']
            xbdm['xbdm'] = xb
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data, kwargs=xbdm)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class XshxJsdXqVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    """用户画像之学生画像教师端详情"""
    # token认证
    # authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        xhs = self.request.query_params.get('xh')
        ret = pm.XshxBq.objects.filter(xh=xhs, sfyx=1)
        return ret

    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    filter_class = filter.XshxJsdXqFilter

    def get(self, request, *args, **kwargs):
        try:
            xbdm = {}
            ret = self.list(request, *args, **kwargs)
            xhs = self.request.query_params.get('xh')
            xb = list(pm.UibeBzks.objects.filter(xh=xhs).values('xb'))[0]['xb']
            xbdm['xbdm'] = xb
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data, kwargs=xbdm)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)
