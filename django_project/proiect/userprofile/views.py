from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from userprofile.forms import NewAccountForm


class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/locations_form.html'
    form_class = NewAccountForm