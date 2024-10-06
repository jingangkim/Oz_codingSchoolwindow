from django.db import models
from common.models import CommonModel
# Create your models here.
class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
    writer = models.CharField(max_length=30)

    def __str__(self):
        return self.title