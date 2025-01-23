from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'header', 'author', 'publication_year', 'genre']

    def validate_header(self, value):
        if not value:
            raise serializers.ValidationError('Header is required.')
        return value

    def validate_author(self, value):
        if not value:
            raise serializers.ValidationError('Author is required.')
        return value