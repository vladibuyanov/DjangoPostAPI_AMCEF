from rest_framework import viewsets, permissions
from .models import Posts
from .serializers import PostsSerializer


class PostsViews(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostsSerializer
