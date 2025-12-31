from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Course
from .forms import StudentForm, TeacherForm, CourseForm


# HOME
def home(request):
    return render(request, 'students/home.html')


# ==========================
# STUDENT VIEWS
# ==========================

def student_list(request):
    students = Student.objects.prefetch_related('courses').all().order_by('first_name')
    form = StudentForm()
    return render(request, 'students/student_list.html', {
        'students': students,
        'form': form
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('student_list')


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    return redirect('student_list')


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


# ==========================
# TEACHER VIEWS
# ==========================

def teacher_list(request):
    teachers = Teacher.objects.all().order_by('first_name')
    form = TeacherForm()
    return render(request, 'students/teacher_list.html', {
        'teachers': teachers,
        'form': form
    })


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('teacher_list')


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
    return redirect('teacher_list')


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teacher_list')


# ==========================
# COURSE VIEWS
# ==========================

def course_list(request):
    courses = Course.objects.select_related('teacher').prefetch_related('students')
    form = CourseForm()
    return render(request, 'students/course_list.html', {
        'courses': courses,
        'form': form
    })

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('course_list')


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
    return redirect('course_list')

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')
