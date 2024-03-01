from django.contrib import admin
from .models import Product, Student, Lesson, Grooup


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'date_start',
              'price', 'min_students', 'max_students',
              ]
    list_display = ['pk', 'name', 'owner', 'min_students', 'max_students']
    ordering = ['pk']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['user', 'name']
    list_display = ['pk', 'user',  'name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ['product', 'name', 'video_url']
    list_display = ['pk', 'name']


@admin.register(Grooup)
class GrooupAdmin(admin.ModelAdmin):
    fields = ['name', 'product', 'students']
    list_display = ['pk', 'product', 'name']