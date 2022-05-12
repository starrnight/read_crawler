from rest_framework import serializers


class NoModelSerializer(serializers.Serializer):
    """
    无数据模型操作基类
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class BaseApiResp(NoModelSerializer):
    """
    响应基类
    """
    code = serializers.CharField(help_text="响应码")
    msg = serializers.CharField(help_text="响应信息")
    data = serializers.JSONField(help_text="响应数据")


class BasePageResp(NoModelSerializer):
    """
    分页响应类
    """
    page = serializers.IntegerField(min_value=1, help_text="页码")
    page_size = serializers.IntegerField(min_value=1, help_text="每页大小")
    total = serializers.IntegerField(min_value=0, help_text="总条数")
    items = serializers.JSONField(help_text="分页数据")


class BasePageReq(NoModelSerializer):
    """
    分页请求类
    """
    page = serializers.IntegerField(required=False, default=1, min_value=1, help_text="页码")
    page_size = serializers.IntegerField(required=False, default=10, min_value=1, help_text="每页大小")
