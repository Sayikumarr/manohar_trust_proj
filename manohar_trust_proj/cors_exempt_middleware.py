from django.core.exceptions import DisallowedHost

class BypassAllowedHostsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Bypass ALLOWED_HOSTS check for specific paths
        bypass_paths = ['/saisync/token/', '/saisync/protected/','/saisync/appointments/','/saisync/contacts/']
        
        if any(request.path.startswith(path) for path in bypass_paths):
            # Temporarily set ALLOWED_HOSTS check to bypass
            request.get_host = lambda: 'localhost'

        # Call the next middleware/view
        return self.get_response(request)
