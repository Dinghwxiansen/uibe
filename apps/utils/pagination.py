from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

"""
自定义分页
"""

"""分页，看第N页，每页显示N条数据"""


class Pagination(PageNumberPagination):
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


"""分页二，在n个文职，向后查看n条数据"""


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 5


"""加密分页，上一页和下一页，最大值和最小值"""


class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 2
    ordering = 'id'

    page_size_query_param = None

    max_page_size = 5
