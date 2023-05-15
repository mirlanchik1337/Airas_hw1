from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
