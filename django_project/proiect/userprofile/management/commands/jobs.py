import requests
from django.core.management import BaseCommand


def jobs():
    url = "https://findwork.dev/api/jobs/?location=London&remote=true"

    payload = {}
    headers = {
        'Authorization': 'Token f7910b6b4fee8499d512a0b0a5b750d6b6b3e1c8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


class Command(BaseCommand):
  help = 'Vizualizare api jobs'

  def handle(self, *args, **options):
    jobs()