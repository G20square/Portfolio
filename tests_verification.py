import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from portfolio.models import Project, ContactMessage

def run_verification():
    print("Starting verification...")
    client = Client()

    # 1. Test Register Page (GET)
    print("Testing Register Page...")
    response = client.get(reverse('register'))
    print(f"Register page status: {response.status_code}")
    if response.status_code == 200:
        print("  - Register page accessible")
    else:
        print("  - Register page FAILED")

    # 2. Create User
    username = 'testuser'
    password = 'testpassword'
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, email='test@example.com', password=password)
        print(f"Created user: {username}")
    else:
        print(f"User {username} already exists")

    # 2. Login
    login_success = client.login(username=username, password=password)
    print(f"Login successful: {login_success}")

    # 3. Access Dashboard
    response = client.get(reverse('dashboard'))
    print(f"Dashboard access (authenticated): {response.status_code}")
    if response.status_code == 200:
        print("  - Dashboard accessible")
    else:
        print("  - Dashboard FAILED")

    client.logout()
    response = client.get(reverse('dashboard'))
    print(f"Dashboard access (unauthenticated): {response.status_code}")
    if response.status_code == 302:
        print("  - Dashboard redirected (correct)")
    else:
        print("  - Dashboard FAILED redirection")

    # 4. Contact Form
    print("\nTesting Contact Form...")
    response = client.post(reverse('contact'), {
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message.'
    }, follow=True)
    print(f"Contact form submit status: {response.status_code}")
    if ContactMessage.objects.filter(email='test@example.com').exists():
        print("  - Message saved to DB")
    else:
        print("  - Message NOT saved")

    # 5. API Tests
    print("\nTesting API...")
    # List Projects
    response = client.get(reverse('api-project-list'))
    print(f"API Project List: {response.status_code}")

    # Create Project (Unauthorized)
    response = client.post(reverse('api-project-list'), {'title': 'New Project', 'description': 'Desc'})
    print(f"API Project Create (Unauthorized): {response.status_code}")
    if response.status_code in [401, 403]:
        print("  - Correctly denied")
    else:
        print("  - Incorrectly allowed")

    # Obtain Token
    response = client.post(reverse('api_token_auth'), {'username': username, 'password': password})
    print(f"Token Auth: {response.status_code}")
    if response.status_code == 200:
        token = response.json().get('token')
        print(f"  - Token obtained: {token[:10]}...")
    else:
        print("  - Token failed")

if __name__ == "__main__":
    run_verification()
