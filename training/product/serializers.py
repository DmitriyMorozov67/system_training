from rest_framework import serializers
from .models import Product, Student, Lesson, Grooup


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'date_start',
                  'min_students', 'max_students', 'price'
                  ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'name', 'last_name']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'product', 'name', 'video_url']


class GrooupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grooup
        fields = ['name', 'students']