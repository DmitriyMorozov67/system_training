from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StudentViewSet, LessonViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]