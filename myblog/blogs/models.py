from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
