from django.db import models
from user.models import User

# Create your models here.

class Author(models.Model):
  """
  Model representing an author.
  """
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  uri_image = models.CharField(max_length=200)
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Category(models.Model):
  """
  Category model
  """
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name}'

class Book(models.Model):
  """
  Book model
  """
  title = models.CharField(max_length=50)
  image = models.CharField(max_length=200)
  isbn = models.CharField(max_length=13)
  status = models.BooleanField(default=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
 
  def __str__(self):
    return f'{self.title} - {self.isbn} - {self.author.first_name}'
