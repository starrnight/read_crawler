from django.http import JsonResponse

from common import res_code


class ApiRes:
    """
    接口响应
    """

    @classmethod
    def success(cls, data=None) -> JsonResponse:
        """ api 接口成功响应
        :param data: 数据内容
        :return:
        """
        return cls.response(res_code.SUCCESS, data)

    @classmethod
    def fail(cls, data=None) -> JsonResponse:
        """ api 接口失败响应
        :param data: 数据内容
        :return:
        """
        return cls.response(res_code.SYSTEM_ERROR, data)

    @classmethod
    def page_format(cls, page_size: int, page: int, total: int, items: list) -> dict:
        """ api 分页数据
        :param page_size:
        :param page:
        :param total:
        :param items:
        :return:
        """
        return {
            'page_size': page_size,
            'page': page,
            'total': total,
            'item': items,
        }

    @classmethod
    def response(cls, code, data=None, **kwargs) -> JsonResponse:
        """ 定义接口返回格式
        :param code: 状态描述
        :param data: 数据
        :return: 格式返回
        """
        if data is None:
            data = {}
        if not isinstance(code, tuple):
            code = (code, '')
        return JsonResponse({
            'code': code[0],
            'msg': code[1],
            'data': data,
            **kwargs,
        })
