from novel.models import Book


class BookService:

    @classmethod
    def create(cls, params):
        """
        创建书
        :param params:
        :return:
        """
        pass

    @classmethod
    def update(cls, params):
        """
        创建书
        :param params:
        :return:
        """
        pass

    @classmethod
    def detail(cls, uuid) -> dict:
        """
        书籍详情
        :param uuid:
        :return:
        """
        return Book.objects.filter(uuid=uuid).first()
