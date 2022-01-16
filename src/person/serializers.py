from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['id']
        model = Book
        fields = [
            'name',
            'author',
            'date_of_publication',
            'publishing_company'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    
    books = BookSerializer(many=True, read_only=True)

    # Validation directly
    def validate(self, data):
        if data['name'] == "teste":
            raise serializers.ValidationError("O nome do autor nao pode ser teste")
        return data

    # Validation by validator method
    def born_now(value):
        if value > 2022:
            raise serializers.ValidationError("O ano de nascimento não pode ser maior que o ano atual")

    #Declaring Fields (Validations) - Using validator born_now
    born = serializers.CharField(validators=[born_now])
    
    #Specifying fields - Getting methods from .models
    d_sum = serializers.CharField(source='get_sum_born_died', read_only=True)

    class Meta:
        ordering = ['-id']
        model = Author
        fields = [
            'name',
            'years',
            'born',
            'died',
            'update',
            'description',
            'books',
            'd_sum',
        ]