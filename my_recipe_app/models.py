# from  import search
from django.db import models

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=10)
  picture = models.ImageField(upload_to='images/')
  description = models.TextField()
  app_label = models.TextField()
  created_at = models.DateTimeField(auto_now_add= True)
