# Core Django imports.
from django.views.generic import ListView

# Blog application imports.
from lms.models.course_model import Course
from lms.models.student_model import Profile
from django.shortcuts import render, Http404, HttpResponse

class CourseListView(ListView):
    model = Course
    context_object_name = "courses"
    template_name = "lms/course/home.html"


def GradeBookHomeView(request):
    context = {'courses':Course.objects.all(),
                'students':Profile.objects.all()}
    return render(request, 'lms/course/gradebook_home.html', context)

def GradeBookCourseView(request):
    context =  {'courses':Course.objects.all(),
                'students':Profile.objects.all()}
    return render(request, 'lms/course/course_gradebook.html', context)

    