from rest_framework import serializers
from . import models 


class CommentaireSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Commentaire
        fields = ["titre", "commentaire", "cdate"]
       
       
