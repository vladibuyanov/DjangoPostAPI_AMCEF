from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer


class PostsView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
