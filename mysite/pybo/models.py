from django.db import models

# Create your models here.

from django.db import models

class Qs(models.Model):
    sbj = models.CharField(max_length=200)
    con = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.sbj

class Aw(models.Model):
    qus = models.ForeignKey(Qs, on_delete=models.CASCADE)
    con = models.TextField()
    create_date = models.DateTimeField()