# from django.test import TestCase

# from django.core.urlresolvers import reverse
# # from django.test import Client
# from django.test.client import RequestFactory

# from apps.hello.models import Person
# from django.contrib.auth.models import User

# from apps.hello.admin import PersonForm

# from django.conf import settings
# from django.conf.urls.static import static

# from apps.hello.utils import get_person_or_admin

# class PersonFormTestCase(TestCase):
#     """
#     test PersonForm modelform from admin.py
#     """
#     fixtures = ['test_data.json']

#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_form_gets_values_from_instance_user_on_init(self):
#         """
#         test that, given instance, form retreives name, surname, email
#         values from instance.user and sets initial values of corresponding
#         fields on __init__ form
#         """
#         user = User.objects.get(username='admin')
#         person = Person(user=user)
#         personform = PersonForm(instance=person)
#         personfields_wishdict = {'name': 'Olexandr',
#                                  'surname': 'Lykhenko',
#                                  'email': 'lykhenko.olexandr@gmail.com',
#                                 }

#         self.assertTrue(all(item in personform.initial.items() \
#                         for item in personfields_wishdict.items()))


#     def test_form_saves_values_to_instance_user_on_save(self):
#         """
#         test that, form saves name, surname, email values to corresponding User
#         when commiting form
#         """
#         person = Person.objects.get(user__username='admin')
#         personform = PersonForm(instance=person, data={'name': 'has_changed'})

#         if personform.is_valid():
#             person = personform.save()
#             self.assertEquals(User.objects.get(pk=person.user.pk).first_name, \
#              "has_changed")
#         else:
#             self.fail("personform not valid")

