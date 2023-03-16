from django.db import models
from datetime import date
# Create your models here.


class Commentaire (models.Model):
    titre = models.CharField(max_length=100)
    commentaire = models.TextField(null=True)
    cdate = models.DateField(blank = True, null= True, default=date.today())
