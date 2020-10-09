from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    completed = models.BooleanField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title[:50]


    def get_absolute_url(self):
        return reverse('work_detail', args=[str(self.pk)])

