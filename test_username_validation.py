import os
import django
from django.core.exceptions import ValidationError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def test_username(username):
    user = User(username=username, email='test@example.com')
    try:
        user.full_clean()
        print(f"Username '{username}' is VALID")
    except ValidationError as e:
        print(f"Username '{username}' is INVALID: {e.message_dict.get('username')}")

if __name__ == '__main__':
    test_username("valid_user")
    test_username("User Name With Spaces")
    test_username("User@Name!")
