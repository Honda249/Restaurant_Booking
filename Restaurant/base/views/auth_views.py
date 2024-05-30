from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from base.forms.auth_forms import CustomLoginForm , SignUpForm
from django.contrib.auth import login, authenticate

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'base/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True
