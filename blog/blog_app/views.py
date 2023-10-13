from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

