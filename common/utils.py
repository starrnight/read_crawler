"""
工具模块
"""
import datetime
import random
import string
import time
from ipaddress import ip_network

from common import constant


class IpUtil:
    """ ip工具类
    """

    @classmethod
    def ip_int2str(cls, ip: int) -> str:
        """ int to str
        :param ip: ip int值
        :return: ip str值
        """
        return '.'.join([str(ip >> (i * 8) & 0x000000ff) for i in range(3, -1, -1)])

    @classmethod
    def ip_str2int(cls, ip: str) -> int:
        """ str to int
        :param ip: ip str值
        :return: ip int值
        """
        return sum([int(v) << ((3 - i) * 8) for i, v in enumerate(ip.split('.'))])

    @classmethod
    def get_cidr_list(cls, cidr):
        """
        获取cidr的范围列表
        @param cidr:
        @return:
        """
        try:
            net = ip_network(cidr, strict=False)
        except ValueError as e:
            raise e
        else:
            return [int(net.network_address) + 1, int(net.broadcast_address)]


class StringUtil:
    """ 字符串工具类
    """

    @classmethod
    def camelize_to_underline(cls, text: str) -> str:
        """ 驼峰转下划线
        :param text:
        :return:
        """
        lst = []
        for index, char in enumerate(text):
            if char.isupper() and index != 0:
                lst.append('_')
            lst.append(char)

        return ''.join(lst).lower()

    @classmethod
    def underline_to_hump(cls, text):
        """
        下划线转驼峰
        @param text:
        @return:
        """
        return ''.join([x.capitalize() for x in text.split('_')])

    @classmethod
    def str_center(cls, value: str, add_len: int = 2, fill: str = '%') -> str:
        """ 字符串两边填充字符
        :param value: 源字符串
        :param add_len: 增加的长度
        :param fill: 填充的字符
        :return:
        """
        return value.center(len(value) + add_len, fill)

    @classmethod
    def generate_random_str(cls, length: int = 10):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        :param length:
        :return:
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
        return ''.join(str_list)


class DateTimeUtil:
    """ 时间工具类
    """

    @classmethod
    def to_str_cn(cls, obj) -> str:
        """ 时间对象转字符串
        :param obj: 时间对象
        :return: 时间字符串
        """
        if isinstance(obj, datetime.datetime):
            return obj.strftime(constant.DATETIME_FORMAT)
        raise TypeError

    @classmethod
    def get_yesterday(cls):
        """
        获取昨天的日期
        @return:
        """
        yesterday = datetime.date.today() + datetime.timedelta(-1)
        return yesterday

    @classmethod
    def timestamp_to_string(cls, timestamp) -> str:
        """
        时间戳转字符串
        @param timestamp:
        @return:
        """
        return time.strftime(constant.DATETIME_FORMAT, time.localtime(timestamp))
