from django.db import models


class HashTag(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Participate(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Member(models.Model):
    school = models.CharField(max_length=100, null=True)
    name = models.CharField(primary_key=True, max_length=10)
    introduce = models.CharField(null=True, max_length=1000)
    team = models.IntegerField(null=True)
    participate = models.ManyToManyField(Participate, blank=True)
    interest = models.ManyToManyField(Interest, blank=True)
    hashtag = models.ManyToManyField(HashTag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['team']