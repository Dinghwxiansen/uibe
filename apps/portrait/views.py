# Create your views here.
import json
from datetime import *

from django.db import connection
from django.db.models import Count
from django.db.models import Q
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
from apps.utils.Sample_username_ip import ip_username, time_cmp
from apps.utils.pagination import Pagination
from apps.warning import models as wm

"""导入自定义日志模块"""
import logging

logger = logging.getLogger("django")

"""***************系统管理之假期设置***************"""


class JqszView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """添加数据"""

    def post(self, request, *args, **kwargs):
        print(request.data['jqkssj'], request.data['jqjssj'])

        if time_cmp(request.data['jqkssj'], request.data['jqjssj']) > 0:
            return restful.result2(message="假期开始时间不能大于结束时间")
        else:
            try:
                mc = pm.XtglJq.objects.filter(jqmc=request.data['jqmc'])
                if mc.exists():
                    return restful.result2(message="请勿重复保存操作")
                else:
                    ret = self.create(request, *args, **kwargs)
                    return restful.result(message="保存成功")
            except Exception as e:
                ip_username(request)
                return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""**************系统管理之标签维度管理**********"""


class BqwdView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """删除"""

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params.get('id', None)
            if not id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in id.split(','):
                get_object_or_404(pm.XtglBqwd, pk=int(i)).delete()
            return restful.ok()
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """添加数据"""

    def post(self, request, *args, **kwargs):
        try:
            mc = pm.XtglBqwd.objects.filter(wdmc=request.data['wdmc'])
            if mc.exists():
                return restful.result2(message="请勿重复保存操作")
            else:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""***********系统管理之画像标签设置之复制标签*********"""


class HxbqszfzView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""**************系统管理之画像标签设置*************"""


# 20200927 添加过滤条件是否删除


class HxbqszView(mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                 generics.GenericAPIView, ):
    # authentication_classes = []
    # permission_classes = []

    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    # todo 20200927 添加过滤条件是否删除,sfsc=0,表示未删除。新增权限
    # queryset = pm.XtglBqsz.objects.all().order_by("-update_time")
    def get_queryset(self):

        user = self.request.user
        user_type = self.request.user.user_type

        if user_type == 0:
            # 管理员
            all_queryset = pm.XtglBqsz.objects.filter(sfsc=0, ).order_by("-update_time")
        else:
            # 教师，学生
            all_queryset = pm.XtglBqsz.objects.filter(sfsc=0, bqqx=user_type).order_by("-update_time")

        print(user, user_type)
        return all_queryset

    # queryset = pm.XtglBqsz.objects.filter(sfsc=0).order_by("-update_time")
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """添加数据"""

    def post(self, request, *args, **kwargs):

        # try:
        # 20200927 添加是否删除的过滤条件
        bqmc = pm.XtglBqsz.objects.filter(bqmc=request.data['bqmc'], sfsc=0)
        print(request.data)
        if bqmc.exists():
            return restful.result2(message="请勿重复保存操作")
        else:
            ret2 = self.create(request, *args, **kwargs)
            # search()
            return restful.result(message="保存成功")
        # except Exception as e:
        #    ip_username(request)
        #    return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    # 重写保存save的逻辑
    def perform_create(self, BqszSerializer):
        # self.get_success_headers(BqszSerializer.data)
        instance = BqszSerializer.save()
        it = self.request.data['bqmc']
        bqgz = self.request.data['bqgz']
        zbfl = self.request.data['zbfl']
        print(type(bqgz))
        print(zbfl)
        if zbfl == 1:
            print("指标分类为1,非权重标签")
            domlist_list = json.loads(bqgz)['domlist']
            # 定义空数组
            ret = []
            # todo 1 遍历列表获取索引值
            for i in range(len(domlist_list)):
                # domlist_list_i_ = domlist_list[i]
                # print(domlist_list_i_)
                # TODO 查询指标项中指标分类是否为单字段多字段进行分类处理
                zbxfl = list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('zbfl'))[0]['zbfl']
                #  TODO、画像标签设置之标签建模单一字段处理
                if zbxfl == 0:
                    ywbm_ = json.loads(
                        list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('zdxz'))[0]['zdxz'])[
                        'dataSelect'][0]['ywbm']
                    zdxz = json.loads(
                        list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('zdxz'))[0]['zdxz'])[
                        'dataSelect'][0]['zdsjbbs']
                    jsf = domlist_list[i]['arrName'][0]['jsf']
                    ysf = domlist_list[i]['arrName'][0]['ysf']
                    yz_val = domlist_list[i]['arrName'][0]['yz_val']
                    if jsf == 'value':
                        print("本次计算value")
                        SQL = 'SELECT ' + ' xh ' + ' FROM ' + ywbm_ + ' WHERE ' + zdxz + ysf + "'" + yz_val + "'"
                    elif jsf == 'sum':
                        print("本次计算sum")
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'Max':
                        print("本次计算max")
                        SQL = 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' FROM ' + ywbm_
                    elif jsf == 'Min':
                        print('本次计算Min')
                        SQL = 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' FROM ' + ywbm_
                    elif jsf == 'average':
                        print('本次计算平均值')
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + " AVG " + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'count':
                        print('本次计算count')
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'Top':
                        SQL = 'SELECT ' + ' xh ' + ' FROM ' + ywbm_ + ' WHERE ' + zdxz + ysf + "'" + yz_val + "'"
                # TODO 画像标签设置之标签建模多字段处理
                elif zbxfl == 1:
                    print(domlist_list[i])
                    print(list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('jsgz')))
                    ywbm_ = json.loads(
                        list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('jsgz'))[0]['jsgz'])[
                        'yunsuan'][0]['ywbm']
                    print(ywbm_)
                    zdxz = json.loads(
                        list(pm.XtglZbx.objects.filter(id=domlist_list[i]['id']).values('jsgz'))[0]['jsgz'])[
                        'yunsuan'][0]['ysfval']
                    jsf = domlist_list[i]['arrName'][0]['jsf']
                    ysf = domlist_list[i]['arrName'][0]['ysf']
                    yz_val = domlist_list[i]['arrName'][0]['yz_val']
                    if jsf == 'value':
                        print("本次计算value")
                        SQL = 'SELECT ' + ' xh ' + ' FROM ' + ywbm_ + ' WHERE ' + zdxz + ysf + "'" + yz_val + "'"
                    elif jsf == 'sum':
                        print("本次计算sum")
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'Max':
                        print("本次计算max")
                        SQL = 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' FROM ' + ywbm_
                    elif jsf == 'Min':
                        print('本次计算Min')
                        SQL = 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' FROM ' + ywbm_
                    elif jsf == 'average':
                        print('本次计算平均值')
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + " AVG " + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'count':
                        print('本次计算count')
                        SQL = 'select xh from (' + 'SELECT ' + ' xh, ' + jsf + '(' + zdxz + ')' + ' as v ' + 'FROM ' + ywbm_ + ' group by  xh ' + ') b ' + ' where b.v ' + ysf + "' " + yz_val + "'"
                    elif jsf == 'Top':
                        SQL = 'SELECT ' + ' xh ' + ' FROM ' + ywbm_ + ' WHERE ' + zdxz + ysf + "'" + yz_val + "'"

                ret.append(SQL)
            # todo 2 列表中拼接字符串
            unionall = ' UNION ALL '.join(ret)
            SQL_parameters = len(ret) - 1
            sql = 'SELECT xh , count(*) FROM ( ' + unionall + " ) a GROUP BY xh HAVING count(*) > " + str(
                SQL_parameters)
            cursor = connection.cursor()
            cursor.execute(sql)
            return_arr = cursor.fetchall()
            for item in return_arr:
                # pm.XshxBq.objects.create(xh=item[0], bq=instance.bqmc, bqsm=instance.bqms, bqqx=instance.bqqx,
                #                          sfyx=instance.kqzt)
                pm.XshxBq.objects.create(xh=item[0], sfyx=instance.kqzt, bq_id=instance.id, )

            instance.bqSQL = sql

            instance.save()

        elif zbfl == 0:
            print("指标分类为0 ，权重标签")
            ysf = json.loads(bqgz)['ysf']
            yz_val = json.loads(bqgz)['yz_val']
            zbxmcarry_ = json.loads(bqgz)['zbxmcarry']
            ret = []
            for i in range(len(zbxmcarry_)):
                # TODO 查询指标项中指标分类是否为单字段多字段进行分类处理
                zbxfl = list(pm.XtglZbx.objects.filter(id=zbxmcarry_[i]['id']).values('zbfl'))[0]['zbfl']
                if zbxfl == 0:
                    # todo 指标项单字段计算
                    ywbm_ = json.loads(
                        list(pm.XtglZbx.objects.filter(id=zbxmcarry_[i]['id']).values('zdxz'))[0]['zdxz'])[
                        'dataSelect'][0]['ywbm']
                    zdxz = json.loads(
                        list(pm.XtglZbx.objects.filter(id=zbxmcarry_[i]['id']).values('zdxz'))[0]['zdxz'])[
                        'dataSelect'][0]['zdsjbbs']
                    qzxs = json.loads(zbxmcarry_[i]['qzxs'])

                    SQL = 'SELECT ' + ' xh ,' + zdxz + ' * ' + qzxs + " as b " + ' FROM ' + ywbm_
                elif zbxfl == 1:
                    # tido 指标项多字段计算
                    print("指标项为多字段处理")
                    ywbm_ = json.loads(
                        list(pm.XtglZbx.objects.filter(id=zbxmcarry_[i]['id']).values('jsgz'))[0]['jsgz'])[
                        'yunsuan'][0]['ywbm']
                    zdxz = json.loads(
                        list(pm.XtglZbx.objects.filter(id=zbxmcarry_[i]['id']).values('jsgz'))[0]['jsgz'])[
                        'yunsuan'][0]['ysfval']
                    qzxs = json.loads(zbxmcarry_[i]['qzxs'])
                    SQL = 'SELECT ' + ' xh, ' + ' ( ' + zdxz + ' * ' + qzxs + ' ) ' + ' as b ' + ' FROM' + ywbm_
                ret.append(SQL)
            # 列表中拼接字符串
            join = " UNION ALL ".join(ret)
            sql = 'SELECT xh,sum (a.b) FROM ( ' + join + " ) a GROUP BY a.xh HAVING sum(a.b)  " + ysf + yz_val
            instance.bqSQL = sql

            instance.save()

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
                        print(request.data, type(request.data))
                        ser = serialiser.BqszSerializer(instance=ret, data=request.data, partial=True)
                        if ser.is_valid():
                            ser.save()
                if int(request.data['kqzt']) == 0:
                    return restful.result(message="操作成功，状态关闭")
                else:
                    return restful.result(message="操作成功，状态开启")
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """删除"""
    '''
    20200927 修改删除方法，实现逻辑删除
    '''

    def delete(self, request, *args, **kwargs):
        try:
            ids = request.query_params.get('id', None)
            if not ids:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in ids.split(','):
                # get_object_or_404(pm.XtglBqsz, pk=int(i)).delete()
                ret = pm.XtglBqsz.objects.filter(id=i).first()
                request.data['sfsc'] = 1
                print(request.data)
                ser = serialiser.BqszSerializer(instance=ret, data=request.data, partial=True)
                if ser.is_valid():
                    ser.save()
            return restful.ok()
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""**************画像标签设置新增之指标项选择*******"""


class HxbqszZbxView(mixins.ListModelMixin, generics.GenericAPIView):

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""****************系统管理之指标项管理**********"""


class ZbxView(mixins.ListModelMixin, mixins.CreateModelMixin,
              mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

    """添加数据"""

    def post(self, request, *args, **kwargs):
        try:
            mc = pm.XtglZbx.objects.filter(zbxmc=request.data['zbxmc'])
            if mc.exists():
                return restful.result2(message="请勿重复保存操作")
            else:
                ret = self.create(request, *args, **kwargs)
                return restful.result(message="保存成功")
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""*****************数据表选择******************"""


class SjbxzView(mixins.ListModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


# todo  自定义方法，判断当前字符串中是否含有中文字符
def check_contain_chinese(self):
    # 在python3中要先把字节字符解码，然后转变为字符
    for ch in self.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        return False


"""***************数据表字段选择********************"""


class SjbxzzdView(viewsets.ModelViewSet):
    # authentication_classes = []   # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    """
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
    """

    def get_queryset(self):
        params_get = self.request.query_params.get('zbfl')
        sjzb_id = self.request.query_params.get('id')
        if int(params_get) == 0:
            rets = pm.Sjzbzd.objects.filter(sjzb_id=sjzb_id)
            return rets
        elif int(params_get) == 1:
            ret = pm.Sjzbzd.objects.filter(Q(sjzb_id=sjzb_id) & ~Q(sjlx="String"))
            return ret

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"*****************教师画像管理员下拉列表*************"


class BmVIew(mixins.ListModelMixin, generics.GenericAPIView):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""******************教师画像管理员******************"""


class JshxView(mixins.ListModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""******************教师画像详情*********************"""


class JshxxqView(mixins.ListModelMixin, generics.GenericAPIView, ):

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""****************教师画像职称详情**********************8"""


class JshxzcxqView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""****************用户画像之学生画像教师端***************"""


class XshxJsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""****************用户画像之学生画像学生端****************"""


class XshxXsdVIew(mixins.ListModelMixin, generics.GenericAPIView, ):

    #  authentication_classes = []

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):

        xhs = self.request.query_params.get('xh')
        # ret = pm.XshxBq.objects.filter(bqqx=1).filter(xh=xhs, sfyx=1)
        # todo 20200924 表关联后修改filter条件
        # ret = pm.XtglBqsz.objects.filter(bqqx=0).filter(xshxbq__xh=xhs, xshxbq__sfyx=1)
        ret = pm.XtglBqsz.objects.filter(bqqx=0).filter(xshxbq__sfyx=1, xshxbq__xh=xhs)
        return ret

    # queryset = pm.XshxBq.objects.filter(bqqx=1).filter()
    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    # filter_class = filter.XshxJsdXqFilter
    filter_class = filter.HxbqszFilter

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""***************用户画像之学生画像教师端详情************"""


class XshxJsdXqVIew(mixins.ListModelMixin, generics.GenericAPIView, ):
    # token认证
    # authentication_classes = []
    # 分页
    pagination_class = Pagination

    # 查询出来所有数据按照创建时间进行排序
    def get_queryset(self):
        xhs = self.request.query_params.get('xh')
        print(xhs)
        # ret = pm.XshxBq.objects.filter(xh=xhs, sfyx=1)
        # 20200924 关联表后修改过滤条件,
        # 20200927 添加  是否删除（sfsc=0）   过滤条件
        ret = pm.XtglBqsz.objects.filter(xshxbq__xh=xhs, xshxbq__sfyx=1, sfsc=0)
        return ret

    # 序列化
    serializer_class = serialiser.XshxJstXqSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # 过滤
    # filter_class = filter.XshxJsdXqFilter
    filter_class = filter.HxbqszFilter

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
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"*******************研究生院系下拉院系列表***********"


class YjsYxVIew(mixins.ListModelMixin, generics.GenericAPIView):
    # 查询
    queryset = pm.UibeYjs.objects.filter(yx__isnull=False).values('yx').distinct()
    # 序列化
    serializer_class = serialiser.UibeYjsYxSerializer

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # value=self.request.COOKIES.get("sessionid")
            # print(value)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"*******************研究生年级下拉院系列表***********"


class YjsNjVIew(mixins.ListModelMixin, generics.GenericAPIView):
    # 查询
    queryset = pm.UibeYjs.objects.filter(xn__isnull=False).values('xn').distinct()
    # 序列化
    serializer_class = serialiser.UibeYjsNjSerializer

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            # print(connection.queries[-1:])
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""*******************研究生行为轨迹***********************"""


class YjsXwgjView(mixins.ListModelMixin, generics.GenericAPIView, ):
    # authentication_classes = []
    """分页"""
    pagination_class = Pagination

    def get_queryset(self):
        kssj = self.request.query_params.get("kssj", date.min)
        jssj = self.request.query_params.get("jssj", date.today() + timedelta(days=1))
        # xhxm = self.request.POST.get("xhxm", None)

        xhxm = self.request.query_params.get('xhxm', None)
        print(xhxm)

        myfilter = Q(grgj__create_time__gt=kssj) & Q(grgj__create_time__lte=jssj)

        if not xhxm:
            ret = pm.UibeYjs.objects.annotate(gjcs=Count("grgj", filter=myfilter)).filter(
                gjcs__gte=1)
        else:
            if xhxm.isdigit():
                ret = pm.UibeYjs.objects.filter(grgj__xh__icontains=xhxm).annotate(
                    gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
            else:
                ret = pm.UibeYjs.objects.filter(xm__icontains=xhxm).annotate(
                    gjcs=Count("grgj", filter=myfilter)).filter(
                    gjcs__gte=1)
        return ret

    # 序列化
    serializer_class = serialiser.YjsXwgjSerialiser
    filter_class = filter.YjsFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('xm', 'xh', 'yx', 'xn',)  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def post(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            d = {"kssj": self.request.query_params.get("kssj", date.min),
                 "jssj": self.request.query_params.get("jssj", date.today())}
            return restful.result(message="操作成功", data=ret.data, kwargs=d)
        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


"""*******************研究生行为轨迹个人详情***********************"""


class YjsXwgjXqView(mixins.ListModelMixin, generics.GenericAPIView, ):
    # authentication_classes = []
    """分页"""
    # pagination_class = Pagination

    queryset = wm.YjsXwgjGrgj.objects.all().order_by('-xwsj')
    # 序列化
    serializer_class = serialiser.XwgjYjsMxSerialiser
    filter_class = filter.XwgjYjsMxFilter

    # 搜索，前端通过search关键字传值，？search=''
    # search_fields = ( 'xh', 'yx', '=kssj', '=jssj')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)

            return restful.result(message="操作成功", data=ret.data)

        except Exception as e:
            ip_username(request)
            return restful.result2(message="操作失败", kwargs=logger.error(e.args), data=e.args)


'''************************定时任务************************'''
# from .tasks import test1, test2
#
#
# def post(request):
#     result1 = test1(1, 2)  # 加上delay()表示开启异步执行
#     result2 = test2(2)  # 不开启异步执行，
