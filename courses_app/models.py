from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}

        if len(postData['name']) < 6:
            errors["name"] = "Course name should be at least 5 characters"
        if len(postData['description']) < 16:
            errors["description"] = "Course description should be at least 15 characters"
        return errors

class Course(models.Model):
    name= models.CharField(max_length = 255)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = CourseManager()

# Create your models here.