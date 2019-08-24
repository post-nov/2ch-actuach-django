from django.contrib.postgres.fields import ArrayField
from django.db import models


class Post(models.Model):
    number = models.IntegerField(primary_key=True, unique=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    notions = models.SmallIntegerField(blank=True, null=True)
    is_op = models.BooleanField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    files = ArrayField(models.TextField(blank=True, null=True))
    thumbs = ArrayField(models.TextField(blank=True, null=True))

    class Meta:
        managed = False
        db_table = 'posts'
        constraints = [models.UniqueConstraint(fields=['number', 'link'], name='unique post')]

    def __str__(self):
        return str(self.number)
