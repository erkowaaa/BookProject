from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filter import BookFilter
from rest_framework.filters import SearchFilter


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers




