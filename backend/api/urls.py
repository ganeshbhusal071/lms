from django.urls import path
from .views import (
    BookListCreateAPIView, 
    BookDetailAPIView,
    IssueListCreateAPIView, 
    IssueDetailAPIView,
    BookReturnAPIView )


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('issues/', IssueListCreateAPIView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueDetailAPIView.as_view(), name='issue-detail'),
    path('issues/<int:pk>/return/', BookReturnAPIView.as_view(), name='book-return'),
]