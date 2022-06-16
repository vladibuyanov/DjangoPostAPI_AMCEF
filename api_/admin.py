from django.contrib import admin
from .models import Posts


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'body')


admin.site.register(Posts, PostsAdmin)
