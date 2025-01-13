import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie1.models import Location, Pontaj
from django.urls import reverse

# CreateView -> adaugare date in baza de date (instante noi)
# DetailView -> vizualizare date pentru o singura instanta din baza de date
# ListView -> vizualizare date pentru toate instantele din baza de date
# UpdateView -> modificarea datelor dintr-o instanta din baza de date
# DeleteView -> stergerea unei instante din baza de date

class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'
    # permission_required = 'location.view_location'

    # def get_queryset(self):
    #     return Location.objects.filter(active=True)

    # def get_context_data(self, **kwargs):
    #     context = super(LocationView, self).get_context_data(**kwargs)
    #     context['ionel'] = [12, 25]
    #     return context


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['country', 'city']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['country', 'city']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


@login_required
# @permission_required
def delete_location(request, pk):
    # SQL native: SELECT country, city FROM aplicatie1_locations WHERE id=1
    # Django quwey: Location.objects.get(id=1).country
    # 1. cu get:
    # instance_object = Location.objects.get(id=pk)
    # if instance_object.active is True:
    #     instance_object.active = False
    #     instance_object.save()

    # 2. cu filter:
    Location.objects.filter(id=pk).update(active=False)

    return redirect('locations:lista_locatii')


@login_required
def restore_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect('locations:lista_locatii')


@login_required
def start_timesheet(request):
    # Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    new_instance = Pontaj()
    new_instance.user_id = request.user.id
    # new_instance.user = User.objects.get(id=request.user.id)
    new_instance.start_date = datetime.datetime.now()
    new_instance.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))