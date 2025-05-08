from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):  # Renamed to fix spelling
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('BL', 'Black Tea'),
        ('LI', 'Lemon Tea'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chai/')
    date_added = models.DateField(default=timezone.now)
    type = models.CharField(choices=CHAI_TYPE_CHOICE, max_length=50)

    def __str__(self):
        return self.name
