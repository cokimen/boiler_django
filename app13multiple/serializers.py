from wsgiref.validate import validator
from rest_framework import serializers
from .models import Author, Book


def buat_book(value):
    if value != "coki":
        raise serializers.ValidationError('this field must be coki.')


class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=300)

    class Meta:
        model = Book
        fields = '__all__'
        # list_serializer_class = BookListSerializer
        extra_kwargs = {
            "name": {
                "validators": [buat_book]
            }
        }

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class BookOtSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=300)

    def validate(self, attrs):
        # if attrs.get('desc') != "coki":
        #     raise serializers.ValidationError("salah", code='desc')
        return super().validate(attrs)

    def validate_desc(self, desc):
        if desc != "coki":
            raise serializers.ValidationError("salah")
        return desc

    class Meta:
        extra_kwargs = {
            "name": {
                "validators": [buat_book]
            }
        }

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
