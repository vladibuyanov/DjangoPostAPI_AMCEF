from rest_framework.exceptions import ValidationError, NotFound

from .models import Posts
from .serializers import PostsSerializer
from rest_framework import viewsets
import requests

BASE = 'https://jsonplaceholder.typicode.com/'


class PostsViews(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            if not Posts.objects.filter(pk=pk):
                posts_res = requests.get(f'{BASE}posts/{pk}').json()
                if posts_res:
                    new_post = Posts.objects.create(
                        id=pk,
                        user_id=posts_res['userId'],
                        title=posts_res['title'],
                        body=posts_res['body']
                    )
                    new_post.save()
                    return Posts.objects.filter(pk=pk)
                return NotFound('Post not exist')
            return Posts.objects.filter(pk=pk)
        return Posts.objects.all()

    def perform_create(self, serializer):
        json_api = requests.get(f'{BASE}users').json()
        user_id_list = [i['id'] for i in json_api]
        if serializer.validated_data['user_id'] in user_id_list:
            serializer.save()
        raise ValidationError('User not exist')
