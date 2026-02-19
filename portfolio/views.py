from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from .models import Project, Skill, ContactMessage
from .forms import UserRegistrationForm

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    
    from django.contrib.auth.models import User
    
    # improved logic to get the main user's profile
    # For now, just getting the first superuser or the first user
    user = User.objects.filter(is_superuser=True).first()
    if not user:
        user = User.objects.first()
    
    profile = user.profile if user and hasattr(user, 'profile') else None

    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills,
        'profile': profile
    })

from django.core.mail import send_mail
from django.conf import settings

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save to DB
            contact = ContactMessage.objects.create(name=name, email=email, message=message)
            
            # Send Email to Admin
            subject_admin = f"New Contact Message from {name}"
            message_admin = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            from django.core.mail import EmailMessage
            email_admin = EmailMessage(
                subject_admin,
                message_admin,
                settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'noreply@example.com',
                ['gauthamg250204@gmail.com'],
                reply_to=[email],
            )
            email_admin.send(fail_silently=True)
            
            # Send Confirmation to User
            subject_user = "Message Received - Gautham's Portfolio"
            message_user = f"Hi {name},\n\nThank you for reaching out. I have received your message and will get back to you shortly.\n\nBest regards,\nGautham"
            send_mail(
                subject_user,
                message_user,
                settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'noreply@example.com',
                [email],
                fail_silently=True,
            )

            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')
            
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from .forms import ProjectForm, ProfileForm, SkillForm
from django.shortcuts import get_object_or_404

@login_required
def dashboard(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    # Assuming one profile for now, linked to the user
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
        
    return render(request, 'dashboard.html', {
        'projects': projects,
        'skills': skills,
        'profile': profile
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Project'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Project'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('dashboard')
    return render(request, 'portfolio/confirm_delete.html', {'item': project.title})

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Create profile if it doesn't exist
        profile = Profile.objects.create(user=request.user)
        
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Profile'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Skill'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('dashboard')
    return render(request, 'portfolio/confirm_delete.html', {'item': skill.name})
