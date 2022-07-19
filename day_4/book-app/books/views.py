#from django.shortcuts import render
#from django.http import HttpResponse

# Django rest framework
from rest_framework.views import Response
from rest_framework import viewsets

#models
from .models import Book, Author, Category

#serializers
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer














"""
def index(request):
    books = Book.objects.all()
    for book in books:
        print(book.title, book.author.first_name, book.category.name)
    
    return render(request, 'books/index.html',{
      "books_list": books
    })
    #return HttpResponse("app book")

def author(request, author_id):
    if request.method == "GET":
        author = Author.objects.get(id=author_id)
        return render(request, 'books/author.html',{
          "author": author
        })
    elif request.method == "POST":
        return HttpResponse(f'<h1>Author id: {author_id}</h1>')
    author = Author.objects.get(id=author_id)
    print(author.first_name, author.last_name)
    return render(request, 'books/author.html', {
        "author": author
    })
    # return HttpResponse(f'<h1>Author id: {author_id}</h1>')

def category(request, category_id):
    return HttpResponse(f'<h1>Category id: {category_id}</h1>')
"""