from django.shortcuts import redirect
from .models import Member

def login_required(func):
    def wrapper(request, *args, **kwargs):
        login_session = request.session.get('login_session', '')

        if login_session == '':
            return redirect('/account/login/')

        return func(request, *args, **kwargs)
    return wrapper