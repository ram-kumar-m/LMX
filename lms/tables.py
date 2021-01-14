# lms/tables.py
import django_tables2 as tables
from lms.models.dummy_model import DummyAssignment

class DummyAssignmentTable(tables.Table):
    class Meta:
        model = DummyAssignment
        template_name = "django_tables2/bootstrap4.html"
        