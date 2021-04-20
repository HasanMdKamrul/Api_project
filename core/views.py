from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post


from rest_framework.views import APIView
from rest_framework.response import Response


class PostApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        post = qs.first()
        #serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)