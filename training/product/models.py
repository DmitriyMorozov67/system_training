from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_start = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    min_students = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.name


class Grooup(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='grooup')

    def __str__(self):
        return self.name