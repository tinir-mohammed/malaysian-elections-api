from django.db import models

# Create your models here.
class ElectionResult(models.Model):
    seatID = models.CharField(max_length=10)
    candidName = models.CharField(max_length=60)
    percentWin = models.CharField(max_length=60)
    status = models.CharField(max_length=3)

    def __str__(self):
        return self.seatID