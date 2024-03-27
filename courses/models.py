from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    image= models.CharField(max_length=500)
    summary = models.CharField(max_length=200)
    youtubeUrl = models.CharField(max_length=800)

    def __str__(self):
        return self.summary


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
