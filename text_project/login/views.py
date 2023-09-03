from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm , PasswordChangingForm , PasswordResettingForm , UserPasswordSetForm , LoginForm
from django.contrib.auth.views import PasswordChangeView , PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import login, authenticate , logout
from django.views import View
from django_ratelimit.decorators import ratelimit



class LoginView(View):
    form_class = LoginForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('action')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                form.add_error(None, 'Invalid username or password. Please try again')
        return render(request, self.template_name, {'form': form})

@ratelimit(key='ip', rate='5/h', method='ALL', block=True)
def UserRegistration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('login'))  # Redirect to the login page on successful registration
    else:
        form = SignUpForm()

    return render(request, 'login/registration.html', {'form': form})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'login/change_password.html'
    success_url = reverse_lazy('login')

class PasswordsResetView(PasswordResetView):
    form_class = PasswordResettingForm
    template_name = 'login/reset_password.html'
    success_url = reverse_lazy('login')

class PasswordsConfirmResetView(PasswordResetConfirmView):
    form_class = UserPasswordSetForm
    template_name = 'login/set_password.html'
    success_url = reverse_lazy('login')

def LogoutView(request):
    logout(request)
    return redirect('login')
     