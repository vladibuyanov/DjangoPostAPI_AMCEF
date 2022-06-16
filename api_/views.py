from .models import Posts
from .serializers import PostsSerializer
from rest_framework import viewsets


class PostsViews(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

# from rest_framework import generics
# class PostsView(generics.ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
#
#
# class PostsUpdate(generics.UpdateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
#
#
# class PostsCrud(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# from django.forms import model_to_dict
# from rest_framework.response import Response
# from rest_framework.views import APIView
# class PostsView(APIView):
#     def get(self, request):
#         posts = Posts.objects.all().values()
#         return Response({'posts': list(posts)})
#
#     def post(self, request):
#         new_post = Posts.objects.create(
#             id=request.data['id'],
#             user_id=request.data['user_id'],
#             title=request.data['title'],
#             body=request.data['body']
#         )
#         return Response({'answer': model_to_dict(new_post)})
