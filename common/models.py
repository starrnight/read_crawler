import time
import uuid

from django.db import models
from django.db.models.base import ModelBase

from common.utils import StringUtil


class CustomTimeField(models.BigIntegerField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        if not value:
            return None
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))


class CustomChoicesField(models.SmallIntegerField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        if not self.choices:
            return value
        if value is not None:
            for row in self.choices:
                if value == row[0]:
                    return row[1]
        return None

    def get_prep_value(self, value):
        if not self.choices or isinstance(value, int):
            return value
        if value is not None:
            for row in self.choices:
                if value == row[1]:
                    return row[0]
        return None


class ModelCustomName(ModelBase):
    """ 规则生成表名 """
    def __new__(mcs, name, bases, attrs, **kwargs):
        table_name = f't_{StringUtil.camelize_to_underline(name)}'
        if not attrs.get('Meta', None):
            attrs['Meta'] = type("Meta", (), dict(db_table=table_name))
        abstract = getattr(attrs["Meta"], 'abstract', False)
        if not hasattr(attrs["Meta"], 'db_table') and not abstract:
            setattr(attrs['Meta'], 'db_table', table_name)

        return super().__new__(mcs, name, bases, attrs, **kwargs)


class BaseModel(models.Model, metaclass=ModelCustomName):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")

    create_time = models.DateTimeField(verbose_name="创建时间", default=time.time())
    update_time = models.DateTimeField(verbose_name="更新时间")

    objects = models.Manager()

    class Meta:
        abstract = True
