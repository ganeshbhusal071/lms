from rest_framework import generics, status,serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import BookSerializer, IssuedSerializer
from .models import Book, IssuedBook
from datetime import date

# Books - List and Create
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Books - Retrieve, Update, Delete (needs pk in URL)
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Issued Books - List and Create
class IssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedSerializer
    
    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        try:
            book = Book.objects.get(id=book_id)
            if book.quantity <= 0:
                raise serializers.ValidationError({"error": "Book not available"})
            book.quantity -= 1
            book.save()
            serializer.save()
        except Book.DoesNotExist:
            raise serializers.ValidationError({"error": "Book does not exist"})

# Issued Books - Retrieve, Update, Delete (needs pk in URL)
class IssueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedSerializer

# Book Return - Custom logic
class BookReturnAPIView(APIView):
    def patch(self, request, pk):
        try:
            issued_book = IssuedBook.objects.get(pk=pk)
        except IssuedBook.DoesNotExist:
            return Response({"error": "Issued book record not found"}, 
                          status=status.HTTP_404_NOT_FOUND)
        
        if issued_book.return_date is not None:
            return Response({"error": "Book has already been returned"}, 
                          status=status.HTTP_400_BAD_REQUEST)
    
        issued_book.return_date = date.today()
        issued_book.save()
        
        book = issued_book.book
        book.quantity += 1
        book.save()
        
        serializer = IssuedSerializer(issued_book)
        return Response({
            "message": "Book returned successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)