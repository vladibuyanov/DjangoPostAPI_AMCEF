from rest_framework import routers
from .api import PostsViews

routers = routers.DefaultRouter()
routers.register('api/posts', PostsViews, 'posts')

urlpatterns = routers.urls
