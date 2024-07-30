from django.db import models

class MaterialDetail(models.Model):
    SQF_CHOICES = [
        ('80', 'SQF 80'),
        ('100', 'SQF 100'),
        ('120', 'SQF 120'),
    ]

    specification = models.CharField(max_length=255)
    quantity = models.IntegerField()
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    sqf_type = models.CharField(max_length=3, choices=SQF_CHOICES)
    
     # New field for heading
    is_heading = models.BooleanField(default=False)

    def __str__(self):
        return self.specification
