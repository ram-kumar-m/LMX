import random

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lmx.settings")

import django
django.setup()

from lms.models.dummy_model import DummyStudent, DummyAssignment
from django_seed import Seed



# assert num_students_to_add < number_per_assignment, "Can't have more than one assignment per student"
    

seeder = Seed.seeder()

num_per_assignment = 10
mark_base = 100
num_students = 10



# seeder.add_entity(DummyStudent, num_students, {
#     "email": lambda x:seeder.faker.email(),
#     "name": lambda x:seeder.faker.name(),
# })
# inserted_pks = seeder.execute()
# print(inserted_pks)

for student in range(100):
    for n in range(1, num_per_assignment):
        seeder.add_entity(DummyAssignment, 1, {
            # "student":student,
            "title": f"Assignment {n}",
            "max_mark": mark_base*n,
            "alloted_mark": lambda x: random.randint(0, mark_base*n),
            "grade": lambda x: random.choice('ABCDEF'),

        })
        inserted_pks = seeder.execute()
