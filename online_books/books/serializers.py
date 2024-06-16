from rest_framework import serializers
from .models import *


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name',]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'pages', 'image', 'have']


