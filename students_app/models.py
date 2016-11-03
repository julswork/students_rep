from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    # card_number = models.
    # group = models.CharField(max_length=15)
    # group = FK group
    # photo

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name


class Group(models.Model):
    title = models.CharField(max_length=15)
    # head = FK student

