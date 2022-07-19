#Django rest framework serializers
from rest_framework import serializers

# models
from .models import Book, Author, Category
from user.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Book
        #exclude = ('id',)
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'image': instance.image,
            'isbn': instance.isbn,
            'author': {
                'id': instance.author.id,
                'first_name': instance.author.first_name,
                'last_name': instance.author.last_name,
                'uri_image': instance.author.uri_image,
            },
            'category': {
                'id': instance.category.id,
                'name': instance.category.name,
                'description': instance.category.description,
            },
        }








#metodo para mostrar datos de la relacion entre tablas
    #category = CategorySerializer()
    #author = AuthorSerializer()
    #metodo 2
    """
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='first_name'
    )
    """