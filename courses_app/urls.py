from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addCourse', views.addCourse, name= 'addCourse'),
    path('courses/delete/<int:courseId>', views.deleteCourse, name= 'deleteCourse'),
]