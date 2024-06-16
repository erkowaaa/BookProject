from django.urls import path
from .views import BookViewSets, AuthorViewSets

urlpatterns = [
    path('', BookViewSets.as_view({'get': 'list', 'post': 'create'}), name='book_list'),
    path('<int:pk>/', AuthorViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='book_detail'),
    path('author/', AuthorViewSets.as_view({'get': 'list', 'post': 'create'}), name='author_list'),
    path('author/<int:pk>/', BookViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='author_detail')
]