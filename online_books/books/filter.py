from django_filters.rest_framework import FilterSet
from .models import *


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'published_date': ['gt', 'lt'],
            'author': ['exact'],
            'have': ['exact']
        }