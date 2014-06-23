from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from sphinxql import configuration


class Command(BaseCommand):
    help = 'Interacts with search deamon.'
    option_list = BaseCommand.option_list

    def handle(self, **options):
        self.stdout.write('Stopping Sphinx\n')
        self.stdout.write('---------------\n')

        self.stdout.write(configuration.stop())

        self.stdout.write('----\n')
        self.stdout.write('Done\n')
