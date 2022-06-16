from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __repr__(self):
        return self.title
