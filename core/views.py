from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

class PostApiView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PostListCreateApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






#class PostApiView(APIView):

 #   permission_classes = [IsAuthenticated]

  #  def post(self,request,*args,**kwargs):
   #     serializer = PostSerializer(data=request.data)
    #    if serializer.is_valid():
     #       serializer.save()
      #      return Response(serializer.data)
       # return Response(serializer.errors)

    #def get(self,request,*args,**kwargs):
     #   qs = Post.objects.all()
      #  post = qs.first()
        #serializer = PostSerializer(qs, many=True)
       # serializer = PostSerializer(post)
        #return Response(serializer.data)