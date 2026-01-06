from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
        
class IssuedBook(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    issue_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"        
    
    