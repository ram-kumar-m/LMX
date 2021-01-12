import random

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lmx.settings")

import django
django.setup()

from lms.models.dummy_model import DummyStudent, DummyAssignment
from django_seed import Seed

seeder = Seed.seeder()

num_per_assignment = 10
mark_base = 100
num_students = 10
num_assignments = 100
max_mark = 1000

seeder.add_entity(DummyStudent, num_students, {
    "email": lambda x:seeder.faker.email(),
    "name": lambda x:seeder.faker.name(),
})
inserted_pks = seeder.execute()

for student in DummyStudent.objects.all():
    for n in range(1, num_per_assignment):
        title = f"Assignment {n}"
        post = {
            "student":student,
            "title": title,
            "max_mark": mark_base*n,
            "alloted_mark": random.randint(0, mark_base*n),
            "grade": random.choice('ABCDEF'),

        }
        as1  = DummyAssignment(**post)
        as1.save()

