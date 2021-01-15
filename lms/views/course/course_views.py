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



#dummy model 
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport
from lms.tables import DummyAssignmentTable
from lms.models.dummy_model import DummyAssignment


class GradeBookCourseView(ExportMixin, SingleTableView):
    model = DummyAssignment
    table_class = DummyAssignmentTable
    template_name = 'lms/course/gradebook/course_gradebook.html'



# download csv file (django_tables2 method)
def table_download(request):
    table = DummyAssignmentTable(DummyAssignment.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    return render(request, "lms/course/gradebook/course_gradebook_export.html", {
        "table": table
    })

