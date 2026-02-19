import os
import django
import sys

# Setup Django environment
sys.path.append('c:/Users/gauth/Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Skill, Project

print(f"Skills count: {Skill.objects.count()}")
for skill in Skill.objects.all():
    print(f"  - {skill.name}: {skill.proficiency}")

print(f"Projects count: {Project.objects.count()}")
for project in Project.objects.all():
    print(f"  - {project.title}")
