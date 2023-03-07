from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=300)
    news_details = models.TextField()
    # cover_image = models.ImageField(upload_to='images')
    cover_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title
    