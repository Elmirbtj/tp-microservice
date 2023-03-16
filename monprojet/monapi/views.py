from django.shortcuts import render
from . import models
from .serializer import CommentaireSerializer
from rest_framework.views import APIView
from .models import Commentaire
from rest_framework import status ,permissions
from rest_framework.response import Response




# Create your views here.
class CommentlistAPIView(APIView):

    def get(self,request,*args,**kwargs):
        clist= Commentaire.objects.all()
        serializer = CommentaireSerializer(clist,many=True)
        return Response(serializer.data,status =status.HTTP_200_OK)
        
    def post(self,request,*args,**kwargs):
        data ={'titre':request.data.get('titre') ,'commentaire':request.data.get('commentaire'),'cdate':request.data.get('cdate')}
        serializer = CommentaireSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'res':'error'},status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):

    def get(self,request,id,*args,**kwargs):
        comment= Commentaire.objects.get(id=id)
        if comment is None:
            return Response ({"res":"object not found"},status=status.HTTP_400_BAD_REQUEST)
    
        serializer = CommentaireSerializer(comment)
        
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def delete(self,request,id):
        comment = Commentaire.object.get(id=id)
        if comment is None :
            return Response ({"res":"not found"},status=status.HTTP_404_not_Found)
        comment.delete()
        return Response({"res":"object deleted"},status=status.HTTP_200_OK)
        
   