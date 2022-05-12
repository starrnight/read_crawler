from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from common.response import ApiRes
from common.serializer import BaseApiResp
from crawler.crawler import Crawler
from novel.service import BookService


class BookView(APIView):
    @swagger_auto_schema(operation_summary="书籍信息", responses={HTTP_200_OK: BaseApiResp()})
    def get(self, request, uuid):
        print(uuid)
        return ApiRes.success(BookService.detail(uuid))


class BooksView(APIView):
    @swagger_auto_schema(operation_summary="书籍集合", responses={HTTP_200_OK: BaseApiResp()})
    def get(self, request):
        obj = Crawler()
        obj.start()
        return ApiRes.success()
