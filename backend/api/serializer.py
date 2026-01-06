from .models import Book, IssuedBook
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class IssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedBook
        fields = '__all__'