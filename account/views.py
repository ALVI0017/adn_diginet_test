from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import SignUpForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'account/sign_up.html'
    success_url = reverse_lazy('sign_in')
    form_class = SignUpForm
    success_message = "Your profile was created successfully"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='account:sign_in')
        return render(request, self.template_name, {'form': form})

    # check if the user is logged in or not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


class SignIn(View):
    template_name = "account/sign_in.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            print(user, "tsst")
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect(to='post:home')
        messages.warning(request, 'Login failed')
        return render(request, self.template_name, context={'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(to='/')
# TO DO sign up view

# TO DO login view
# TO DO logout
# TO DO user profile
# TO DO user update
# TO DO user password
