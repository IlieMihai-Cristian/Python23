import requests
from django.core.management import BaseCommand


def API():
  url = "https://v6.exchangerate-api.com/v6/4c7c987629a9daf434ac285c/latest/RON"

  payload = {}
  headers = {
    'Authorization': '4c7c987629a9daf434ac285c'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # print(response.text)
  print(eval(response.text)['conversion_rates'])


class Command(BaseCommand):
  help = 'Vizualizare api conversie'

  def handle(self, *args, **options):
    API()