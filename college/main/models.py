from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    COURSE_TYPES = [
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
        
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='teachers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
