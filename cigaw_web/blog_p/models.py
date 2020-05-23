from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
