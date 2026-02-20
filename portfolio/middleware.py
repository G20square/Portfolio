from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse, NoReverseMatch

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            
            # Paths that are always allowed
            exempt_prefixes = [
                '/admin/',
                settings.STATIC_URL,
            ]
            
            if settings.MEDIA_URL:
                exempt_prefixes.append(settings.MEDIA_URL)

            # Add named URLs to allow
            try:
                exempt_prefixes.append(reverse('login'))
                exempt_prefixes.append(reverse('register'))
                # Also allow password reset urls if they existed, but for now just these
            except NoReverseMatch:
                pass
            
            # Check if current path starts with any allowed prefix
            if not any(path.startswith(prefix) for prefix in exempt_prefixes):
                return redirect(settings.LOGIN_URL)

        return self.get_response(request)
