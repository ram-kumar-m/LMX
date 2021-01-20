# Core Django imports.
from django.views.generic import ListView
from django_filters import filterset

# Blog application imports.
from lms.models.course_model import Course
from lms.models.student_model import Profile
from django.shortcuts import render, Http404, HttpResponse

from django_filters import filterset
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class CourseListView(ListView):
    model = Course
    context_object_name = "courses"
    template_name = "lms/course/home.html"



#dummy model 
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.export.views import ExportMixin

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from lms.tables import DummyAssignmentTable, DummyAssignmentFilter
from lms.models.dummy_model import DummyAssignment
class GradeBookCourseView(ExportMixin, SingleTableMixin, FilterView):
    model = DummyAssignment
    table_class = DummyAssignmentTable
    
    template_name = 'lms\course\gradebook\course_gradebook.html'
    filterset_class  = DummyAssignmentFilter
