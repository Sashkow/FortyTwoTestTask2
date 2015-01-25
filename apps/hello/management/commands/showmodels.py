from django.core.management.base import BaseCommand, CommandError
from apps.hello.models import Person

class Command(BaseCommand):
    def handle(self, *args, **options):
        # for poll_id in args:
        try:
            name = 'admin'
            Person = Person.objects.get(user__username=name)
        except Person.DoesNotExist:
            raise CommandError('Person "" does not exist' % name)

        person.name = "Commanded"
        person.save()

        self.stdout.write('Successfully modified "%s"' % name)
        self.stdout.write('"%s" is now commanded: %s %s' % (name, person.name, person.surname))

