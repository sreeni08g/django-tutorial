from django.db import models


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
