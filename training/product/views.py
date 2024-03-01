
from django.db.models import Count
from rest_framework import viewsets
from .models import Product, Student, Lesson, Grooup
from .serializers import ProductSerializer, StudentSerializer, LessonSerializer, GrooupSerializer


def has_product_access(user, product):
    try:
        student = Student.objects.get(user=user)
        if student.grooup.filter(product=product).exists():
            return True
    except Student.DoesNotExist:
        pass
    return False


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(student__user=user)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Grooup.objects.all()
    serializer_class = GrooupSerializer


def distribute_students(product):
    students = Student.objects.filter(grooup__isnull=True)
    groups = product.grooup_set.annotate(student_count=Count('students')).order_by('student_count')

    for student in students:

        group = groups.first()

        if group.students.count() < product.max_students:
            group.students.add(student)
        else:

            new_group = Grooup.objects.create(product=product, name=f'Group {groups.count() + 1}')
            new_group.students.add(student)
            groups = groups.annotate(student_count=Count('students')).order_by('student_count')

    return groups
