from django.contrib.auth.views import LoginView
from base.forms.auth_forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    authentication_form = CustomLoginForm
