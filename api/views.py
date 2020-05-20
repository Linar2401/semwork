from tokenize import Token

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import *

from api.permitions import MyCommentPermissions
from books.models import Comment
from books.serializers import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    permission_classes = [MyCommentPermissions]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

