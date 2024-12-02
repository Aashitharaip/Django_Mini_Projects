from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email
    
class Messages(models.Model):
    message= models.TextField()
    code= models.CharField(max_length=10)
    burn=models.BooleanField(default=False)

    def __str__(self):
        return self.code
