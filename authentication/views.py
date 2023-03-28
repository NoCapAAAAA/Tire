from django.views.generic import FormView, UpdateView, DetailView, TemplateView
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy

from authentication.forms import (LoginForm, RegisterForm, UserEditForm,
                                  CustomPasswordChangeForm)
from profiles.forms import ClientProfileForm
from django.contrib.auth.models import Group


User = get_user_model()


class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = settings.LOGIN_REDIRECT_URL

    def get_success_url(self) -> str:
        users_in_group = Group.objects.get(name="Директор").user_set.all()
        users_in_group2 = Group.objects.get(name="Менеджер").user_set.all()

        if self.request.user in users_in_group:
            return '/staff/director/'
        elif self.request.user in users_in_group2:
            return '/staff/manager/'
        return super().get_success_url()

    def form_valid(self, form):
        user = authenticate(self.request, **form.cleaned_data)
        # if user.is_superuser:
        #     return self.form_invalid(self.get_form())
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/')


class UserEditView(UpdateView):
    template_name = 'authentication/user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('user_edit')

    def get_object(self):
        return self.request.user


class UserDetailView(DetailView):
    template_name = 'authentication/user_detail.html'
    model = User

    def get_object(self):
        return self.request.user


class PasswordChangeView(UpdateView):
    form_class = CustomPasswordChangeForm
    template_name = 'authentication/password.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
