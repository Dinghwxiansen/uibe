# encoding: utf-8
from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    error = 201
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500


# {"code":400,"message":"","data":{}}
def result(code=HttpCode.ok, message="", data=None, kwargs=None):
    json_dict = {"code": code, "message": message, "data": data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


def result2(code=HttpCode.error, message="", data=None, kwargs=None):
    json_dict = {"code": code, "message": message, "data": data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


def ok():
    return result(message="操作成功")


def error():
    return result(message="操作失败")


def params_error_400(message="", data=None):
    return result(code=HttpCode.paramserror, message=message, data=data)


def unauth_401(message="", data=None):
    return result(code=HttpCode.unauth, message=message, data=data)


def method_error_405(message='', data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


def server_error_500(message='', data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
