from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Book.objects.all()
    # シリアライザーを取得
    serializer_class = BookSerializer
