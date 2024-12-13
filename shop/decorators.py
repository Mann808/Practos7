from django.shortcuts import redirect
from functools import wraps
from .models import User

def role_required(role_name):
   
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_id = request.session.get('user_id')
            if not user_id:
                return redirect('login')
            user = User.objects.get(id=user_id)
            if user.role.role_name != role_name:
                return redirect('dashboard') 
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
