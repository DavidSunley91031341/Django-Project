from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=100, default='name')
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=100, default='phone')
    product = models.CharField(max_length=100, default='product')
    message = models.TextField(null=True, default='message', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
