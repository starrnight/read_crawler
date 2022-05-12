from rest_framework.serializers import ModelSerializer

from novel.models import Book


class BookCreateSerializer(ModelSerializer):
    """
    新增书籍
    """

    class Meta:
        model = Book
        fields = ['name', 'author', 'intro', 'words_num', 'chapter_latest']
