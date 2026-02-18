from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    
    # Handle Contact Form POST in the same view if desired, or separate view
    # Here we use a separate view for clarity, but home handles GET
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills
    })

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')
            
    return redirect('home')
