from django.contrib import admin
from .models import Teacher, Student, Course


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'email')
    search_fields = ('first_name', 'last_name', 'department')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number', 'program', 'admission_year')
    search_fields = ('first_name', 'last_name', 'roll_number')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'teacher', 'semester', 'academic_year')
    search_fields = ('course_code', 'title')
    filter_horizontal = ('students',)
