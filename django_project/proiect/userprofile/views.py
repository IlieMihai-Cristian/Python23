import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView
from userprofile.forms import NewAccountForm


class CreateNewAccount(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/locations_form.html'
    form_class = NewAccountForm
    permission_required = 'auth.add_user'

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase +
                                                   string.digits + '!@$#%&*') for _ in range(8))
        if User.objects.filter(id=self.object.id).exists():
            user_instance = User.objects.get(id=self.object.id)
        # if (user_instance := User.objects.get(id=self.object.id)) and user_instance.exists():
        #     user_object = user_instance.first()
            user_instance.set_password(psw)
            user_instance.save()
            content = f'Datele dumneavoastra de autentificare sunt: \n {user_instance.username} \n {psw}'
            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Date conectare in aplicatie', body=content,
                                           from_email='content@test.ro', to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('locations:lista_locatii')

    # def form_valid(self, form):
    #     if form.is_valid():

# georgeadi
#  usernou1