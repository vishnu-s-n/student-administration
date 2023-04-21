from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student


def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})