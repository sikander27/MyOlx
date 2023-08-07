from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # Add other user-related fields as needed


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    # Add other category-related fields as needed

    def __str__(self):
        return self.category_name

class Option(models.Model):
    option_name = models.CharField(max_length=100)
    # Add other option-related fields as needed

    def __str__(self):
        return self.option_name

class Category_Option(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.option}"

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other ad-related fields as needed

    def __str__(self):
        return self.title

class Ad_Option(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    # Add other ad-option related fields as needed

    def __str__(self):
        return f"{self.ad} - {self.option} - {self.value}"
