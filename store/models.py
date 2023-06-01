from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
      return self.name


class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='static/products/', null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.name