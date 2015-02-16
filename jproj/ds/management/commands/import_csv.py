#https://docs.djangoproject.com/en/1.7/howto/custom-management-commands/

from django.core.management.base import BaseCommand, CommandError
from ds.utils import import_csv


class Command(BaseCommand):
    help = 'Reads csv data from url and stores it to db'

    def handle(self, *args, **options):
		import_csv()
