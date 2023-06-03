from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # json で出力するフィールド
        fields = ("name", "genre", "url")
