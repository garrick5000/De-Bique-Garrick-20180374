from django.db import models

class Level(models.Model):
    GOALS_INITIATIVES = 'GI'
    PRODUCTS_SERVICES = 'PS'
    DATA_INFORMATION = 'DI'
    SYSTEMS_APPLICATION = 'SA'
    NETWORKS_INFRASTRUCTURE = 'NI'
    LEVEL_CHOICES = [
        (GOALS_INITIATIVES, 'Goals and Initiatives'),
        (PRODUCTS_SERVICES, 'Products and Services'),
        (DATA_INFORMATION, 'Data and Information'),
        (SYSTEMS_APPLICATION, 'Systems and Application'),
        (NETWORKS_INFRASTRUCTURE, 'Networks and Infrastructure')
    ]
    
    name = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=DATA_INFORMATION)

    def __str__(self):
        return self.name


class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=Level.DATA_INFORMATION)
    
    def __str__(self):
        return self.name
