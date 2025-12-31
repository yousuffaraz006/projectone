from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    date_of_birth = models.DateField(null=True, blank=True)
    program = models.CharField(max_length=100, null=True, blank=True)
    admission_year = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=150)

    description = models.TextField(blank=True)
    credits = models.PositiveSmallIntegerField(null=True, blank=True)

    semester = models.CharField(max_length=20, null=True, blank=True)
    academic_year = models.CharField(max_length=20, null=True, blank=True)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name='courses',
        null=True,
        blank=True
    )

    students = models.ManyToManyField(
        Student,
        related_name='courses',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_code} - {self.title}"
