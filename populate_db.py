
import os
import django
import sys
from datetime import datetime

# Setup Django environment
sys.path.append('c:/Users/gauth/Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Skill, Project
from django.core.files.uploadedfile import SimpleUploadedFile

def populate():
    # Helper to clear existing data to avoid duplicates (optional, use if you want a fresh start)
    # Skill.objects.all().delete()
    # Project.objects.all().delete()

    print("Populating Skills...")
    skills = [
        {"name": "Python", "proficiency": 90},
        {"name": "Django", "proficiency": 85},
        {"name": "JavaScript", "proficiency": 80},
        {"name": "HTML/CSS", "proficiency": 95},
        {"name": "PostgreSQL", "proficiency": 75},
        {"name": "Git", "proficiency": 85},
    ]

    for skill_data in skills:
        skill, created = Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"proficiency": skill_data["proficiency"]}
        )
        if created:
            print(f"Created skill: {skill.name}")
        else:
            print(f"Skill already exists: {skill.name}")

    print("\nPopulating Projects...")
    # Placeholder images would be better if we had them, but we'll leave image field empty or use a placeholder URL 
    # if the model supports it. The model has an ImageField, so we might need a dummy file if we strictly want to fill it.
    # For now, we'll create projects without images or let them use the default behavior if any. 
    
    projects = [
        {
            "title": "Portfolio Website",
            "description": "My personal portfolio website built with Django and Bootstrap. Features a dashboard, project showcase, and contact form.",
            "tech_stack": "Django, Python, Bootstrap, PostgreSQL",
            "github_link": "https://github.com/G20square/portfolio",
            "live_link": "https://gauth-portfolio.com",
        },
        {
            "title": "E-commerce Platform",
            "description": "A full-featured e-commerce platform with cart functionality, payment gateway integration, and user authentication.",
            "tech_stack": "Django REST Framework, React, Stripe API",
            "github_link": "https://github.com/G20square/ecommerce",
            "live_link": "",
        },
        {
            "title": "Task Management App",
            "description": "A productivity app to manage daily tasks and projects. Includes real-time updates and team collaboration features.",
            "tech_stack": "Vue.js, Firebase, Node.js",
            "github_link": "https://github.com/G20square/taskmanager",
            "live_link": "https://taskmanager-app.com",
        }
    ]

    for project_data in projects:
        project, created = Project.objects.get_or_create(
            title=project_data["title"],
            defaults={
                "description": project_data["description"],
                "tech_stack": project_data["tech_stack"],
                "github_link": project_data["github_link"],
                "live_link": project_data["live_link"]
            }
        )
        if created:
            print(f"Created project: {project.title}")
        else:
            print(f"Project already exists: {project.title}")

if __name__ == '__main__':
    populate()
    print("\nDatabase population completed!")
