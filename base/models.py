from django.db import models
from .choices import TYPE_CHOICES

class Section(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image_1 = models.ImageField(upload_to="images", null=True)
    image_2 = models.ImageField(upload_to="images", blank=True, null=True)
    section_type = models.CharField("Type", max_length=50, choices=TYPE_CHOICES, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    
    