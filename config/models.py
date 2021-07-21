from django.db import models

# Create your models here.

"""
from django.db import models

# Create your models here.
CATEGORY = {
    ('DRAMA','Drama'),
    ('ACTION','Action')
}

class Listings(models.Model):
    class Meta:
        verbose_name = "Listings"
        verbose_name_plural = "Listings"
    
    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY, max_length=6)

    def __str__(self):
        return self.name
"""
