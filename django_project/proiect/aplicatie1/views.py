
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from aplicatie1.models import Location
from django.urls import reverse

# CreateView -> adaugare date in baza de date (instante noi)
# DetailView -> vizualizare date pentru o singura instanta din baza de date
# ListView -> vizualizare date pentru toate instantele din baza de date
# UpdateView -> modificarea datelor dintr-o instanta din baza de date
# DeleteView -> stergerea unei instante din baza de date

class LocationView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'


class CreateLocationView(CreateView):
    model = Location
    fields = ['country', 'city']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


