from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    user_id = models.IntegerField(blank=False)
    title = models.CharField
    body = models.TextField

    def __repr__(self):
        return self.id
