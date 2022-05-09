from datetime import datetime
from django.db import models

# Create your models here.
class Board(models.Model):
    b_no = models.IntegerField(default=0,primary_key=True)
    member = models.CharField(max_length=1000)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    b_group = models.IntegerField(default=0)
    b_step = models.IntegerField(default=0)
    b_indent = models.IntegerField(default=0)
    b_hit = models.IntegerField(default=1)
    b_img = models.ImageField(blank=True)

    
    
