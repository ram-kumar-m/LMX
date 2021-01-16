# lms/tables.py
import django_tables2 as tables
from lms.models.dummy_model import DummyAssignment

class DummyAssignmentTable(tables.Table):
    class Meta:
        model = DummyAssignment
        template_name = "django_tables2/bootstrap4.html"
        fields = ('student__name', 'title', 'grade', 'alloted_mark', 'max_mark', 'student__email',)

import django_filters

class DummyAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = DummyAssignment
        fields = ['student__name', 'student__email', 'title']