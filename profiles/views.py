from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model

from authentication.forms import UserEditForm


user_model = get_user_model()

@login_required
def profile(request):
    context = {
        'form': UserEditForm()
    }
    return render(request, 'profiles/user_profile.html', context)


class ProfileView(UpdateView):
    template_name = 'profiles/user_profile.html'
    model = user_model
    fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
        'phone_number', 'gender')