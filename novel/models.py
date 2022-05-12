from django.db import models

from common.models import BaseModel


class Book(BaseModel):
    name = models.CharField(max_length=64, verbose_name="书籍名称")
    author = models.CharField(max_length=64, verbose_name="作者")
    intro = models.CharField(max_length=512, blank=True, verbose_name="简介")
    words_num = models.IntegerField(null=True, verbose_name="字数")
    chapter_latest = models.UUIDField(null=True, verbose_name="最新章节")


class Chapter(BaseModel):
    chapter_no = models.IntegerField(null=True, verbose_name="章节编号")
    name = models.CharField(max_length=64, verbose_name="章节名称")
    content = models.TextField(null=True, verbose_name="章节内容")
    words_num = models.IntegerField(null=True, verbose_name="字数")
